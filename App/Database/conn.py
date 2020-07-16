import io

import pyodbc
class connection:
    def __int__(self):
        pass
    def connection_to_database(self):
        server = 'earticles.database.windows.net'
        database = 'EArticle'
        username = 'Sanaullah'
        password = 'Admin1234'
        driver = '{ODBC Driver 17 for SQL Server}'
        conn = pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        if conn:
            #print("Connected")
            return conn
    def create_tables(self):
        conn=self.connection_to_database()
        cursor = conn.cursor()
        a="create table users(" \
             "id int primary key not null IDENTITY(1, 1)," \
             "name varchar(40) ," \
             "email varchar(40) unique ," \
             "password varchar(40)," \
             "type varchar(5))"
        articles="create table article(" \
                 "id int primary key not null IDENTITY(1, 1)," \
                 "name varchar(400) ," \
                 "author varchar(400) ," \
                 "pubdate varchar (10)," \
                 "category varchar(15) ," \
                 "content text)"
        history="create table history(" \
                "id int primary key not null IDENTITY(1, 1)," \
                "email varchar(40) FOREIGN KEY REFERENCES users(email), " \
                "name varchar(400) ," \
                "author varchar(400) ," \
                "pubdate date ," \
                "category varchar(15) ," \
                "content text)"
        crawler="create table crawler(" \
                "email varchar(40) ," \
                "date varchar(10) ," \
                "time varchar(10) ," \
                "job varchar(10) )"
        #cursor.execute(a)
        #cursor.execute(articles)
        #cursor.execute(history)
        #cursor.execute(crawler)
        conn.commit()
    def check_user(self):
        art="From Sushant Singh Rajput’s suicide to Deepika Padukone’s"
        abc=art.replace("'s", '')
        #print(abc)
        sql="insert into article values ('"+abc+"','WebDesk','2020-06-13','Entertainment','coronavirus pandemic has meant that movie release dates have been shifted and how Here is a piece of news that is of interest to all fans of Wonder Woman 1984 movies release date has been shifted from August 14 to October 2 2020 This report has got mixed reviews from fans who were eager to watch the second film of the franchise It seems Disneys Mulan will hit the screens on July 24 while Christopher Tenet will be out on July 31 In a report of Associated Press AMC Theaters the worlds largest theater operator said it expects to have atleast 97 per cent of its locations open by midJuly It is being said that 9095 per cent of the cinemas around the world will open then as well Also Read Coronavirus pandemic Even Wonder Woman is helpless release date of Wonder Woman 1984 pushed due to Covid19Gal Gadot wrote on Instagram The new release date for WW84 is October 2 2020 Wow its finally happening and I couldn’t be more excited To all the fans that stuck with us through this time thank you so much We couldnt have done this without you Im so excited for you to get to see it WW84 it will be worth the wait This is how fans reacted Also Read Hollywood Movie Calendar 2020 – From Tenet to Conjuring 3 here are the films we can’t wait to watchVizyona girmesi planlanan filmlerin bazılarından ertelenme haberleri geldiTenet 17 Temmuzdan 31 TemmuzaWonderWoman1984 14 Ağustostan 2 Ekime TheMatrix4 ise 21 Mayıs 2021’den 1 Nisan 2022’ye Ertelendi pictwittercomUXMW4F5PR1 OverGeek OverGeek6 June 13 2020Nooo Another delay I cant wait to see some wonder actionWonderWoman1984 Velislava Stoyanova RAM ramflight June 13 2020Talking about the backdrop of 1980s Patty Jenkins told Syfy I really felt like the 1980s is mankind at their most extreme and at their best It was when we could do anything we wanted and we had no idea of the price yet So we have really committed to that version of the 80s where it’s not needle drops and its not a bunch of jokes Also Read Wonder Woman 1984 trailer Gal Gadot looks invincible in this wonderful throwback to the 80s disco era')"
        sql2="select * from article"
        sql1="insert into users values ('Sanaullah','f168178@gmail.com','Asdf1234','Admin')"
        sql3="delete from users where email='f168178@nu.edu.pk'"
        sql4="delete from article"
        sql5= "select count(name) from article where category='Sports'"
        sql6="select * from article where author='Web Desk' order by pubdate desc "
        remove = "delete from article where name='Title'"
        conn = self.connection_to_database()
        cursor = conn.cursor()
        cursor.execute(remove)
        cursor.execute(sql2)
        row=cursor.fetchone()
        while row:
            print(str(row[0]),str(row[3]),str(row[4]),str(row[2]),str(row[1]),str(row[5]))
            row = cursor.fetchone()
        #cursor.execute(sql4)
        conn.commit()
    def abc(self):
        print("Creating Dataset")
        remove = "delete from article where name='Title'"
        conn = self.connection_to_database()
        cursor = conn.cursor()
        cursor.execute(remove)
        with io.open(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\recommend\data.txt", "w",
                     encoding="utf-8") as filehandle:
            filehandle.write(("Author,Title,PubDate,Category,Content\n"))
            de = "select * from article order by pubdate desc"

            cursor = conn.cursor()
            cursor.execute(de)
            row = cursor.fetchone()
            while row:
                filehandle.write('%s,' % str(row[2]).replace(",",''))
                filehandle.write('%s,' % str(row[1]).replace(",",''))
                filehandle.write('%s,' % str(row[3]).replace(",",''))
                filehandle.write('%s,' % str(row[4]).replace(",",''))
                filehandle.write('%s\n' % str(row[5]).replace(",",''))
                row = cursor.fetchone()
        remove = "delete from article where name='Title'"
        cursor = conn.cursor()
        cursor.execute(remove)
    def remove_duplicate_tuple(self):
        ssql="with cte(cnt) as(select row_number() over (partition by name order by category) from article) delete from cte where cnt > 1"
        sql="delete from history where email='hassan@nu.edu.pk'"
        conn = self.connection_to_database()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    def select_query(self,email):
        conn = self.connection_to_database()
        cursor = conn.cursor()
        ssql="select * from history where email='"+email+"'"
        cursor.execute(ssql)
        row=cursor.fetchone()
        with io.open(r"C:\Users\Sanau\PycharmProjects\FYP_Version_04\model_train\recommend\history.txt", "w",
                     encoding="utf-8") as filehandle:
            filehandle.write(("Author,Title,PubDate,Category,Content\n"))
            while row:
                #print(str(row[3]), str(row[2]), str(row[4]), str(row[5]), str(row[6]))
                filehandle.write('%s,' % str(row[3]).replace(",",''))
                filehandle.write('%s,' % str(row[2]).replace(",",''))
                filehandle.write('%s,' % str(row[4]).replace(",",''))
                filehandle.write('%s,' % str(row[5]).replace(",",''))
                filehandle.write('%s\n' % str(row[6]).replace(",",''))
                row = cursor.fetchone()

#object=connection()
#object.connection_to_database()
#object.create_tables()
#object.check_user()
#object.abc()
#object.remove_duplicate_tuple()
#object.select_query("f168288@nu.edu.pk")