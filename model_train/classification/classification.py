import io
import pickle
import string
import pandas as pd
from nltk import SnowballStemmer
from nltk.corpus import stopwords

class predict:
    def __init__(self):
        pass
    def clean_text_preprocessing(self,text):
        sw = stopwords.words('english')
        text = [word.lower() for word in text.split() if word.lower() not in sw]
        stop_words_removed = " ".join(text)
        translator = str.maketrans('', '', string.punctuation)  # return the text stripped of punctuation marks
        punctuation_removed = stop_words_removed.translate(translator)
        stemmer = SnowballStemmer("english")
        root_words_extracted = [stemmer.stem(word) for word in punctuation_removed.split()]
        root_words_joined_with_space = " ".join(root_words_extracted)
        final_text = root_words_joined_with_space.lower()
        return final_text

    def create_features_from_text(self,text):
        with open(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\classification\tf__idf.pickle", 'rb') as data:
            tf__idf = pickle.load(data)
        df = pd.DataFrame(columns=['Content'])
        df.loc[0] = self.clean_text_preprocessing(text)
        features = tf__idf.transform(df['Content']).toarray()
        return features

    def get_category_name(self,category_id):
        category_codes = {'Sports': 0, 'Entertainment': 1, 'Politics': 2}
        for category, id_ in category_codes.items():
            if id_ == category_id:
                return category

    def predict_from_text(self,text):
        with open(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\classification\svc_svc.pickle", 'rb') as data:
            svc_model = pickle.load(data)
        a = self.create_features_from_text(text)
        prediction_svc = svc_model.predict(a)[0]
        #prediction_svc_proba = svc_model.predict_proba(self.create_features_from_text(text))[0]
        # Return result
        category_svc = self.get_category_name(prediction_svc)
        #print("The predicted category using the SVM model is %s." % (category_svc))
        #print("The conditional probability is: %a" % (prediction_svc_proba.max() * 100))

        return category_svc

    def category(self):
        dataset = pd.read_csv(
            r'C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\Preprocessing\preprocessed.txt',
            names=['Author', 'Title', 'PubDate', 'content'])
        number = 0
        with open(r'C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\Preprocessing\preprocessed.txt',
                  encoding="latin-1") as ifh, open(
            r'C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\classification\categorize.txt', 'w',
            encoding="latin-1") as ofh:
            for lineno, line in enumerate(ifh):
                cate = self.predict_from_text(dataset.content[number])
                line = line.rstrip()  # remove newline
                line += ',' + cate  # append category
                ofh.write(line + '\n')
                number = number + 1
    def cont_cat(self,text):
        cate = self.predict_from_text(text)
        return cate




#obj=predict()
#obj.category()
