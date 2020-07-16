
import pandas as pd
from nltk.corpus import stopwords
import string
from nltk.stem.snowball import SnowballStemmer


class CleanData:

    def  stop_words(self, text):
         sw = stopwords.words('english')
         sw=['?','(',')','[',']','❤','❤','-','❤','—','–','“','”',',', '.', 'THE', '?', 'The', '‘', '’', 'an', '*', '½', 'ï', '<', '>', '\w', '\d','�',
                          '\s','#','!','@','$','%','^','&','*']
         text = [word for word in text.split() if word not in sw]
         return " ".join(text)
    def remove(self,text):
        abc = text.replace("'s", '')
        abc = abc.replace("'", '')
        return abc

    def remove_punctuation(self,text):
        # replacing the punctuations with no space,         # which in effect deletes the punctuation marks

        translator = str.maketrans('', '',string.punctuation)  # return the text stripped of punctuation marks

        return text.translate(translator)


    def perform_stemming(self, text):

        stemmer = SnowballStemmer("english")

        text = [stemmer.stem(word) for word in text.split()]
        return " ".join(text)


    def cleaning(self):
        self.merging()
        data = pd.read_csv(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\Preprocessing\clean.txt")  # removing stop words from Content column and Title column
        data['content'] = data['content'].fillna("")
        data['Title']=data['Title'].fillna("")
        data['Title'] = data['Title'].apply(self.remove)
        data['content'] = data['content'].apply(self.stop_words)
        data['content'] = data['content'].apply(self.remove)
        data['content'] = data['content'].apply(self.remove_punctuation)
        #data['content'] = data['content'].apply(self.perform_stemming)
        #data['content'] = data['content'].str.lower()
        print("writing to the file")
        data.to_csv(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\Preprocessing\preprocessed.txt", sep=',', index=False)

    def merging(self):
        number = 0
        with open(r'C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\crawling\output\entertainment.txt',
                  encoding="latin-1") as ifh, open(
            r'C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\Preprocessing\clean.txt', 'w',
            encoding="latin-1") as ofh:
            #ofh.write("{},{},{},{}\n".format("Author", "Title", "PubDate","content"))
            for lineno, line in enumerate(ifh):
                line = line.rstrip()  # remove newline
                ofh.write(line + '\n')
                number = number + 1
        with open(r'C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\crawling\output\politics.txt',
                  encoding="latin-1") as ifh, open(
                r'C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\Preprocessing\clean.txt', 'a',
                encoding="latin-1") as ofh:
            number = 0
            for lineno, line in enumerate(ifh):
                line = line.rstrip()  # remove newline
                ofh.write(line + '\n')
                number = number + 1
        with open(r'C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\crawling\output\sports.txt',
                  encoding="latin-1") as ifh, open(
            r'C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\Preprocessing\clean.txt', 'a',
            encoding="latin-1") as ofh:
            number = 0
            for lineno, line in enumerate(ifh):
                line = line.rstrip()  # remove newline
                ofh.write(line + '\n')
                number = number + 1


#cd = CleanData()
#cd.merging()
#cd.cleaning()