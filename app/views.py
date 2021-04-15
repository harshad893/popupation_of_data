from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

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
    #webpages=Webpage.objects.all().order_by(Length('name').desc())
    #webpages=Webpage.objects.filter(url__startswith='http:')
    #webpages=Webpage.objects.filter(url__endswith='.com')
    #webpages=Webpage.objects.filter(name__icontains='h')
    webpages=Webpage.objects.filter(Q(topic_name='Tennis') & Q(name='Michael'))
    #webpages=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name='Walter') | Q(url='https://manning.info/'))
    webpages=Webpage.objects.filter(name__in=['Dhoni','Patricia'])
    webpages=Webpage.objects.filter(name__regex=r'^[a-zA-Z]{1}h')
    d={'webpages':webpages}

    return render(request,'display_webpage.html',context=d)

def display_access(request):
    access=Access_Records.objects.all()
    #access=Access_Records.objects.filter(date__gt='1995-11-11')
    #access=Access_Records.objects.filter(date__year='2003')
    #access=Access_Records.objects.filter(date__month='05')
    access=Access_Records.objects.filter(date__day='17')
    
    
    d={'access':access}
    return render(request,'display_access.html',d)



