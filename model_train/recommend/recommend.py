import duplicates as duplicates
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances
class MyClass:

    my_list = []
    my_list1=[]
    new_list= []
    Author=[]
    pubdate=[]
    Title=[]
    Category=[]
    Content=[]
    def tfidf_based_model(self,row_index, num_similar_items):
        news_articles_temp = pd.read_csv(
            r'C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\recommend\history.txt', delimiter=',')
        tfidf_headline_vectorizer = TfidfVectorizer(min_df=0)
        tfidf_headline_features = tfidf_headline_vectorizer.fit_transform(news_articles_temp['Title'])
        couple_dist = pairwise_distances(tfidf_headline_features,tfidf_headline_features[row_index])
        indices = np.argsort(couple_dist.ravel())[0:num_similar_items]
        df = pd.DataFrame({'Author':news_articles_temp['Author'][indices].values,
                            'Title' : news_articles_temp['Title'][indices].values,
                            'PubDate': news_articles_temp['PubDate'][indices].values,
                            'Category': news_articles_temp['Category'][indices].values,
                            'Content': news_articles_temp['Content'][indices].values
                           })
        self.Author.append(news_articles_temp['Author'][indices[0]])
        self.Title.append(news_articles_temp['Title'][indices[0]])
        self.Category.append(news_articles_temp['Category'][indices[0]])
        self.Content.append(news_articles_temp['Content'][indices[0]])
        self.pubdate.append(news_articles_temp['PubDate'][indices[0]])

        #print('Title: ', self.news_articles_temp['Title'][indices[0]])
        #print('Author: ', self.news_articles_temp['Author'][indices[0]])
        #self.my_list.append(df.iloc[1])
    def tfidf_based_modell(self,row_index, num_similar_items):
        news_articles_temp = pd.read_csv(
            r'C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\recommend\history.txt', delimiter=',')
        tfidf_headline_vectorizer = TfidfVectorizer(min_df=0)
        tfidf_headline_features1 = tfidf_headline_vectorizer.fit_transform(news_articles_temp['Author'])
        couple_dist = pairwise_distances(tfidf_headline_features1,tfidf_headline_features1[row_index])
        indices = np.argsort(couple_dist.ravel())[0:num_similar_items]
        a = min(couple_dist)
        df = pd.DataFrame({
                            'Author':news_articles_temp['Author'][indices].values,
                            'Title' :news_articles_temp['Title'][indices].values,
                            'PubDate':news_articles_temp['PubDate'][indices].values,
                            'Category':news_articles_temp['Category'][indices].values,
                            'Content':news_articles_temp['Content'][indices].values

        })
        #print('Author: ', self.news_articles_temp['Author'][indices[0]])
        self.Author.append(news_articles_temp['Author'][indices[0]])
        self.Title.append(news_articles_temp['Title'][indices[0]])
        self.Category.append(news_articles_temp['Category'][indices[0]])
        self.Content.append(news_articles_temp['Content'][indices[0]])
        self.pubdate.append(news_articles_temp['PubDate'][indices[0]])
        #self.new_list.append(df.iloc[1])
    def result(self):
        for i in range(5):
            self.tfidf_based_model(i, 4)
        #print(obj.my_list)

        for j in range(5):
            self.tfidf_based_modell(j, 4)
        seen, result = set(), []
        for idx, item in enumerate(self.Content):
            if item not in seen:
                #print(item)
                seen.add(item)  # First time seeing the element
            else:
                result.append(idx)  # Already seen, add the index to the result
        n = (len(result))
        for i in range(n):
            j = result[i]
            #print(j)
            if i == 0:
                self.Content.pop(j)
                self.Author.pop(j)
                self.Title.pop(j)
                self.pubdate.pop(j)
                self.Category.pop(j)
            if i == 1:
                self.Content.pop(j -1)
                self.Author.pop(j - 1)
                self.Title.pop(j - 1)
                self.pubdate.pop(j - 1)
                self.Category.pop(j - 1)
            if i == 2:
                self.Content.pop(j - 2)
                self.Author.pop(j - 2)
                self.Title.pop(j - 2)
                self.pubdate.pop(j - 2)
                self.Category.pop(j - 2)
            if i == 3:
                self.Content.pop(j - 3)
                self.Author.pop(j - 3)
                self.Title.pop(j - 3)
                self.pubdate.pop(j - 3)
                self.Category.pop(j - 3)
            if i == 4:
                self.Content.pop(j - 4)
                self.Author.pop(j - 4)
                self.Title.pop(j - 4)
                self.pubdate.pop(j - 4)
                self.Category.pop(j - 4)
            if i == 5:
                self.Content.pop(j - 5)
                self.Author.pop(j - 5)
                self.Title.pop(j - 5)
                self.pubdate.pop(j - 5)
                self.Category.pop(j - 5)
            if i == 6:
                self.Content.pop(j - 6)
                self.Author.pop(j - 6)
                self.Title.pop(j - 6)
                self.pubdate.pop(j - 6)
                self.Category.pop(j - 6)
            if i == 7:
                self.Content.pop(j - 7)
                self.Author.pop(j - 7)
                self.Title.pop(j - 7)
                self.pubdate.pop(j - 7)
                self.Category.pop(j - 7)
            if i == 8:
                self.Content.pop(j - 8)
                self.Author.pop(j - 8)
                self.Title.pop(j - 8)
                self.pubdate.pop(j - 8)
                self.Category.pop(j - 8)
            if i == 9:
                self.Content.pop(j - 9)
                self.Author.pop(j - 9)
                self.Title.pop(j - 9)
                self.pubdate.pop(j - 9)
                self.Category.pop(j - 9)
            if i == 10:
                self.Content.pop(j - 10)
                self.Author.pop(j - 10)
                self.Title.pop(j - 10)
                self.pubdate.pop(j - 10)
                self.Category.pop(j - 10)

        #print(obj.new_list)
        #print(self.Author)
        #print(self.Title)
        #print(self.pubdate)
        #print(self.Category)
        #print(self.Content)
        return self.Author,self.Title,self.pubdate,self.Category,self.Content
#obj = MyClass()
#obj.result()
