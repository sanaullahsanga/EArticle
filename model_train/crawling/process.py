from model_train.Preprocessing.preprocesse import CleanData
from model_train.classification.classification import predict
from model_train.crawling.entertainment import ENT
from model_train.crawling.politics import POLI
from model_train.crawling.sports import SPT
#Crawling data from ENT
class Crawler:
    def __int__(self):
        pass
    def crawling(self):
        print("I am crawler")
        print("Crawling Start")
        # Crawling data from ENT
        obj = ENT()
        myurl = 'https://www.bollywoodlife.com/page/1/'
        obj.Crawl(myurl)
        obj.cont()
        obj.save_to_txt_file()
        # Crawling data from SPT
        obj1 = SPT()
        myurl = 'https://www.pakistantoday.com.pk/sports/'
        obj1.Crawl(myurl)
        obj1.cont()
        obj1.save_to_txt_file()
        # Crawling data from POLI
        obj2 = POLI()
        myurl = 'https://www.pakistantoday.com.pk/columns/'
        obj2.Crawl(myurl)
        obj2.cont()
        obj2.save_to_txt_file()
#object=Crawler()
#object.crawling()