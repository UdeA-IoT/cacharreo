from gpiozero import LED, Button
from time import sleep

btn = Button(4)
led = LED(17)

while True:
    if btn.is_pressed:
        print("You pressed me")
    sleep(0.1)

"""
Creating a light switch

You have just created a switch that will print a statement when the button is pressed.

Using your experience with LEDs from last week, edit your program so:

The LED is turned on when the button is pressed.
The LED turns back off after five seconds, creating an energy-saving feature.
Share your code in the discussion. Make sure to try it yourself before looking at other learners' solutions. 
You can also share any problems you face, if you need help.
"""