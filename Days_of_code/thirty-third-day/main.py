import requests as req
from datetime import datetime

MY_LAT = -9.648139
MY_LONG = -35.717239

# res = req.get(url="http://api.open-notify.org/iss-now.json")

# res.raise_for_status()

# data = res.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)


def is_iss_overhead():
    res = req.get('https://api.sunrise-sunset.org/json', params=paramenters)
    res.raise_for_status()
    data = res.json()
    time_now = datetime.now()

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


paramenters = {
    'Lat': MY_LAT,
    'Lng': MY_LONG,
    'formatted': 0
}
