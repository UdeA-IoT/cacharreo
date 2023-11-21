""" 
Run in: https://trinket.io/sense-hat
"""

from sense_hat import SenseHat

sense = SenseHat()

temperature = round(sense.temperature, 1)

# sense.show_message("It is " + str(temperature) + " degrees")
if temperature > 25 and temperature < 35:
    sense.show_message("That's quite warm")

elif temperature > 10 and temperature <= 25:
    sense.show_message("Not too cold")

elif temperature > -15 and temperature <= 10:
    sense.show_message("Brr, it's chilly")

elif temperature >= 100:
    sense.show_message("It's boiling")

elif temperature >= 35 or temperature <= -15:
    sense.show_message("The temperature is extreme!")