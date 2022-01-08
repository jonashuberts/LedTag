import time
import os
from datetime import datetime

minute = datetime.now().minute

while True:
    if minute < datetime.now().minute:
        text = str(datetime.now().strftime('%d.%m.%Y %H:%M'))
        print(text)
        os.system('sudo python3 /home/pi/badge/led-badge-11x44.py "%s"' % text)
        minute = datetime.now().minute 
    else:
        pass