#import subprocess
#subprocess.call('sudo python3 /home/pi/badge/led-badge-11x44.py "Hello World!"', shell=False)
import time
import os

os.system('sudo python3 /home/pi/badge/led-badge-11x44.py "Hello World!"')
time.sleep(4)
os.system('sudo python3 /home/pi/badge/led-badge-11x44.py "2"')