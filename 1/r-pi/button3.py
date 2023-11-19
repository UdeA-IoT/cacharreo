from gpiozero import Button, LED

btn = Button(4)
led = LED(17)

while True:
    btn.wait_for_press()
    led.on()
    btn.wait_for_release()
    led.off()

