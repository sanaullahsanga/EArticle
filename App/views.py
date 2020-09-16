import datetime
import io
from collections import namedtuple
import pandas as pd
from nltk import word_tokenize, re
from nltk.corpus import stopwords
from nltk.tokenize.treebank import TreebankWordDetokenizer
from App.Database.conn import connection
from model_train.Preprocessing.preprocesse import CleanData
from model_train.classification.classification import predict
from model_train.crawling.process import Crawler
from model_train.recommend.recommend_cont import recommend
from model_train.recommend.recommend import MyClass
from model_train.crawling.entertainment import ENT
from model_train.crawling.politics import POLI
from model_train.crawling.sports import SPT
stop_words = set(stopwords.words('english'))
new_stopwords = [',', '.', 'THE', '?', 'The', ')', '(', '‘', '’', 'an','.']
new_stopwords_list = stop_words.union(new_stopwords)
from django.shortcuts import render
object=connection()
conn=object.connection_to_database()
cursor=conn.cursor()
# Create your views here.
# Admin Functions
def index(request):
    if request.session.has_key('loged'):
        obj = connection()
        conn = obj.connection_to_database()
        cursor = conn.cursor()
        counts = "select count(email) from users "
        cursor.execute(counts)
        row = cursor.fetchone()
        while row:
            counts = str(row[0])
            row = cursor.fetchone()
        admincount = "select count(email) from users where type='Admin'"
        cursor.execute(admincount)
        row = cursor.fetchone()
        while row:
            admincount = str(row[0])
            row = cursor.fetchone()
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            count_sport = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            count_entertainment = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            count_politics = str(row[0])
            row = cursor.fetchone()
        count_total_articles = "select count(name) from article "
        cursor.execute(count_total_articles)
        row = cursor.fetchone()
        while row:
            count_total_articles = str(row[0])
            row = cursor.fetchone()
        if request.session['type']=="Admin":
            return render(request, 'admin_pages/admin.html',
                          {'user_name': request.session['name'], 'user_type': request.session['type'], 'total': counts,
                           'admincount': admincount,
                           'countsport': count_sport, 'countentertainment': count_entertainment,
                           'countpolitics': count_politics,
                           'TotalArticles': count_total_articles})
        else:
            return render(request, 'user_pages/user.html',
                          {'user_name': request.session['name'], 'user_type': request.session['type'], 'total': counts,
                           'admincount': admincount,
                           'countsport': count_sport, 'countentertainment': count_entertainment,
                           'countpolitics': count_politics,
                           'TotalArticles': count_total_articles})
    else:
        return render(request,'main_pages/index.html')
def about(request):
    if request.session.has_key('loged'):
        obj = connection()
        conn = obj.connection_to_database()
        cursor = conn.cursor()
        counts = "select count(email) from users "
        cursor.execute(counts)
        row = cursor.fetchone()
        while row:
            counts = str(row[0])
            row = cursor.fetchone()
        admincount = "select count(email) from users where type='Admin'"
        cursor.execute(admincount)
        row = cursor.fetchone()
        while row:
            admincount = str(row[0])
            row = cursor.fetchone()
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            count_sport = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            count_entertainment = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            count_politics = str(row[0])
            row = cursor.fetchone()
        count_total_articles = "select count(name) from article "
        cursor.execute(count_total_articles)
        row = cursor.fetchone()
        while row:
            count_total_articles = str(row[0])
            row = cursor.fetchone()
        if request.session['type']=="Admin":
            return render(request, 'admin_pages/admin.html',
                          {'user_name': request.session['name'], 'user_type': request.session['type'], 'total': counts,
                           'admincount': admincount,
                           'countsport': count_sport, 'countentertainment': count_entertainment,
                           'countpolitics': count_politics,
                           'TotalArticles': count_total_articles})
        else:
            return render(request, 'user_pages/user.html',
                          {'user_name': request.session['name'], 'user_type': request.session['type'], 'total': counts,
                           'admincount': admincount,
                           'countsport': count_sport, 'countentertainment': count_entertainment,
                           'countpolitics': count_politics,
                           'TotalArticles': count_total_articles})
    else:
        return render(request,'main_pages/about.html')
def login(request):
    if request.session.has_key('loged'):
        obj = connection()
        conn = obj.connection_to_database()
        cursor = conn.cursor()
        counts = "select count(email) from users "
        cursor.execute(counts)
        row = cursor.fetchone()
        while row:
            counts = str(row[0])
            row = cursor.fetchone()
        admincount = "select count(email) from users where type='Admin'"
        cursor.execute(admincount)
        row = cursor.fetchone()
        while row:
            admincount = str(row[0])
            row = cursor.fetchone()
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            count_sport = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            count_entertainment = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            count_politics = str(row[0])
            row = cursor.fetchone()
        count_total_articles = "select count(name) from article "
        cursor.execute(count_total_articles)
        row = cursor.fetchone()
        while row:
            count_total_articles = str(row[0])
            row = cursor.fetchone()
        if request.session['type']=="Admin":
            return render(request, 'admin_pages/admin.html',
                          {'user_name': request.session['name'], 'user_type': request.session['type'], 'total': counts,
                           'admincount': admincount,
                           'countsport': count_sport, 'countentertainment': count_entertainment,
                           'countpolitics': count_politics,
                           'TotalArticles': count_total_articles})
        else:
            return render(request, 'user_pages/user.html',
                          {'user_name': request.session['name'], 'user_type': request.session['type'], 'total': counts,
                           'admincount': admincount,
                           'countsport': count_sport, 'countentertainment': count_entertainment,
                           'countpolitics': count_politics,
                           'TotalArticles': count_total_articles})
    else:
        return render(request,'main_pages/login.html')
