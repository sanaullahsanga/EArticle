# Generated by Django 3.0.7 on 2020-06-10 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('authorname', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=60500)),
            ],
        ),
        migrations.CreateModel(
            name='crawler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=1000)),
                ('u_category', models.CharField(max_length=30)),
                ('u_content', models.CharField(max_length=60500)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=5)),
            ],
        ),
    ]
