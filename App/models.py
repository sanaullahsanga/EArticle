from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=5)

class article(models.Model):
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    authorname=models.CharField(max_length=30)
    date=models.CharField(max_length=15)
    content=models.CharField(max_length=60500)
class history(models.Model):
    u_id=models.CharField(max_length=1000)
    u_category=models.CharField(max_length=30)
    u_content=models.CharField(max_length=60500)
class crawler(models.Model):
    email=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    job=models.CharField(max_length=10)