def register(request):
    if request.session.has_key('loged'):
        obj = connection()
        conn = obj.connection_to_database()
        cursor = conn.cursor()
        counts = "select count(email) from users "
        cursor.execute(counts)
        row = cursor.fetchone()
        while row:
            counts = str(row[0])
            row = cursor.fetchone()
        admincount = "select count(email) from users where type='Admin'"
        cursor.execute(admincount)
        row = cursor.fetchone()
        while row:
            admincount = str(row[0])
            row = cursor.fetchone()
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            count_sport = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            count_entertainment = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            count_politics = str(row[0])
            row = cursor.fetchone()
        count_total_articles = "select count(name) from article "
        cursor.execute(count_total_articles)
        row = cursor.fetchone()
        while row:
            count_total_articles = str(row[0])
            row = cursor.fetchone()
        if request.session['type']=="Admin":
            return render(request, 'admin_pages/admin.html',
                          {'user_name': request.session['name'], 'user_type': request.session['type'], 'total': counts,
                           'admincount': admincount,
                           'countsport': count_sport, 'countentertainment': count_entertainment,
                           'countpolitics': count_politics,
                           'TotalArticles': count_total_articles})
        else:
            return render(request, 'user_pages/user.html',
                          {'user_name': request.session['name'], 'user_type': request.session['type'], 'total': counts,
                           'admincount': admincount,
                           'countsport': count_sport, 'countentertainment': count_entertainment,
                           'countpolitics': count_politics,
                           'TotalArticles': count_total_articles})
    else:
        return render(request,'main_pages/register.html')
def registration(request):
    if request.session.has_key('loged'):
        obj = connection()
        conn = obj.connection_to_database()
        cursor = conn.cursor()
        counts = "select count(email) from users "
        cursor.execute(counts)
        row = cursor.fetchone()
        while row:
            counts = str(row[0])
            row = cursor.fetchone()
        admincount = "select count(email) from users where type='Admin'"
        cursor.execute(admincount)
        row = cursor.fetchone()
        while row:
            admincount = str(row[0])
            row = cursor.fetchone()
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            count_sport = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            count_entertainment = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            count_politics = str(row[0])
            row = cursor.fetchone()
        count_total_articles = "select count(name) from article "
        cursor.execute(count_total_articles)
        row = cursor.fetchone()
        while row:
            count_total_articles = str(row[0])
            row = cursor.fetchone()
        if request.session['type']=="Admin":
            return render(request, 'admin_pages/admin.html',
                          {'user_name': request.session['name'], 'user_type': request.session['type'], 'total': counts,
                           'admincount': admincount,
                           'countsport': count_sport, 'countentertainment': count_entertainment,
                           'countpolitics': count_politics,
                           'TotalArticles': count_total_articles})
        else:
            return render(request, 'user_pages/user.html',
                          {'user_name': request.session['name'], 'user_type': request.session['type'], 'total': counts,
                           'admincount': admincount,
                           'countsport': count_sport, 'countentertainment': count_entertainment,
                           'countpolitics': count_politics,
                           'TotalArticles': count_total_articles})
    else:
        names = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        type = 'User'
        obj = connection()
        conn = obj.connection_to_database()
        sql = "insert into users values ('" + names + "','" + email + "','" + password + "','" + type + "')"
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        # check=usertable(name=request.POST['name'], email=request.POST['email'], password=request.POST['password'],type='User')
        # check.save()
        return render(request, 'main_pages/login.html')
