import time
import os
from datetime import datetime as dt
minute = dt.now().minute
while true:
    if minute > dt.now().minute:
        os.system('sudo python3 /home/pi/badge/led-badge-11x44.py "%s"' % minute)
    else:
       minute = dt.now().minute 