from django.shortcuts import render, HttpResponse
import json
import requests
# Create your views here.


def weather(request):
    if request.method == 'POST':
        city = request.POST['city']    
        source ="https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid=a0b657ad1b0c9ce2939381885f337261"
        list_of_data = requests.get(source.format(city)).json

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['long']) + ' ' + str(list_of_data['coord']['long']),
            "temperature" : int((int(list_of_data["main"]["temp"]) - 32) * 5.0/9.0,2),
            "description" : str(list_of_data["weather"][0]["description"]),
            "humidity" : float(str(list_of_data["main"]["humidity"]))
        }

    else:
        data = {}
    return render(request, "weather.html", data)