def loginAuth(request):
    if request.session.has_key('loged'):
        obj = connection()
        conn = obj.connection_to_database()
        cursor = conn.cursor()
        counts = "select count(email) from users "
        cursor.execute(counts)
        row = cursor.fetchone()
        while row:
            counts = str(row[0])
            row = cursor.fetchone()
        admincount = "select count(email) from users where type='Admin'"
        cursor.execute(admincount)
        row = cursor.fetchone()
        while row:
            admincount = str(row[0])
            row = cursor.fetchone()
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            count_sport = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            count_entertainment = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            count_politics = str(row[0])
            row = cursor.fetchone()
        count_total_articles = "select count(name) from article "
        cursor.execute(count_total_articles)
        row = cursor.fetchone()
        while row:
            count_total_articles = str(row[0])
            row = cursor.fetchone()

        return render(request, 'admin_pages/admin.html',
                      {'user_name': request.session['name'], 'user_type': request.session['type'], 'total': counts,
                       'admincount': admincount,
                       'countsport': count_sport, 'countentertainment': count_entertainment,
                       'countpolitics': count_politics,
                       'TotalArticles': count_total_articles})

    else:
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            sql="select name,email,type from users where email='"+email+"' and password='"+password+"'"
            obj = connection()
            conn = obj.connection_to_database()
            cursor=conn.cursor()
            if cursor.execute(sql):
                row = cursor.fetchone()
                if row:
                    while row:
                        print(str(row[0]))
                        request.session['loged'] = True
                        request.session['name'] = str(row[0])
                        request.session['email'] = str(row[1])
                        request.session['type'] = str(row[2])
                        row = cursor.fetchone()
                    counts = "select count(email) from users "
                    cursor.execute(counts)
                    row = cursor.fetchone()
                    while row:
                        counts = str(row[0])
                        row = cursor.fetchone()
                    admincount = "select count(email) from users where type='Admin'"
                    cursor.execute(admincount)
                    row = cursor.fetchone()
                    while row:
                        admincount = str(row[0])
                        row = cursor.fetchone()
                    count_sport = "select count(name) from article where category='Sports'"
                    cursor.execute(count_sport)
                    row = cursor.fetchone()
                    while row:
                        count_sport = str(row[0])
                        row = cursor.fetchone()
                    count_entertainment = "select count(name) from article where category='Entertainment'"
                    cursor.execute(count_entertainment)
                    row = cursor.fetchone()
                    while row:
                        count_entertainment = str(row[0])
                        row = cursor.fetchone()
                    count_politics = "select count(name) from article where category='Politics'"
                    cursor.execute(count_politics)
                    row = cursor.fetchone()
                    while row:
                        count_politics = str(row[0])
                        row = cursor.fetchone()
                    count_total_articles = "select count(name) from article "
                    cursor.execute(count_total_articles)
                    row = cursor.fetchone()
                    while row:
                        count_total_articles = str(row[0])
                        row = cursor.fetchone()
                    if request.session['type'] == 'Admin':
                        return render(request, 'admin_pages/admin.html',
                                      {'user_name': request.session['name'], 'user_type': request.session['type'],
                                       'total': counts, 'admincount': admincount,
                                       'countsport': count_sport, 'countentertainment': count_entertainment,
                                       'countpolitics': count_politics,
                                       'TotalArticles': count_total_articles})
                    elif request.session['type'] == 'User':
                        return render(request, 'user_pages/user.html',
                                      {'user_name': request.session['name'], 'user_type': request.session['type'],
                                       'total': counts, 'admincount': admincount,
                                       'countsport': count_sport, 'countentertainment': count_entertainment,
                                       'countpolitics': count_politics,
                                       'TotalArticles': count_total_articles})
                    else:
                        return render(request, 'main_pages/login.html')
                else:
                    a="Please Enter Valid Email or Password"
                    return render(request, 'main_pages/login.html')
            else:
                return render(request, 'main_pages/login.html')
        else:
            return render(request,'main_pages/login.html')
def admin_page(request):
    if request.session.has_key('loged'):
        counts = "select count(email) from users "
        cursor.execute(counts)
        row = cursor.fetchone()
        while row:
            counts = str(row[0])
            row = cursor.fetchone()
        admincount = "select count(email) from users where type='Admin'"
        cursor.execute(admincount)
        row = cursor.fetchone()
        while row:
            admincount = str(row[0])
            row = cursor.fetchone()
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            count_sport = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            count_entertainment = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            count_politics = str(row[0])
            row = cursor.fetchone()
        count_total_articles = "select count(name) from article "
        cursor.execute(count_total_articles)
        row = cursor.fetchone()
        while row:
            count_total_articles = str(row[0])
            row = cursor.fetchone()

        return render(request, 'admin_pages/admin.html',
                          {'user_name': request.session['name'], 'user_type': request.session['type'], 'total': counts,
                           'admincount': admincount,
                           'countsport': count_sport, 'countentertainment': count_entertainment,
                           'countpolitics': count_politics,
                           'TotalArticles': count_total_articles})
    else:
        return render(request, 'main_pages/login.html')
def admin_profile(request):
    if request.session.has_key('loged'):
        return render(request, 'admin_pages/profile.html', {'user_name': request.session['name'],'user_type':request.session['type'],'user_email':request.session['email']})
    else:
        return render(request, 'main_pages/login.html')
def allusers(request):
    if request.session.has_key('loged'):
        user="select * from users"
        cursor.execute(user)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return render(request, 'admin_pages/all_users.html', {'user1': [nt_result(*row) for row in cursor.fetchall()], 'user_name': request.session['name'],'user_type':request.session['type']})
    else:
        return render(request, 'main_pages/login.html')
def register_admin(request):
    if request.session.has_key('loged'):
        if id:
            return render(request, 'admin_pages/register_admin.html', {'user_name': request.session['name'],'user_type':request.session['type']})
        else:
            print("not found")
    else:
        return render(request, 'main_pages/login.html')
