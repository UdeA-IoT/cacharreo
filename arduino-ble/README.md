# Arduino ble


Tiny Machine Learning Kid ([link](https://store.arduino.cc/products/arduino-tiny-machine-learning-kit)):
- [x] ARDUINO Nano 33 Ble Sense Lite
- [x] Tiny Machine Learning Shield
- [x] OV7605 Camera Module
- [x] USB A - Micro USB Cable (1m)

Documento: **Nano 33 BLE Sense** ([link](https://docs.arduino.cc/hardware/nano-33-ble-sense))

De https://tinyml.seas.upenn.edu/ la sección 3 **Getting Started (C++, SW/HW Setup, Sensors)**

La información del kid se encuentra resumida en: 
1. **Tutorial Hardware Assembly** ([link](Tutorial%20The%20TinyML%20Kit%20(Hardware%20Assembly)-1.pdf)))
2. **Tutorial Software Assembly** ([link](Tutorial%20Software%20Assembly.pdf))
3. **Tutorial Step by Step**([link](Tutorial%20Step%20by%20step%20-1.pdf))


![pines_arduino_ble](https://content.arduino.cc/assets/NANO-33-BLE-Sense_sensor-indentification.png)
https://docs.arduino.cc/hardware/nano-33-ble-sense

## Instalación de librerias

Se siguieron los pasos de **Tutorial Software Assembly** ([link](Tutorial%20Software%20Assembly.pdf))

1. Agregar la board (Tools → Board → Boards Manager)
   
   

2. ss


mbed nano

3. sss

4. ss

Open the Library Manager, which you can find via the Tools drop-down menu. Navigate,
as follows: Tools → Manage Libraries

* The Tensorflow Lite Micro Library

Tensorflow

The Tensorflow Lite Micro Library:
Search Term: Tensorflow
Library Name: Arduino_TensorFlowLite
Version: 2.4.0-ALPHA

---

The Tensorflow Lite Micro Library:
Search Term: Tensorflow
Library Name: Hardvard_TinyMLx
Version: 1.2.3-ALPHA

**The library that supports the accelerometer, magnetometer, and gyroscope on the
Nano 33 BLE sense**

Search Term: LSM9DS1
Library Name: Arduino_LSM9DS1
Version: 

Search Term: ArduinoBLE
Library Name: ArduinoBLE
Version: 1.2.1 or newer (tested up to 1.2.2)

Se complemento de aqui:
http://dejazzer.com/eece4710/docs/W62_Setup.pdf


## Primer test

Ver: 
* http://dejazzer.com/eece4710/docs/W62_Setup.pdf
* 


```ino
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);                      // wait for a second
}
```


ss



https://support.arduino.cc/hc/en-us/articles/360016724140-How-to-control-the-RGB-LED-and-Power-LED-of-the-Nano-33-BLE-boards-?queryID=f8337761d7af67e7a4ba29aec63d3949

```ino
// How to control the RGB Led and Power Led of the Nano 33 BLE boards.  

 #define RED 22     
 #define BLUE 24     
 #define GREEN 23
 #define LED_PWR 25

void setup() {

 // initialize the digital Pin as an output
  pinMode(RED, OUTPUT);
  pinMode(BLUE, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(LED_PWR, OUTPUT);

}

// the loop function runs over and over again
void loop() {
  digitalWrite(RED, LOW); // turn the LED off by making the voltage LOW
  delay(1000);            // wait for a second
  digitalWrite(GREEN, LOW);
  delay(1000);  
  digitalWrite(BLUE, LOW);
  delay(1000);  
  digitalWrite(RED, HIGH); // turn the LED on (HIGH is the voltage level)
  delay(1000);                         
  digitalWrite(GREEN, HIGH);
  delay(1000);  
  digitalWrite(BLUE, HIGH);
  delay(1000);  
  digitalWrite(LED_PWR, HIGH);
  delay(1000);  
  digitalWrite(LED_PWR, LOW);
  delay(1000);  
}
```



# Referencias


* https://hackmd.io/@unipd/HkAnHT7b9#13-TinyML-hands-on-examples
* https://tinyml.seas.harvard.edu/courses/
* https://www.datacamp.com/blog/what-is-tinyml-tiny-machine-learning
* https://tinyml.seas.harvard.edu/
* https://machinelearningforkids.co.uk/#!/stories/ml-hasnt-replaced-coding
* http://dejazzer.com/eece4710/index.html#1_intro