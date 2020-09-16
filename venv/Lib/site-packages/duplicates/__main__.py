#!/usr/bin/python3
#
# duplicates - Find files with identical content.
#
# Copyright (c) 2019, Stefan Schönberger <me@s5s9r.de>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import argparse
from pathlib import Path
import re
import sys

from . dupfinder import DupFinder


def natural_key(text):
    convert = lambda st: int(st) if st.isdigit() else st.lower()
    return [convert(part) for part in re.split('([0-9]+)', str(text))]


def path_sort(l): 
    path_key = lambda item: natural_key(item["path"])
    return sorted(l, key = path_key)


def dup_sort(l):
    dup_key = lambda item: (item["age"], natural_key(item["path"]))
    return sorted(l, key = dup_key)


def s_or_p(n, singular, plural):
    if n==1:
        return f"{n} {singular}"
    else:
        return f"{n} {plural}"


def main():
    parser = argparse.ArgumentParser(description="Search for identical files.")

    parser.add_argument("path", type=Path, nargs="+", help="Paths to scan.")
    parser.add_argument("--follow",
            help="Symlinks not followed by default.",
            action="store_true")
    parser.add_argument("--hidden",
            help="Files in hidden directories are ignored by default.",
            action="store_true")
    parser.add_argument("--one-file-system",
            help="Do not enter mounted file systems.",
            action="store_true")
    parser.add_argument("--unique",
            help="Print also unique files.",
            action="store_true")
    parser.add_argument("--dups-only",
            help="Print only duplicates, no uniques and no originals, zero-delimited.",
            action="store_true")
    parser.add_argument("--verbose",
            help="Print more information.",
            action="store_true")
    parser.add_argument("--summary",
            help="Print the final summary.",
            action="store_true")
    parser.add_argument("--debug",
            help="Print debug output.",
            action="store_true")

    args = parser.parse_args()

    try:
        df = DupFinder(
            ignore_symlinks=not args.follow,
            ignore_hidden=not args.hidden,
            ignore_mounts=args.one_file_system,
            verbose=args.verbose,
            debug=args.debug,
        )
        uniq, dup = df.scan(*args.path)

        if args.unique and not args.dups_only:
            for item in path_sort(uniq):
                print(item["path"])
            print("")

        dup_files = 0
        for items in dup:
            dup_files += len(items)
            files = dup_sort(items)
            if args.dups_only:
                print(*[f["path"] for f in files[1:]], sep="\0")
            else:
                print(files[0]["path"])
                for f in files[1:]:
                    print("\t", f["path"], sep="")

        if args.verbose or args.summary:
            uniq_files = len(uniq)
            dup_count = dup_files - len(dup)
            total_files = uniq_files + dup_files
            print(
                "SUMMARY:",
                f"{s_or_p(total_files, 'file', 'files')} total,",
                f"{s_or_p(dup_count, 'duplicate', 'duplicates')}",
                f"out of {s_or_p(len(dup), 'file', 'files')}",
                file=sys.stderr
            )

    except KeyboardInterrupt:
        print("Stopped.", file=sys.stderr)


if __name__ == "__main__":
    main()

# vim: set et sw=4 ts=4:
