import requests



def get_weather_data(city):
    api = '435528714a1028118e4c030dc06fa681'
    city = 'khulna'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
    response = requests.get(url)
    data = response.json()
    print(f" Weather is {data['weather'][0]['main']}")
    print(f" Tempreture is {round(data['main']['temp'] - 273.15, 2)}°C")

inp = input('enter the value').capitalize()
get_weather_data('khulna')



