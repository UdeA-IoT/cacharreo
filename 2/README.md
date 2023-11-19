# Arduino Nano en Platformio

![Arduino-Nano](https://docs.arduino.cc/static/bfd8d45fe6dfd1bdf76735464ef75ab0/a6d36/Nano33_ble_sense.png)

* **Nano 33 BLE Sense Cheat Sheet** [[link]](https://docs.arduino.cc/tutorials/nano-33-ble-sense/cheat-sheet)


![pinout](https://docs.arduino.cc/static/c18e027f826663ba9f16ffd94b60500f/a6d36/pinout.png)


Camara: https://openmv.io/


## Ejemplo 1 - Temperatura

Este ejemplo no dio. La tarjeta al parecer no tiene sensor de temperatura

## Ejemplo 2 - Sensor de proximidad

https://docs.arduino.cc/tutorials/nano-33-ble-sense/proximity-sensor

La solución al problema de la programación del Arduino Nano 33 BLE se encuentra en el siguiente foro: https://community.platformio.org/t/issues-flashing-arduino-nano-33-ble-with-platformio-on-vscode/34458


```ini 
[env:nano33ble]
platform = nordicnrf52@9.5.0
board = nano33ble
framework = arduino
lib_deps = arduino-libraries/Arduino_APDS9960@^1.0.4
```

Codigo:

```ino
#include <Arduino.h>
#include <Arduino_APDS9960.h>

int ledState = LOW;

unsigned long previousMillis = 0;

const long intervalLong = 1000;
const long intervalMed = 500;
const long intervalShort = 100;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!APDS.begin()) {
    Serial.println("Error initializing APDS9960 sensor!");
  }

  // set the LEDs pins as outputs
  pinMode(LEDR, OUTPUT);
  pinMode(LEDG, OUTPUT);
  pinMode(LEDB, OUTPUT);

  // turn all the LEDs off
  digitalWrite(LEDR, HIGH);
  digitalWrite(LEDG, HIGH);
  digitalWrite(LEDB, HIGH);
}

void loop() {
  unsigned long currentMillis = millis();

  // check if a proximity reading is available
  if (APDS.proximityAvailable()) {
    // read the proximity
    // - 0   => close
    // - 255 => far
    // - -1  => error
    int proximity = APDS.readProximity();

    if (proximity > 150) {
      if (currentMillis - previousMillis >= intervalLong) {
        previousMillis = currentMillis;

        // if the LED is off turn it on and vice-versa:
        if (ledState == LOW) {
          ledState = HIGH;
        } else {
          ledState = LOW;
        }

        // set the green LED with the ledState of the variable and turn off the rest
        digitalWrite(LEDG, ledState);
        digitalWrite(LEDR, HIGH);
        digitalWrite(LEDB, HIGH);
      }
    }

    else if(proximity > 50 && proximity <= 150){
      if (currentMillis - previousMillis >= intervalMed) {
        previousMillis = currentMillis;

        // if the LED is off turn it on and vice-versa:
        if (ledState == LOW) {
          ledState = HIGH;
        } else {
          ledState = LOW;
        }

        // set the blue LED with the ledState of the variable and turn off the rest
        digitalWrite(LEDB, ledState);
        digitalWrite(LEDR, HIGH);
        digitalWrite(LEDG, HIGH);
      }
    }

    else {
      if (currentMillis - previousMillis >= intervalShort) {
        previousMillis = currentMillis;

        // if the LED is off turn it on and vice-versa:
        if (ledState == LOW) {
          ledState = HIGH;
        } else {
          ledState = LOW;
        }

        // set the blue LED with the ledState of the variable and turn off the rest
        digitalWrite(LEDR, ledState);
        digitalWrite(LEDB, HIGH);
        digitalWrite(LEDG, HIGH);
      }
    }

    // print value to the Serial Monitor
    Serial.println(proximity);
  }
}
```





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

