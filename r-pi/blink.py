from gpiozero import LED
from time import sleep

red_led = LED(17)

while True:
    red_led.on()
    sleep(1)
    red_led.off()
    sleep(1)


"""
https://gpiozero.readthedocs.io/en/stable/api_output.html#led
"""

"""
Challenge time
Edit the code and add more instructions so that the LED blinks the Morse code for one of the following:
- SOS
- Hello World
"""