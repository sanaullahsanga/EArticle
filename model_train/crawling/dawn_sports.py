from newspaper import Article
import newspaper
import pandas as pd
class MyClass:
    s = []
    w = []
    sub = []
    author = []
    titl = []
    cal = []
    content = []
    category = []
    i = 0
    

    count=0
    def Crawl(self):
        print("crawl start %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        myurl = 'https://www.dawn.com/sport'
        article = Article(myurl)
        cnn_paper = newspaper.build(myurl,memoize_articles=False)
        slist=[]
        for article in cnn_paper.articles:
            print("for loop start")
            if self.i < 100 :
                print("first if start $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print(article.url)
                slist.append(article.url)
                self.i +=1
            else:
                break
        for link in slist:
            if self.count % 3 == 0:
                try:
                    print("2nd if starts %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% with try")
                    article = Article(link)
                    article.download()
                    article.parse()
                    a = article.authors
                    str1 = ""
                    # traverse in the string
                    for ele in a:
                        str1 += ele
                    import datetime
                    today = datetime.date.today()
                    timestampStr = today.strftime("%Y-%m-%d")

                    print(timestampStr)
                    b=article.publish_date
                    e = str(b)
                    q = e.split(' ')[0]
                    print(type(q))

                    print(q)
                    c=article.title
                    str2 = ''
                    # traverse in the string
                    for ele in c:
                        str2 += ele
                    if q == timestampStr:
                        print("3rd if starts %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ")
                        self.titl.append(str2)
                        self.content.append(article.text)
                        self.author.append(str1)
                        self.cal.append(q)
                    self.count += 1
                except:
                    print("going in except")
                    self.count += 1
                    print("")
            else:
                print("going in else ")
                self.count += 1
        print("crawl done $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    def save_to_txt_file(self):
        list2 = [x.replace('\n', '') for x in self.content]
        if self.author and self.titl and self.cal and list2:
            df = pd.DataFrame(
                data={"Author": self.author,
                      "Title": self.titl,
                      "PubDate": self.cal,
                      " content": list2})
            print("hy i am printer 555555555555555555555555555555555555555555555555555555555555555555555555555")
            df.to_csv(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\crawling\output\check.txt", sep=',', index=False)
        print("save to file done $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
obj = MyClass()
obj.Crawl()
obj.save_to_txt_file()

            