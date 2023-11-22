from gpiozero import MotionSensor, Buzzer
from time import sleep

pir = MotionSensor(4)
buz = Buzzer(17)

while True:
    pir.wait_for_motion()
    print("Motion detected")
    sleep(1)
