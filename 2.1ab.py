import requests

city = "Moscow,RU"
appid = "84a94e092a16a9f9b1803fff92599eed"

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

for i in data['list']:
    print(
        "--------------------------------",
        "\r\nДата <", i['dt_txt'],
          "> \r\nТемпература", '{0:+3.0f}'.format(i['main']['temp']),"°C",
          "> \r\nПогодные условия", i['weather'][0]['description'],
          "> \r\nСкорость ветра", i['wind']['speed'],
          "> \r\nВидимость", i['visibility']
          )