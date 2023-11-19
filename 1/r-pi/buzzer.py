from gpiozero import Buzzer
from time import sleep

buzzer = LED(17)

while True:
    buzzer.on()
    sleep(0.5)
    buzzer.off()
    sleep(1)