from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout,name='logout'),
    path('login/',views.login,name='login_page'),
    path('register/',views.register,name='register_page'),
    path('Home/',views.loginAuth,name='loginAuth'),
    path('registration/',views.registration,name='registration'),
    path('adminpage/', views.admin_page, name='adminpage'),
    path('adminprofile/', views.admin_profile, name='adminprofile'),
    path('allusers/', views.allusers, name='allusers'),
    path('registerAdmin/', views.register_admin, name='register_admin'),
    path('registration_admin',views.registration_admin,name='registration_admin'),
    path('operation/', views.operation, name='operation'),
    path('crawler/',views.crawler,name='crawler'),
    path('article/', views.article, name='article'),
    path('search_article/',views.search_article,name='search_article'),
    path('search_article_date/', views.search_article_date, name='search_article_date'),
    path('Articles/Entertainment/',views.search_article_Ent,name='search_article_Ent'),
    path('Articles/Politics/', views.search_article_Pol, name='search_article_Pol'),
    path('Articles/Sports/', views.search_article_Sport, name='search_article_Sport'),
    path('users/', views.users, name='users'),
    path('User_Profile/', views.User_Profile, name='User_Profile'),
    path('articles_user/', views.articles_user, name='articles_user'),
    path('searcharticle1/', views.searcharticle1, name='searcharticle1'),
    path('search_article_date_user/', views.search_article_date1, name='search_article_date1'),
    path('Articles/Entertainment_user/', views.search_article_Ent1, name='search_article_Ent1'),
    path('Articles/Politics_user/', views.search_article_Pol1, name='search_article_Pol1'),
    path('Articles/Sports_user/', views.search_article_Sport1, name='search_article_Sport1'),


]
