#create a Django environment
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project4.settings')

#accessing the features of django
import django
django.setup()

from app.models import *
import random
from faker import Faker
f=Faker()
topics=['Hockey','Kabaddi','Tennis','swimming']

def add_topic():
    topic_name=random.choice(topics)
    t=Topic.objects.get_or_create(topic_name=topic_name)[0]
    t.save()
    return t

def add_webpage(webpagename,url):
    t=add_topic()
    w=Webpage.objects.get_or_create(topic_name=t,name=webpagename,url=url)[0]
    w.save()
    return w

def add_records(webpagename,url,date):
    name=add_webpage(webpagename,url)
    a=Access_Records.objects.get_or_create(name=name,date=date)[0]
    a.save()



def add_data(n):
    for i in range(n):
        fake_name=f.first_name()
        fake_url=f.url()
        fake_date=f.date()

        add_records(fake_name,fake_url,fake_date)

if __name__=='__main__':

    n=int(input('enter n value'))#5
    print('population is starting')
    add_data(n)
    print('population is done successfully')






















