from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib import messages
import requests
import datetime


# Create your views here.


def home(request):
    if request.method == 'POST':
        city = request.POST.get('city', 'chennai')
    else:
        city = 'chennai'

    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6a8b01b69ddaadcb460b4bfb6858eb3c'
    weather_params = {'units': 'metric'}

    try:
        weather_response = requests.get(weather_url, params=weather_params)
        weather_data = weather_response.json()

        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temperature = weather_data['main']['temp']
        day = datetime.date.today()

    except:
        messages.error(request, 'Entered city is not available. Showing default data for Chennai.')
        description = 'clear sky'
        icon = '01d'
        temperature = '25'
        city = 'chennai'
        day = datetime.date.today()


    return render(request, 'weatherapp/index.html', {
        'description': description,
        'icon': icon,
        'temp': temperature,
        'day': day,
        'city': city,
    })



