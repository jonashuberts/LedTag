import time
import os
from datetime import datetime
import requests
import json

#wetter
api_key = "fdb6287e199be3f245fe9c7166d3c8c8"
lat = "48.035264"
lon = "10.861981"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

response = requests.get(url)
data = json.loads(response.text)
temp = data["current"]["dt"]
print(temp)

#time
minute = datetime.now().minute

while True:
    if minute < datetime.now().minute:
        time = str(datetime.now().strftime('%H:%M %d.%m.%Y'))

        response = requests.get(url)
        data = json.loads(response.text)
        temp = str(data["current"]["dt"])
        
        text = time + " " + temp
        print(text)
        os.system('sudo python3 /home/pi/badge/led-badge-11x44.py -s 6 "%s"' % text)
        minute = datetime.now().minute 
    else:
        pass