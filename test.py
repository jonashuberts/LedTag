"""
usage: led-badge-11x44.py [-h] [-t TYPE] [-s SPEED] [-m MODE] [-b BLINK]
			  [-a ANTS] [-p FILE] [-l]
                          MESSAGE [MESSAGE ...]

Upload messages or graphics to a 44x11 led badge via USB HID.
Version 0.6 from https://github.com/jnweiger/led-badge-44x11
 -- see there for more examples and for updates.

positional arguments:
  MESSAGE               Up to 8 message texts with embedded builtin icons or
                        loaded images within colons(:) -- See -l for a list of
                        builtins

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE
			Type of display: supported values are 12x48 or
			(default) 11x44. Rename the program to led-badge-12x48,
			to switch the default.
  -s SPEED, --speed SPEED
                        Scroll speed (Range 1..8). Up to 8 comma-seperated
                        values
  -m MODE, --mode MODE  Up to 8 mode values: Scroll-left(0) -right(1) -up(2)
                        -down(3); still-centered(4); animation(5); drop-
                        down(6); curtain(7); laser(8); See '--mode-help' for
                        more details.
  -b BLINK, --blink BLINK
                        1: blinking, 0: normal. Up to 8 comma-seperated values
  -a ANTS, --ants ANTS  1: animated border, 0: normal. Up to 8 comma-seperated
                        values
  -l, --list-names      list named icons to be embedded in messages and exit

Example combining image and text:
 sudo ./led-badge-11x44.py "I:HEART2:you"
"""

import time
import os

os.system('sudo python3 /home/pi/badge/led-badge-11x44.py "Hello World!"')
time.sleep(4)
os.system('sudo python3 /home/pi/badge/led-badge-11x44.py "text1:/home/pi/LedTag/images/test.png:text2"')