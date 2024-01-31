import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from bs4 import BeautifulSoup

from webscraperapp.models import Links


# Create your views here.
def home(request):
    if request.method=="POST":
        link_new=request.POST.get('page','')
        urls=requests.get(link_new)
        beautysoup=BeautifulSoup(urls.text,'html.parser')
        # address=[]

        for link in beautysoup.find_all('a'):
            li_address=link.get('href')
            li_name=link.string
            Links.objects.create(address=li_address,string_name=li_name)
        return HttpResponseRedirect('/')
    else:
        data_values=Links.objects.all()
    return render(request,'home.html',{'data_values':data_values})