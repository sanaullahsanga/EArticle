import io
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd
from newspaper import Article
import datetime
class SPT:
    Title_list = []
    Desc_list = []
    Amount_list = []
    DD_list = []
    major = []
    type = []
    type_i = 0
    sub = []
    author = []
    titl = []
    calend = []
    ####################################     CREATING FILE    ###################################
    # filename = "Youthhop.csv"from urllib.request import Request, urlopen
    # from bs4 import BeautifulSoup as soup
    # import pandas as pd
    # from newspaper import Article
    # f = open(filename, "w")
    # fieldnames = "Major, Type, Title , Description , Amount , Due_Date \n"
    # f.write(fieldnames)
    ####################################     SCRAPING    ###################################
    s = []
    w = []
    i = 0

    def Crawl(self, url):

        uClient = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        page_html = urlopen(uClient).read()
        page_soup = soup(page_html, "html.parser")
        Container_1 = page_soup.find_all("div", {"class": "content-inner layout-"})
        Pagination = page_soup.find_all("div", {"class": "pagination"})
        for Container in Container_1:
            Articles = Container.find_all("article")
            for Art in Articles:
                Link = Art.find_all("h2", {"class", "entry-title"})
                for L in Link:
                    Links = L.a["href"]

                   # print(Links)
                    self.w.append(Links)
        for Pag in Pagination:
            flag = 0
            Link_s = Pag.find_all("ul", {"class", "page-numbers"})
            # print(Link_s)
            for Lin in Link_s:
                Li = Lin.find_all("li")
                ##print(len(Li))
                for Single_li in Li:
                    # print(len(Li))

                    if Single_li.find("a", {"class", "next page-numbers"}) and flag == 0 and self.i < 3:
                        # print(len(Li))
                        Linkss = Single_li.a["href"]

                       # print(Linkss)
                        self.i += 1
                        # s.append(Linkss)
                        self.Crawl(Linkss)
                    else:
                        # print("Doing Nothing")
                        flag = 0
                        continue

    def cont(self):

        i = 0
        for art in self.w:
            try:
                article = Article(art)
                article.download()
                article.parse()
                a = article.authors
                today = datetime.date.today()
                timestampStr = today.strftime("%Y-%m-%d")
               # print(timestampStr)
                d = article.publish_date
                e = str(d)
                q = e.split(' ')[0]
                #print(type(q))
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
                    # print(iteration, "==========-------------========>>>>>>>>>", "##")
                    self.sub.append(article.text)
                else:
                    pass
                    #print("no article found with current date")
            except:
                pass
                #print("")

    def save_to_txt_file(self):
        print("Article for Sports has been crawled")
        list2 = [x.replace('\n', '') for x in self.sub]
        if self.author and self.titl and self.calend and list2:
            print("Articles found")
            df = pd.DataFrame(
                data={"Author": self.author,
                      "Title": self.titl,
                      "PubDate": self.calend,
                      "content": list2})

            df.to_csv(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\crawling\output\sports.txt", sep=',', index=False)
        else:
            print("Articles not found")
            with io.open(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\crawling\output\sports.txt", "w",
                         encoding="utf-8") as filehandle:
                filehandle.write(("Web Desk,Int’l Kabaddi tournament to be held in Pakistan in December,2020-07-07,ISLAMABAD International Kabaddi tournament will be held in Pakistan in December this year provided Corona pandemic comes under controlIn interview Secretary Pakistan Kabaddi Federation Mohammad Sarwar Rana said six countries including host Pakistan India Afghanistan Iran Canada and Australia will take part in the event in which one more team may be added later He said consent from all participating teams has been received"))

#myurl = 'https://www.pakistantoday.com.pk/sports/'
#obj = SPT()
#obj.Crawl(myurl)
#obj.cont()
#obj.save_to_txt_file()