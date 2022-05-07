import requests as req

OWN_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = '7ab38b799cbe1e340b828fab2486793b'


weather_params = {
    'lat': '-9.665220',
    'lon': '-35.735710',
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

res = req.get(OWN_Endpoint, params=weather_params)

res.raise_for_status()
weather_data = res.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print('It will rain!')

# print(weather_data['hourly'][0]['weather'][0]['description'])