def registration_admin(request):
    if request.session.has_key('loged'):
        names = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        type = 'Admin'
        sql="insert into users values('"+names+"','"+email+"','"+password+"','"+type+"')"
        cursor.execute(sql)
        conn.commit()
        user = "select * from users"
        cursor.execute(user)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return render(request,'admin_pages/all_users.html',{'user1':[nt_result(*row) for row in cursor.fetchall()],'user_name': request.session['name'],'user_type':request.session['type']})
    else:
        return render(request,'main_pages/login.html')
def operation(request):
    if request.session.has_key('loged'):

            crawler = "select TOP 15 * from crawler order by date desc , time desc "
            cursor.execute(crawler)
            desc = cursor.description
            nt_result = namedtuple('Result', [col[0] for col in desc])
            return render(request, 'admin_pages/operation.html', {'user_name': request.session['name'],'user_type':request.session['type'], 'crawl': [nt_result(*row) for row in cursor.fetchall()]})
    else:
        return render(request, 'main_pages/login.html')
def crawler(request):
    if request.session.has_key('loged'):
        object = Crawler()
        object.crawling()
        print("Preprocessing Start")
        # Performing Preprocessing
        obj3 = CleanData()
        obj3.cleaning()
        print("Predicion of Category Start")
        # Predicting Category
        obj4 = predict()
        obj4.category()
        print("Updating Status")
        email=request.session.get('email')
        date = str(datetime.datetime.now().date())
        time = str(datetime.datetime.now().strftime("%H:%M:%S"))
        sql = "insert into crawler values('" + email + "','" + date + "','" + time + "','" + "Done" + "')"
        cursor=conn.cursor()
        cursor.execute(sql)
        conn.commit()
        obj=connection()
        obj.insert_article_to_db()
        print("Creating Dataset")
        remove = "delete from article where name='Title'"
        cursor = conn.cursor()
        cursor.execute(remove)
        ssql = "with cte(cnt) as(select row_number() over (partition by name order by category) from article) delete from cte where cnt > 1"
        cursor = conn.cursor()
        cursor.execute(ssql)
        conn.commit()
        with io.open(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\recommend\data.txt", "w",
                     encoding="utf-8") as filehandle:
            filehandle.write(("Author,Title,PubDate,Category,Content\n"))
            de = "select * from article order by pubdate desc"
            cursor=conn.cursor()
            cursor.execute(de)
            row=cursor.fetchone()
            while row:
                filehandle.write('%s,' % str(row[2]))
                filehandle.write('%s,' % str(row[1]))
                filehandle.write('%s,' % str(row[3]))
                filehandle.write('%s,' % str(row[4]))
                filehandle.write('%s\n' % str(row[5]))
                row = cursor.fetchone()

        print("Updating Crawler Status")
        crawler = "select TOP 15 * from crawler order by date desc, time desc "
        cursor.execute(crawler)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return render(request, 'admin_pages/operation.html',
                      {'user_name': request.session['name'], 'user_type': request.session['type'],
                       'crawl': [nt_result(*row) for row in cursor.fetchall()]})
    else:
        return render(request,'main_pages/login.html')
def article(request):
    if request.session.has_key('loged'):
        email=request.session['email']
        object.select_query(email)
        count_sport = "select count(name) from article where category='Sports'"
        cursor=conn.cursor()
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            Sports_count = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            Entertainment_count = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            Politics_count = str(row[0])
            row = cursor.fetchone()
        sql="select * from history where email='"+email+"'"
        cursor.execute(sql)
        row=cursor.fetchone()
        if row:
            print(row)
            obj = MyClass()
            auth, title, pubdate, cate, cont = obj.result()
        else:
            auth, title, pubdate, cate, cont =[],[],[],[],[]



        au="select DISTINCT author from article"
        cursor.execute(au)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return render(request, 'admin_pages/articles.html',
                          { 'data':zip(auth,title,pubdate,cate,cont),'user_name': request.session['name'],'user_type':request.session['type'], 'sports': Sports_count,
                           'entertain': Entertainment_count, 'poli': Politics_count,'auth': [nt_result(*row) for row in cursor.fetchall()]})

    else:
        return render(request, 'main_pages/login.html')
