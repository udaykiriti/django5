# Generated by Django 3.2.4 on 2022-01-14 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='movies')),
                ('banner', models.ImageField(upload_to='movies_banner')),
                ('category', models.CharField(choices=[('action', 'ACTION'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE')], max_length=10)),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('german', 'GERMAN')], max_length=10)),
                ('status', models.CharField(choices=[('RA', 'RECRNTLY ADDED'), ('MW', 'MOST WATCHED'), ('TR', 'TOP RATED')], max_length=2)),
                ('cast', models.CharField(max_length=100)),
                ('year_of_producation', models.DateField()),
                ('views_count', models.IntegerField(default=0)),
                ('movie_trailer', models.URLField()),
                ('created', models.DateTimeField(default=datetime.datetime(2022, 1, 14, 17, 48, 21, 987895))),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]