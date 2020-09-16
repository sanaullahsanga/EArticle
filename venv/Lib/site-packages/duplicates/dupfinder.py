import hashlib
import stat
import sys
import traceback

from pathlib import Path



class DupFinder:
    def __init__(self, **kwargs):
        self.ignore_symlinks = kwargs.get("ignore_symlinks", True)
        self.ignore_hidden = kwargs.get("ignore_hidden", True)
        self.ignore_mounts = kwargs.get("ignore_mounts", False)
        self.verbose = kwargs.get("verbose", False)
        self.debug = kwargs.get("debug", False)


    @staticmethod
    def flatten(*args):
        result = []
        for item in args:
            if isinstance(item, (list, tuple)):
                for subitem in DupFinder.flatten(*item):
                    result.append(subitem)
            else:
                result.append(item)
        return result


    @staticmethod
    def filetype(path, unknown="", prefix="", suffix=""):
        def _get_type_of(path):
            mode = path.stat().st_mode
            if stat.S_ISDIR(mode):
                if path.is_mount():
                    return "mountpoint"
                else:
                    return "directory"
            elif stat.S_ISLNK(mode):
                return "symlink"
            elif stat.S_ISSOCK(mode):
                return "socket"
            elif stat.S_ISFIFO(mode):
                return "fifo"
            elif stat.S_ISCHR(mode) or stat.S_ISBLK(mode):
                return "device"
            elif stat.S_ISREG(mode):
                return "file"
            else:
                return None
        ft = _get_type_of(path)
        return prefix+ft+suffix if ft else unknown


    @staticmethod
    def _to_stderr(*text, prefix="MSG", active=True):
        if active:
            print(prefix+":", *text, file=sys.stderr)


    def _error_out(self, *text, prefix="ERROR"):
        DupFinder._to_stderr(*text, prefix=prefix)


    def _info_out(self, *text, prefix="INFO"):
        DupFinder._to_stderr(*text, prefix=prefix, active=self.verbose or self.debug)


    def _debug_out(self, *text, prefix="DEBUG"):
        DupFinder._to_stderr(*text, prefix=prefix, active=self.debug)


    def _fingerprint(self, path, blocksize=1048576):
        m = hashlib.sha256()
        with open(path, "rb") as f:
            block = f.read(blocksize)
            while block:
                m.update(block)
                block = f.read(blocksize)
        return m.hexdigest()


    def _stat_file(self, path):
        self._debug_out(path, prefix="FILE")
        stat = Path.stat(path)
        age = max(stat.st_mtime, stat.st_ctime)
        size = stat.st_size
        return {"path":path, "size":size, "age":age}


    def _scan_dir(self, path, files):
        self._debug_out(path, prefix="DIR")
        for entry in path.iterdir():
            try:
                if self.ignore_symlinks and entry.is_symlink():
                    self._info_out(f"Ignoring symlink '{entry}'")
                elif self.ignore_hidden and entry.name.startswith("."):
                    self._info_out(f"Ignoring hidden {DupFinder.filetype(entry, suffix=' ')}'{entry}'")
                elif Path.is_dir(entry):
                    if self.ignore_mounts and entry.is_mount():
                        self._info_out(f"Ignoring mountpoint '{entry}'")
                    else:
                        self._scan_dir(entry, files)
                elif entry.is_file():
                    files.append(self._stat_file(entry))
                else:
                    self._info_out(f"Ignoring {DupFinder.filetype(entry, suffix=' ')}'{entry}'")
            except (SystemExit, KeyboardInterrupt):
                raise
            except PermissionError:
                self._info_out(f"Access denied to {DupFinder.filetype(entry, suffix=' ')}'{entry}'")
            except Exception as exc:
                self._error_out(f"{exc}")
                if self.debug:
                    traceback.print_exc()
        return files


    def scan(self, *paths):
        # Gather all file objects
        files = []
        for path in [p if isinstance(p, Path) else Path(str(p)) for p in paths]:
            if path.exists():
                if path.is_dir():
                    self._scan_dir(path, files)
                elif path.is_file():
                    files.append(self._stat_file(path))
                else:
                    self._info_out(f"Ignoring {DupFinder.filetype(path, suffix=' ')}'{path}'")
            else:
                self._info_out(f"'{path}' not found")
        # Duplicates must have same size
        sizes = {}
        for f in files:
            s = f["size"]
            if s in sizes:
                sizes[s].append(f)
            else:
                sizes[s] = [f]
        self._debug_out(f"{len(files)} files of {len(sizes)} different sizes")
        # Separate unique files from possible duplicates
        uniq = [v for k, v in sizes.items() if len(v)==1 or k==0]
        ident = [v for k, v in sizes.items() if len(v)>1 and k!=0]
        if 0 in sizes and len(sizes[0])>1:
            self._info_out(f"{len(sizes[0])} empty files are not considered identical")
        # Check fingerprint of all candidates
        hashes = {}
        for cand in ident:
            for f in cand:
                try:
                    fp = self._fingerprint(f["path"])
                    f["hash"] = fp
                    if fp in hashes:
                        hashes[fp].append(f)
                    else:
                        hashes[fp] = [f]
                except (PermissionError, IOError):
                    self._error_out(f"Unable to read content of '{f['path']}'")
        # Separate unique files from duplicates
        dup = []
        for items in hashes.values():
            if len(items)==1:
                uniq.append(items[0])
            elif len(items)>1:
                dup.append(items)

        return DupFinder.flatten(uniq), dup


# vim: set et sw=4 ts=4:
