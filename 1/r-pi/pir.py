from gpiozero import MotionSensor, Buzzer
from time import sleep

pir = MotionSensor(4)
buz = Buzzer(17)

""" 
Meter el PIR dentro de un basito desechable para realizar pruebas pues es muy sensible. Tambien mover los
potenciometros puede ayudar con el ajuste de la sensibilidad
"""

while True:
    """ - 1 - 
    print(pir.motion_detected)
    """
    pir.wait_for_motion()  # Luego probar con: wait_for_no_motion()
    print("Motion detected!")
    sleep(1)

""" 
An algorithm for an alarm

Rather than stepping through the next edits to your code, I am going to lay out an algorithm for you in plain English. I would like you to take these steps and convert them into a Python program inside the while loop you already have.
* Wait until motion is detected
* Turn on the buzzer
* Wait for five seconds
* Turn off the buzzer
* Wait for no motion

If you need a reminder of how to use the buzzer, you can check the documentation or look back at week one of this course.
"""


