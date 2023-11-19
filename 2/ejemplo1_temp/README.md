# Arduino Nano en Platformio

![Arduino-Nano](https://docs.arduino.cc/static/bfd8d45fe6dfd1bdf76735464ef75ab0/a6d36/Nano33_ble_sense.png)

* **Nano 33 BLE Sense Cheat Sheet** [[link]](https://docs.arduino.cc/tutorials/nano-33-ble-sense/cheat-sheet())


![pinout](https://docs.arduino.cc/static/c18e027f826663ba9f16ffd94b60500f/a6d36/pinout.png)


Camara: https://openmv.io/


## Ejemplo 1

Vamos a implementar el ejemplo **Reading Temperature & Humidity on Nano 33 BLE Sense** ([link](https://docs.arduino.cc/tutorials/nano-33-ble-sense/humidity-and-temperature-sensor)) en Platformio.

![temperatura](https://docs.arduino.cc/static/19335a6e6e521e84d1ca10dadbc89089/a6d36/nano33BS_01_temp_sensor.png)



```ini
[env:nano33ble]
platform = nordicnrf52
board = nano33ble
framework = arduino
lib_deps = arduino-libraries/Arduino_HTS221@^1.0.0
```

Se dio un momento en el cual no se detectaba la tarjeta. La solución se encontro a continuación en el siguiente foro ([link](https://forum.arduino.cc/t/arduino-nano-33-ble-is-not-recognized-by-computer/640776/3)), mas espeficicamente la siguiente entrada:

> Try this:
>
> 1. Plug the USB cable of your Nano 33 BLE board into your computer.
> 2. Press and release the reset button twice quickly.
>
>After doing that, does the "L" LED start pulsing?


* **Nota**: El ensayo fracaso, parece que este el sensor de temperatura y humedad no viene con la tarjeta del kit ([link](https://forum.arduino.cc/t/cant-initialize-onboard-temperature-sensor/1014660/18))


## Ejemplo 2

## Referencias

* https://github.com/Harvard-CS249R-Fall2020/assignments/tree/master/hello_world
* https://github.com/Harvard-CS249R-Fall2020/assignments/tree/master/person_detection
* https://github.com/Harvard-CS249R-Fall2020/assignments/blob/master/wake_words/README.md#deploying-a-speech-model-to-the-microcontroller-using-vscode--platformio
* https://github.com/Harvard-CS249R-Fall2020/assignments/blob/master/wake_words/README.md
* https://docs.platformio.org/en/latest/boards/nordicnrf52/nano33ble.html
* https://sensiml.com/documentation/firmware/arduino-nano33/arduino-nano33.html
* https://kevinxli.medium.com/manage-two-arduinos-with-ease-using-platformio-4f83ad4a8868
* https://www.digikey.be/en/maker/tutorials/2022/platformio-advanced-features-for-code-debugging-and-version-control
* https://edgeimpulse.com/blog/platformio
* https://github.com/PacktPublishing/TinyML-Cookbook/blob/main/Chapter03/ArduinoSketches
* https://docs.arduino.cc/hardware/nano-33-ble-sense
* https://docs.arduino.cc/tutorials/nano-33-ble-sense/cheat-sheet
* https://docs.arduino.cc/tutorials/nano-33-ble-sense/getting-started-omv
* https://docs.arduino.cc/tutorials/nano-33-ble-sense/community-projects
* https://docs.arduino.cc/tutorials/nano-33-ble-sense-rev2/community-projects
* https://docs.arduino.cc/tutorials/nano-33-ble-sense/ble-device-to-device
* https://docs.arduino.cc/tutorials/nano-33-ble-sense/humidity-and-temperature-sensor
* https://github.com/sandeepmistry/Arduino-Nano-33-BLE-Sense-Examples/tree/master

