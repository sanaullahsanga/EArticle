import io
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from newspaper import Article
import pandas as pd
####################################     VARIABLES    ###################################
class POLI:
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

                    #print(Links)
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

                        #print(Linkss)
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
                import datetime

                today = datetime.date.today()
                timestampStr = today.strftime("%Y-%m-%d")
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
                    # print(iteration, "==========-------------========>>>>>>>>>", "##")
                    self.sub.append(article.text)
                else:
                    pass
                    #print("no article found with current date")

            except:
                pass
                #print("")

    def save_to_txt_file(self):
        print("Article for Politics has been crawled")
        list2 = [x.replace('\n', '') for x in self.sub]
        if self.author and self.titl and self.calend and list2:
            print("Articles found")
            df = pd.DataFrame(
                data={"Author": self.author,
                      "Title": self.titl,
                      "PubDate": self.calend,
                      " content": list2})


            df.to_csv(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\crawling\output\politics.txt", sep=',', index=False)
        else:
            print("Articles not found")
            with io.open(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\crawling\output\politics.txt", "w",
                         encoding="utf-8") as filehandle:
                filehandle.write(("Web Desk,Positive aspects of new federal budget,2020-07-10,It was tough but the budget had some good things tooBy Muhammad Zahid RifatThere is no denying the that the federal budget for financial year 202021 which has already commenced on July 1 was formulated in the very unusual and difficult circumstances and conditions caused by the covid19 pandemic which affected Pakistan as it did to countries around the world one after the otherEverything was going in the right direction following the bold and necessary policy decisions of the Federal Government economic recovery was on upward trajectory and there were encouraging positive signs of the stabilization of the national economy which had been in the bad shape for some time This was till March 2020 the third quarter of the outgoing financial year 201920 All this can be affirmed by the appreciable improvement in major economic indicators of the country during the first nine months of FY 2019The current account deficit had reduced by 73 pe cent from 10 billion to 3 billion the trade deficit had decreased by 31 percent from 21 billion to 15 billion the fiscal deficit had reduced from 5 percent to 38 percent of the GDP a primary surplus of 04 of the GDP was achieved for the first time in 10 years Federal Board of Revenue FBR revenue collection had increased by 17 per cent and the federal government was on the track to achieve the revised revenue generation target of Rs 4800 billion Nontax revenue had increased by as much as 134 per cent against the annual target of Rs 1161 billion remittances back home from overseas Pakistanis had increased to 17 billion Foreign Direct Investment FDI had almost been doubled from 09 billion to 215 billionThe new federal budget for financial year 202021 the second regular budget presentation by the PTI government has undoubtedly been a crisis budget prepared under very unusual and difficult circumstances requiring a wellthought philosophy and approach by all concernedFurthermore debt management had improved by shifting 74 percent of the domestic debt portfolio to long term resulting in reduction of0 domestic borrowing rates from 14 percent to 10 percent besides a saving of Rs 240 billion Due to the reforms introduced by the federal government Extended Fund Facility EFF of 6 billion was approved by the International Monetary Fund IMF Only in December 2019 Bloomberg had ranked the Pakistan Stock Exchange as one of the top performing markets of the world Moody’s rating was upgraded from B3Negative to B3Positive Pakistan’s “Ease of Doing Business” ranking had improved and Significant progress was made on as many as 27 actionable items included in the Financial Action Task Force FATF action planAnd then came the attack of the covid19 pandemic which has turned out to be a very severe global economic threat having the potential of destabilizing the international economic system Pakistan was no exception to the general disorder as the corona virus adversely impacted the economy of the country forcing the economic team managers to do fresh thinking and reset the targets for financial year 202021 immediate economic repercussions of covid19 for Pakistan during FY 20192020 are briefly indicatedThe industry and the retail businesses all over Pakistan have been badly affected Economic growth has been reduced by Rs 3 trillion bringing down the GDP growth projection from 33 percent to 04 percent Projection of overall budget deficit has been revised upward from 71percent to 91 percent of GDP FBR revenue loss has been projected at Rs 900 billion Nontax revenue of the federal government has been reduced by Rs 102 billion Exports and remittances back home from Overseas Pakistanis have been badly Unemployment and poverty have increased Large scale manufacturing and Foreign Direct Investment FDI have declined Domestic tourism in Pakistan has stalledThe new federal budget for financial year 202021 the second regular budget presentation by the PTI government has undoubtedly been a crisis budget prepared under very unusual and difficult circumstances requiring a wellthought philosophy and approach by all concernedThe federal government has positively stood up to the socioeconomic challenge by reaching out to the vulnerable segments of the society and business community to neutralize the negative impact of lockdown and unemployment federal government has also given relief to the farmers community and daily wage earners incentives have been provided to the construction sector for stimulating the national economy and the State Bank of Pakistan has also introduced a number of initiatives for businesses to neutralize the negative impact of closure owing to persisting pandemic COVID19Following are the positive aspects and main features of the new federal budget philosophy briefly speaking1Striking a balance between Corona expenditure and fiscal deficit2Keeping the primary balance at sustainable levelProtection of social spending under the Ehsaas Programme to support the vulnerable segments of the society Resource mobilization without unnecessary changes in tax structure Successful continuation of the IMF programme Carrying forward of the Stimulus Package of more than Rs 1200 billion Keeping the development budget at adequate level to stimulate economic growth of the country Defence and internal security of the country has been given due importance in the prevailing circumstances and persisting hostile activities by India Housing initiatives including Naya Pakistan Housing project have been funded Funding for special areas that is erstwhile FATA since merged in Khyber Pakhtunkhwa Azad Jammu and Kashmir GilgitBaltistan has also been ensured for their development special initiatives led by the Prime Minister like Kamyab Jawan Sehat Card Billion Trees Tsunami and so on have also been protected Austerity and rationalization of expenditures will be observed13The sSubsidy regime has been rationalized to provide targeted subsidy to the deserving segments of the societyThe National Finance Commission NFC Award is to be revisited More the provinces will be asked to fulfill the funding commitment made at the time of the merger of erstwhile FATA"))


#myurl = 'https://www.pakistantoday.com.pk/columns/'
#obj = POLI()
#obj.Crawl(myurl)
#obj.cont()
#obj.save_to_txt_file()
