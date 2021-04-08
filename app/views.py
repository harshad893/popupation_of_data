from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length

def display_topic(request):
    #topics=Topic.objects.all()
    topics=Topic.objects.filter(topic_name='Cricket')
    return render(request,'display_topic.html',context={'topics':topics})

def display_webpage(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(topic_name='swimming')
    #webpages=Webpage.objects.exclude(topic_name='swimming')
    #webpages=Webpage.objects.all()[0:6]
    #webpages=Webpage.objects.all().order_by('name')
    #webpages=Webpage.objects.all().order_by('-name')
    #webpages=Webpage.objects.all().order_by(Length('name'))
    webpages=Webpage.objects.all().order_by(Length('name').desc())
    webpages=Webpage.objects.filter(url__startswith='http:')
    webpages=Webpage.objects.filter(url__endswith='.com')
    webpages=Webpage.objects.filter(name__icontains='h')
    d={'webpages':webpages}
    return render(request,'display_webpage.html',context=d)

def display_access(request):
    access=Access_Records.objects.all()
    d={'access':access}
    return render(request,'display_access.html',d)