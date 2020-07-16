import io

import pandas

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from newspaper import Article
import pandas as pd
from nltk.corpus import stopwords
import string
from nltk.stem.snowball import SnowballStemmer
import numpy as np
class ENT:
    s = []
    w = []
    sub = []
    author = []
    titl = []
    calend = []
    category = []
    i = 0

    def Crawl(self, url):
       # print("hy this is zero")
        uClient = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        page_html = urlopen(uClient).read()
        page_soup = soup(page_html, "html.parser")
        Container_1 = page_soup.find_all("h3", {"class": "story_heading"})
        Pagination = page_soup.find_all("div", {"class": "pagination"})

        for Container in Container_1:
            Links = Container.a["href"]
           # print(Links)
            self.w.append(Links)
      #  print("hy this is two")
        for Pag in Pagination:
            flag = 0
            Link_s = Pag.find_all("ul", {"class", "pgn_list"})
            # print(Link_s)
            self.i = self.i + 1
           # print(self.i, "	>>>>>>")
            for Lin in Link_s:
                Li = Lin.find_all("li")
                for Single_li in Li:
                    if Single_li.find("a", {"class", "next"}) and flag == 0 and self.i < 3:
                        Linkss = Single_li.a["href"]
                     #   print(Linkss)
                        self.Crawl(Linkss)
                    else:
                        # print("Doing Nothing")
                        flag = 0
                        continue
            #print("hy this is three")

    def cont(self):
        c=''
        iteration = 0
        for art in self.w:
            try:
                iteration = iteration + 1
                article = Article(art)
                article.download()
                article.parse()
                a = article.authors
                import datetime

                today = datetime.date.today()
                timestampStr = today.strftime("%Y-%m-%d")
                #timestampStr="2020-07-10"
               # print(timestampStr)
                d = article.publish_date
                e = str(d)
                q = e.split(' ')[0]
               # print(type(q))
                if timestampStr == q:
                    #print("article found with current date")
                    if a:
                        qq = str(a)
                        ddauthor = qq.strip('[]')
                        c = ddauthor.strip("''")
                        self.author.append(c)
                    else:
                        self.author.append("Web Desk")
                    self.calend.append(q)
                    self.titl.append(article.title)
                    #print(iteration, "==========-------------========>>>>>>>>>", "##")
                    self.sub.append(article.text)
                else:
                    pass
                    #print("no article found with current date")
            except:
                pass
            #    print("")

    def save_to_txt_file(self):
        print("Article for Entertainment has been crawled")
        list2 = [x.replace('\n', '') for x in self.sub]
        if self.author and self.titl and self.calend and list2:
            df = pd.DataFrame(
                data={"Author": self.author,
                      "Title": self.titl,
                      "PubDate": self.calend,
                      "content": list2})
            #print("hy  here&%&%&%&%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            df.to_csv(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\crawling\output\entertainment.txt", sep=',', index=False)
        else:
            with io.open(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\crawling\output\entertainment.txt", "w",
                         encoding="utf-8") as filehandle:
                filehandle.write(("Author,Title,PubDate,content"))


#myurl = 'https://www.bollywoodlife.com/page/1/'
#obj = ENT()
#obj.Crawl(myurl)
#obj.cont()
#obj.save_to_txt_file()