def search_article(request):
    if request.session.has_key('loged'):
        count_sport = "select count(name) from article where category='Sports'"
        cursor=conn.cursor()
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            Sports_count = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            Entertainment_count = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            Politics_count = str(row[0])
            row = cursor.fetchone()
        col = request.POST['dropdown']
        if col=="Entertainment":

            print(request.POST['dropdown'])
            search=request.POST['search']
            print(request.POST['search'])
            cat="select TOP 10 * from article where category='"+search+"' order by pubdate desc"
            cursor.execute(cat)
            desc = cursor.description
            nt_result = namedtuple('Result', [col[0] for col in desc])
            row=cursor.fetchall()
            au = "select DISTINCT author from article"
            cursor.execute(au)
            desc1 = cursor.description
            nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
            return render(request, 'admin_pages/search_article.html',
                          {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                           'user_type': request.session['type'], 'sports': Sports_count,
                           'entertain': Entertainment_count, 'poli': Politics_count,'auth': [nt_result1(*row) for row in cursor.fetchall()]})
        if col=="Author":
            print(request.POST['dropdown'])
            search = request.POST['search']
            print(request.POST['search'])
            email = request.session['email']
            aut="select * from article where author='"+search+"'"
            cursor=conn.cursor()
            cursor.execute(aut)
            row=cursor.fetchone()
            while row:
                print(email,str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]))
                insert="insert into history values ('"+email+"','"+str(row[1])+"','"+str(row[2])+"','"+str(row[3])+"','"+str(row[4])+"','"+str(row[5])+"')"
                conn1=object.connection_to_database()
                cursor1=conn1.cursor()
                cursor1.execute(insert)
                cursor1.commit()
                row=cursor.fetchone()
            cat = "select TOP 10 * from article where author='" + search + "'order by pubdate desc"
            cursor.execute(cat)
            desc = cursor.description
            nt_result = namedtuple('Result', [col[0] for col in desc])
            row = cursor.fetchall()
            au = "select DISTINCT author from article"
            cursor.execute(au)
            desc1 = cursor.description
            nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
            return render(request, 'admin_pages/search_article.html',
                          {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                           'user_type': request.session['type'], 'sports': Sports_count,
                           'entertain': Entertainment_count, 'poli': Politics_count,
                           'auth': [nt_result1(*row) for row in cursor.fetchall()]})
        if col=="Title":
            print(request.POST['dropdown'])
            search = request.POST['search']
            print(request.POST['search'])
            email = request.session['email']
            aut = "select * from article where name='" + search + "'"
            cursor = conn.cursor()
            cursor.execute(aut)
            row = cursor.fetchone()
            while row:
                print(email, str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))
                insert = "insert into history values ('" + email + "','" + str(row[1]) + "','" + str(
                    row[2]) + "','" + str(row[3]) + "','" + str(row[4]) + "','" + str(row[5]) + "')"
                conn1 = object.connection_to_database()
                cursor1 = conn1.cursor()
                cursor1.execute(insert)
                cursor1.commit()
                row = cursor.fetchone()
            cat = "select TOP 10 * from article where name='" + search + "'order by pubdate desc"
            cursor.execute(cat)
            desc = cursor.description
            nt_result = namedtuple('Result', [col[0] for col in desc])
            row = cursor.fetchall()
            au = "select DISTINCT author from article"
            cursor.execute(au)
            desc1 = cursor.description
            nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
            return render(request, 'admin_pages/search_article.html',
                          {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                           'user_type': request.session['type'], 'sports': Sports_count,
                           'entertain': Entertainment_count, 'poli': Politics_count,
                           'auth': [nt_result1(*row) for row in cursor.fetchall()]})
        if col=="content":
            print(request.POST['dropdown'])
            search = request.POST['search']
            print(request.POST['search'])
            obj=predict()
            cat=obj.cont_cat(search)
            with io.open(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\recommend\cont.txt", "w", encoding="utf-8") as filehandle:
                filehandle.write(("content,category\n"))
                token = word_tokenize(search)
                content = [word for word in token if not word in new_stopwords_list]
                text = TreebankWordDetokenizer().detokenize(content)
                filehandle.write('%s,' % search)
                filehandle.write('%s\n' % cat)
            obj = recommend()
            cont, cat = obj.category()
            Author = []
            Title = []
            datesss = []
            category = []
            content = []
            for i in cont:
                #number=0
                cont1 = str(i)

                #cat1 = str(cat[0])
                cont1 = cont1.replace("[", '')
                cont1 = cont1.replace("]", '')
                cont1 = cont1.replace("'", '')
                #print(cont1)
                j="select * from article where content LIKE '"+cont1+"';"
                cursor=conn.cursor()
                cursor.execute(j)
                row=cursor.fetchone()
                print("Query Executed")
                while row:
                    print("fetching data")
                    Title.append(str(row[1]))
                    Author.append(str(row[2]))
                    datesss.append(str(row[3]))
                    category.append(str(row[4]))
                    content.append(str(row[5]))
                    row = cursor.fetchone()
            au = "select DISTINCT author from article"
            cursor = conn.cursor()
            cursor.execute(au)
            desc1 = cursor.description
            nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
            return render(request, 'admin_pages/admin_search_topic.html',
                          {'re_ar':cont,'re_cat':cat,'data': zip(Title,Author,datesss,category,content), 'user_name': request.session['name'],
                           'user_type': request.session['type'], 'sports': Sports_count,
                           'entertain': Entertainment_count, 'poli': Politics_count,
                           'auth': [nt_result1(*row) for row in cursor.fetchall()]})
    else:
        return render(request, 'main_pages/login.html')
def search_article_date(request):
    count_sport = "select count(name) from article where category='Sports'"
    cursor.execute(count_sport)
    row = cursor.fetchone()
    while row:
        Sports_count = str(row[0])
        row = cursor.fetchone()
    count_entertainment = "select count(name) from article where category='Entertainment'"
    cursor.execute(count_entertainment)
    row = cursor.fetchone()
    while row:
        Entertainment_count = str(row[0])
        row = cursor.fetchone()
    count_politics = "select count(name) from article where category='Politics'"
    cursor.execute(count_politics)
    row = cursor.fetchone()
    while row:
        Politics_count = str(row[0])
        row = cursor.fetchone()
    search = request.POST['search']
    print(request.POST['search'])
    cat = "select * from article where pubdate='" + search + "'order by pubdate desc"
    cursor.execute(cat)
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    row = cursor.fetchall()
    au = "select DISTINCT author from article"
    cursor.execute(au)
    desc1 = cursor.description
    nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
    return render(request, 'admin_pages/search_article.html',
                  {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                   'user_type': request.session['type'], 'sports': Sports_count,
                   'entertain': Entertainment_count, 'poli': Politics_count,
                   'auth': [nt_result1(*row) for row in cursor.fetchall()]})
def search_article_Ent(request):
    if request.session.has_key('loged'):
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            Sports_count = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            Entertainment_count = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            Politics_count = str(row[0])
            row = cursor.fetchone()

        cat = "select * from article where category='Entertainment' order by pubdate desc"
        cursor.execute(cat)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        row = cursor.fetchall()
        au = "select DISTINCT author from article"
        cursor.execute(au)
        desc1 = cursor.description
        nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
        return render(request, 'admin_pages/search_article.html',
                      {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                       'user_type': request.session['type'], 'sports': Sports_count,
                       'entertain': Entertainment_count, 'poli': Politics_count,
                       'auth': [nt_result1(*row) for row in cursor.fetchall()]})
    else:
        return render(request,'main_pages/login.html')
def search_article_Pol(request):
    if request.session.has_key('loged'):
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            Sports_count = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            Entertainment_count = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            Politics_count = str(row[0])
            row = cursor.fetchone()
        cat = "select * from article where category='Politics' order by pubdate desc"
        cursor.execute(cat)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        row = cursor.fetchall()
        au = "select DISTINCT author from article"
        cursor.execute(au)
        desc1 = cursor.description
        nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
        return render(request, 'admin_pages/search_article.html',
                      {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                       'user_type': request.session['type'], 'sports': Sports_count,
                       'entertain': Entertainment_count, 'poli': Politics_count,
                       'auth': [nt_result1(*row) for row in cursor.fetchall()]})
    else:
        return render(request, 'main_pages/login.html')
def search_article_Sport(request):
    if request.session.has_key('loged'):
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            Sports_count = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            Entertainment_count = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            Politics_count = str(row[0])
            row = cursor.fetchone()
        cat = "select * from article where category='Sports' order by pubdate desc"
        cursor.execute(cat)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        row = cursor.fetchall()
        au = "select DISTINCT author from article"
        cursor.execute(au)
        desc1 = cursor.description
        nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
        return render(request, 'admin_pages/search_article.html',
                      {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                       'user_type': request.session['type'], 'sports': Sports_count,
                       'entertain': Entertainment_count, 'poli': Politics_count,
                       'auth': [nt_result1(*row) for row in cursor.fetchall()]})
    else:
        return render(request, 'main_pages/login.html')
#User Functions
def users(request):
    if request.session.has_key('loged'):
        sql="select count(name) from article where category='Sports'"
        cursor.execute(sql)
        row=cursor.fetchone()
        while row:
            count_sport=str(row[0])
            row = cursor.fetchone()
        sql1 = "select count(category) from article where category='Entertainment'"
        cursor.execute(sql1)
        row = cursor.fetchone()
        while row:
            count_entertainment = str(row[0])
            row = cursor.fetchone()
        sql2 = "select count(category) from article where category='Politics'"
        cursor.execute(sql2)
        row = cursor.fetchone()
        while row:
            count_politics = str(row[0])
            row = cursor.fetchone()
        sql3 = "select count(category) from article"
        cursor.execute(sql3)
        row = cursor.fetchone()
        while row:
            count_total_articles = str(row[0])
            row = cursor.fetchone()
        return render(request, 'user_pages/user.html', {'user_name': request.session['name'],'user_type':request.session['type'], 'countsport': count_sport,
                                                      'countentertainment': count_entertainment,
                                                      'countpolitics': count_politics,
                                                      'TotalArticles': count_total_articles})
    else:
        return render(request,'main_pages/login.html')
def User_Profile(request):
    if request.session.has_key('loged'):
        return render(request, 'user_pages/user_profile.html',
                      {'user_name': request.session['name'], 'user_type': request.session['type'],
                       'user_email': request.session['email']})
    else:
        return render(request, 'main_pages/login.html')
def articles_user(request):
    if request.session.has_key('loged'):
        cursor = conn.cursor()
        email=request.session['email']
        sql = "select * from history where email='" + email + "'"
        cursor.execute(sql)
        row = cursor.fetchone()
        if row:
            print(row)
            object.select_query(email)
            obj = MyClass()
            auth, title, pubdate, cate, cont = obj.result()
        else:
            auth, title, pubdate, cate, cont = [], [], [], [], []

        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            Sports_count = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            Entertainment_count = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            Politics_count = str(row[0])
            row = cursor.fetchone()
        au = "select DISTINCT author from article"
        cursor.execute(au)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return render(request, 'user_pages/user_articles.html',
                      {'data':zip(auth,title,pubdate,cate,cont),'user_name': request.session['name'], 'user_type': request.session['type'],
                       'sports': Sports_count,
                       'entertain': Entertainment_count, 'poli': Politics_count,
                       'auth': [nt_result(*row) for row in cursor.fetchall()]})

    else:
        return render(request, 'main_pages/login.html')
def searcharticle1(request):
    if request.session.has_key('loged'):
        count_sport = "select count(name) from article where category='Sports'"
        cursor = conn.cursor()
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            Sports_count = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            Entertainment_count = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            Politics_count = str(row[0])
            row = cursor.fetchone()
        col = request.POST['dropdown']
        if col == "Entertainment":
            print(request.POST['dropdown'])
            search = request.POST['search']
            print(request.POST['search'])
            cat = "select TOP 10 * from article where category='" + search + "' order by pubdate desc"
            cursor.execute(cat)
            desc = cursor.description
            nt_result = namedtuple('Result', [col[0] for col in desc])
            row = cursor.fetchall()
            au = "select DISTINCT author from article"
            cursor.execute(au)
            desc1 = cursor.description
            nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
            return render(request, 'user_pages/search_article.html',
                          {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                           'user_type': request.session['type'], 'sports': Sports_count,
                           'entertain': Entertainment_count, 'poli': Politics_count,
                           'auth': [nt_result1(*row) for row in cursor.fetchall()]})
        if col == "Author":
            print(request.POST['dropdown'])
            search = request.POST['search']
            print(request.POST['search'])
            email = request.session['email']
            aut = "select * from article where author='" + search + "'"
            cursor = conn.cursor()
            cursor.execute(aut)
            row = cursor.fetchone()
            while row:
                print(email, str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))
                insert = "insert into history values ('" + email + "','" + str(row[1]) + "','" + str(
                    row[2]) + "','" + str(row[3]) + "','" + str(row[4]) + "','" + str(row[5]) + "')"
                conn1 = object.connection_to_database()
                cursor1 = conn1.cursor()
                cursor1.execute(insert)
                cursor1.commit()
                row = cursor.fetchone()
            cat = "select TOP 10 * from article where author='" + search + "'order by pubdate desc"
            cursor.execute(cat)
            desc = cursor.description
            nt_result = namedtuple('Result', [col[0] for col in desc])
            row = cursor.fetchall()
            au = "select DISTINCT author from article"
            cursor.execute(au)
            desc1 = cursor.description
            nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
            return render(request, 'user_pages/search_article.html',
                          {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                           'user_type': request.session['type'], 'sports': Sports_count,
                           'entertain': Entertainment_count, 'poli': Politics_count,
                           'auth': [nt_result1(*row) for row in cursor.fetchall()]})
        if col == "Title":
            print(request.POST['dropdown'])
            search = request.POST['search']
            print(request.POST['search'])
            email = request.session['email']
            aut = "select * from article where name='" + search + "'"
            cursor = conn.cursor()
            cursor.execute(aut)
            row = cursor.fetchone()
            while row:
                print(email, str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))
                insert = "insert into history values ('" + email + "','" + str(row[1]) + "','" + str(
                    row[2]) + "','" + str(row[3]) + "','" + str(row[4]) + "','" + str(row[5]) + "')"
                conn1 = object.connection_to_database()
                cursor1 = conn1.cursor()
                cursor1.execute(insert)
                cursor1.commit()
                row = cursor.fetchone()
            cat = "select TOP 10 * from article where name='" + search + "'order by pubdate desc"
            cursor.execute(cat)
            desc = cursor.description
            nt_result = namedtuple('Result', [col[0] for col in desc])
            row = cursor.fetchall()
            au = "select DISTINCT author from article"
            cursor.execute(au)
            desc1 = cursor.description
            nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
            return render(request, 'user_pages/search_article.html',
                          {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                           'user_type': request.session['type'], 'sports': Sports_count,
                           'entertain': Entertainment_count, 'poli': Politics_count,
                           'auth': [nt_result1(*row) for row in cursor.fetchall()]})
        if col == "content":
            print(request.POST['dropdown'])
            search = request.POST['search']
            print(request.POST['search'])
            obj = predict()
            cat = obj.cont_cat(search)
            with io.open(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\recommend\cont.txt", "w",
                         encoding="utf-8") as filehandle:
                filehandle.write(("content,category\n"))
                token = word_tokenize(search)
                content = [word for word in token if not word in new_stopwords_list]
                text = TreebankWordDetokenizer().detokenize(content)
                filehandle.write('%s,' % search)
                filehandle.write('%s\n' % cat)
            obj = recommend()
            cont, cat = obj.category()
            Author = []
            Title = []
            datesss = []
            category = []
            content = []
            for i in cont:
                # number=0
                cont1 = str(i)

                # cat1 = str(cat[0])
                cont1 = cont1.replace("[", '')
                cont1 = cont1.replace("]", '')
                cont1 = cont1.replace("'", '')
                # print(cont1)
                j = "select * from article where content LIKE '" + cont1 + "';"
                cursor = conn.cursor()
                cursor.execute(j)
                row = cursor.fetchone()
                print("Query Executed")
                while row:
                    print("fetching data")
                    Title.append(str(row[1]))
                    Author.append(str(row[2]))
                    datesss.append(str(row[3]))
                    category.append(str(row[4]))
                    content.append(str(row[5]))
                    row = cursor.fetchone()
            au = "select DISTINCT author from article"
            cursor = conn.cursor()
            cursor.execute(au)
            desc1 = cursor.description
            nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
            return render(request, 'user_pages/user_search_topic.html',
                          {'re_ar': cont, 're_cat': cat, 'data': zip(Title, Author, datesss, category, content),
                           'user_name': request.session['name'],
                           'user_type': request.session['type'], 'sports': Sports_count,
                           'entertain': Entertainment_count, 'poli': Politics_count,
                           'auth': [nt_result1(*row) for row in cursor.fetchall()]})
    else:
        return render(request, 'main_pages/login.html')
