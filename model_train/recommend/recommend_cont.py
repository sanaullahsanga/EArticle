import numpy as np
import pandas as pd
from pandas import CategoricalDtype
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
#nltk.download('punkt')

class recommend:
    def __init__(self):
        pass
    def article_train(self):
        n = 10
        dt = pd.read_csv(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\recommend\cont.txt", error_bad_lines=False)
        df = pd.read_csv(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\recommend\data.txt", error_bad_lines=False,
                         names=['Author', 'Title', 'PubDate', 'Category', 'Content'])

        X_train = df['Content']
        X_train_sections = df['Category']
        X_test = dt['content']
        X_test_sections = dt['category']
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_vectorizer.fit(X_train)
        X_train_tfidf = tfidf_vectorizer.transform(X_train)
        X_test_tfidf = tfidf_vectorizer.transform(dt['content'].apply(lambda x: np.str_(x)))
        #X_test_tfidf = tfidf_vectorizer.transform(X_)
        return X_train_tfidf, X_test_tfidf, X_train_sections, X_test_sections, X_train

    def get_top_n_rec_articles(self,X_train_tfidf, X_train, test_article, X_train_sections, n=5):
        similarity_scores = X_train_tfidf.dot(test_article.toarray().T)
        sorted_indicies = np.argsort(similarity_scores, axis=0)[::-1]
        sorted_sim_scores = similarity_scores[sorted_indicies]
        temp = sorted_indicies[:n]
        #print(temp)5
        top_n_recs = []
        rec_sections = []
        for item in temp:
            s = pd.Series(X_train[item])
            #top_n_recs.append(s.to_string(index=False))
            top_n_recs.append(s.values.tolist())
            s1 = pd.Series(X_train_sections[item].to_string(index=False))

            rec_sections.append(s1.to_string(index=False))
            #print(X_train_sections[item])
        return top_n_recs, rec_sections, sorted_sim_scores
    def category(self):
        X_train_tfidf, X_test_tfidf, X_train_sections, X_test_sections, X_train = self.article_train()
        test_article = X_test_tfidf[0]

        # return the top n most similar articles as recommendations
        top_n_recs, rec_sections, sorted_sim_scores = self.get_top_n_rec_articles(X_train_tfidf, X_train, test_article,
                                                                              X_train_sections, n=5)
        print(top_n_recs[:5])
        return(top_n_recs[:5],rec_sections[:5])
#object=recommend()
#object.category()