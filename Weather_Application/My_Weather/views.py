from django.shortcuts import render,redirect
from .forms import CityForm
from .models import Weather
import requests
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    return render(request,'home.html')


def weather(request):
    api_key='  Here our API key(i have deleted)'
    url='http://api.openweathermap.org/data/2.5/weather?,&q={},&appid=04a4905d2fb5bcf331e33154a61cade9&units=matric'
    if request.method=="POST":
        form=CityForm(request.POST)
        if form.is_valid():
            ncity=form.cleaned_data['name']
            ccity=Weather.objects.filter(name=ncity).count()
            if ccity==0:
                res=requests.get(url.format(ncity)).json()
                if res['cod']==200:
                    form.save()
                else:
                    pass
            else:
                pass        
    form=CityForm
    cities=Weather.objects.all()
    data=[]
    for city in cities:
        res=requests.get(url.format(city)).json()
        city_weather={
           'city':city,
           'temparature':res['main']['temp'],
           'description': res['weather'][0]['description'],
           'country':res['sys']['country'],
           'icon': res['weather'][0]['icon']
        }
        data.append(city_weather)
    context={'data':data,'form':form}    
    return render(request,'weather.html',context)

def delete(request,cname):
    weather = get_object_or_404(Weather, name=cname)
    weather.delete()
    return redirect('Weather')