def search_article_date1(request):
    count_sport = "select count(name) from article where category='Sports'"
    cursor.execute(count_sport)
    row = cursor.fetchone()
    while row:
        Sports_count = str(row[0])
        row = cursor.fetchone()
    count_entertainment = "select count(name) from article where category='Entertainment'"
    cursor.execute(count_entertainment)
    row = cursor.fetchone()
    while row:
        Entertainment_count = str(row[0])
        row = cursor.fetchone()
    count_politics = "select count(name) from article where category='Politics'"
    cursor.execute(count_politics)
    row = cursor.fetchone()
    while row:
        Politics_count = str(row[0])
        row = cursor.fetchone()
    search = request.POST['search']
    print(request.POST['search'])
    cat = "select * from article where pubdate='" + search + "'order by pubdate desc"
    cursor.execute(cat)
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    row = cursor.fetchall()
    au = "select DISTINCT author from article"
    cursor.execute(au)
    desc1 = cursor.description
    nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
    return render(request, 'user_pages/search_article.html',
                  {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                   'user_type': request.session['type'], 'sports': Sports_count,
                   'entertain': Entertainment_count, 'poli': Politics_count,
                   'auth': [nt_result1(*row) for row in cursor.fetchall()]})
def search_article_Ent1(request):
    if request.session.has_key('loged'):
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            Sports_count = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            Entertainment_count = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            Politics_count = str(row[0])
            row = cursor.fetchone()

        cat = "select * from article where category='Entertainment' order by pubdate desc"
        cursor.execute(cat)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        row = cursor.fetchall()
        au = "select DISTINCT author from article"
        cursor.execute(au)
        desc1 = cursor.description
        nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
        return render(request, 'user_pages/search_article.html',
                      {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                       'user_type': request.session['type'], 'sports': Sports_count,
                       'entertain': Entertainment_count, 'poli': Politics_count,
                       'auth': [nt_result1(*row) for row in cursor.fetchall()]})
    else:
        return render(request,'main_pages/login.html')
