"""
The reflexes game
In this game, an LED will turn on after a random amount of time, and the player will then have to push a button 
as quickly as possible. The game will record the time between the LED switching on and the button being pressed, 
and then display this reaction time on the screen.    
"""

# import the classes and function
from gpiozero import Button, LED
from time import time, sleep
from random import randint

# Create LED and Button objects
led = LED(17)
btn = Button(4)

"""
# It's always a good idea to test your wiring, so add a little bit of code to make sure it's all working as it should.
led.on()
btn.wait_for_press()
led.off()
"""

while True:
    sleep(randint(1,10))
    led.on()
    start = time()
    btn.wait_for_press()
    end = time()
    led.off()
    print(end - start)



while True:
    btn.wait_for_press()
    led.on()
    btn.wait_for_release()
    led.off()

