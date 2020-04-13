import requests
from django.shortcuts import render
from .forms import CityForm

# Create your views here.
def index(request):

    # URl has city name and unit of the temparature 
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4bc2afcae9071b37342570eeb23e1027'
    form = CityForm()
    if request.method =='POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            # this statement puts the city name and returns data
    # r is a dictionary and converting it intojson can store data in key-value pair format
            r = requests.get(url.format(city)).json()
            city_weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            }
            context = {'city_weather':city_weather,'form':form}
    else:
        context = {'form':form}
    #print(city_weather)
    return render(request,'weatherApp/weather.html',context,)
    

    #print all the data
    #print(r.text)