def search_article_Pol1(request):
    if request.session.has_key('loged'):
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            Sports_count = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            Entertainment_count = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            Politics_count = str(row[0])
            row = cursor.fetchone()
        cat = "select * from article where category='Politics' order by pubdate desc"
        cursor.execute(cat)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        row = cursor.fetchall()
        au = "select DISTINCT author from article"
        cursor.execute(au)
        desc1 = cursor.description
        nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
        return render(request, 'user_pages/search_article.html',
                      {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                       'user_type': request.session['type'], 'sports': Sports_count,
                       'entertain': Entertainment_count, 'poli': Politics_count,
                       'auth': [nt_result1(*row) for row in cursor.fetchall()]})
    else:
        return render(request, 'main_pages/login.html')
def search_article_Sport1(request):
    if request.session.has_key('loged'):
        count_sport = "select count(name) from article where category='Sports'"
        cursor.execute(count_sport)
        row = cursor.fetchone()
        while row:
            Sports_count = str(row[0])
            row = cursor.fetchone()
        count_entertainment = "select count(name) from article where category='Entertainment'"
        cursor.execute(count_entertainment)
        row = cursor.fetchone()
        while row:
            Entertainment_count = str(row[0])
            row = cursor.fetchone()
        count_politics = "select count(name) from article where category='Politics'"
        cursor.execute(count_politics)
        row = cursor.fetchone()
        while row:
            Politics_count = str(row[0])
            row = cursor.fetchone()
        cat = "select * from article where category='Sports' order by pubdate desc"
        cursor.execute(cat)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        row = cursor.fetchall()
        au = "select DISTINCT author from article"
        cursor.execute(au)
        desc1 = cursor.description
        nt_result1 = namedtuple('Result1', [col[0] for col in desc1])
        return render(request, 'user_pages/search_article.html',
                      {'data': [nt_result(*row) for row in row], 'user_name': request.session['name'],
                       'user_type': request.session['type'], 'sports': Sports_count,
                       'entertain': Entertainment_count, 'poli': Politics_count,
                       'auth': [nt_result1(*row) for row in cursor.fetchall()]})
    else:
        return render(request, 'main_pages/login.html')
#Common Functions
def logout(request):
    print("logout &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    if request.session.has_key('loged'):
        del request.session['loged']
        del request.session['name']
        del request.session['type']
        del request.session['email']
        return render(request, 'main_pages/login.html')