import seaborn as sns
sns.set_style("whitegrid")
import warnings
warnings.filterwarnings("ignore")
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ShuffleSplit

class classify:
    def __init__(self):
        pass

    def feature_extraction(self):
        df = pd.read_csv(r"C:\Users\Sanau\PycharmProjects\FYP_Version_03\model_train\classification\dataset.txt")
        category_codes = {
            'Sports': 0,
            'Entertainment': 1,
            'Politics': 2
        }
        df['Category_Code'] = df['category']
        df = df.replace({'Category_Code': category_codes})
        #X_train = df['content']
        #y_train = df['Category_Code']
        #X_test = df['content']
        #y_test = df['Category_Code']
        X_train, X_test, y_train, y_test = train_test_split(df['content'],
                                                       df['Category_Code'],
                                                       test_size=0.15,
                                                       random_state=8)
        print("Train #####################################################################################################")
        print(y_train)
        print("\n")
        print("Train #####################################################################################################")
        print(y_test)

        ngram_range = (1, 2)
        min_df = 10
        max_df = 1.
        max_features = 300
        tfidf = TfidfVectorizer(encoding='utf-8',
                            ngram_range=ngram_range,
                            stop_words=None,
                            lowercase=False,
                            max_df=max_df,
                            min_df=min_df,
                            max_features=max_features,
                            norm='l2',
                            sublinear_tf=True)
        features_train = tfidf.fit_transform(X_train).toarray()
        labels_train = y_train
        #print(features_train.shape)
        #features_test = tfidf.transform(X_test).toarray()
        #labels_test = y_test
        #print(features_test.shape)
        data = open("tf__idf.pickle", "wb")
        pickle.dump(tfidf, data)
        data.close()
        return features_train,labels_train
    def impliment_svm(self):
        C = [.0001, .001, .01, .1]
        degree = [3, 4, 5]
        gamma = [1, 10, 100]
        probability = [True]
        param_grid = [
        {'C': C, 'kernel': ['linear'], 'probability': probability},
        {'C': C, 'kernel': ['poly'], 'degree': degree, 'probability': probability},
        {'C': C, 'kernel': ['rbf'], 'gamma': gamma, 'probability': probability}
        ]
        cv_sets = ShuffleSplit(n_splits=3, test_size=.33, random_state=8)
        svc = svm.SVC(random_state=8)
        grid_search = GridSearchCV(estimator=svc,
                               param_grid=param_grid,
                               scoring='accuracy',
                               cv=cv_sets,
                               verbose=1)
        features_train,labels_train = self.feature_extraction()
        grid_search.fit(features_train, labels_train)
        best_svc = grid_search.best_estimator_
        best_svc.fit(features_train, labels_train)
        pickle_out = open("svc_svc.pickle", "wb")
        pickle.dump(best_svc, pickle_out)
        pickle_out.close()

obj=classify()
obj.impliment_svm()