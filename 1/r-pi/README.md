# Rpi

## Sensing the world around you

## Physical properties
The physical world is full of measurable properties that you may want to detect and react to inside your programs. Some of the 
best uses for physical computing involve sensing the environment to produce a useful output automatically; think of a greenhouse that knows when to water your plants, for example.

The next section will describe some of the other sensors you can use and the properties they measure.

### Individual components

A **light dependent resistor**, or photocell, is a component whose resistance changes depending on the intensity of the light shining on it and can thus be used to detect changes in light. They are commonly used in street lighting, so that a light will turn on when it gets dark at night and turn off when it gets light in the morning.


An **air quality sensor** is used to determine air quality by detecting various gases, aerosols, and particulates (such as those in smoke or ash). The devices comprise a heater and an electrochemical sensor. The heater is used to bring the device up to the operational temperature at which the gases and particles can be detected. The output of the sensor is an analogue voltage that goes up and down according to how contaminated the air is. The more contaminants, the lower the potential difference across the sensor.

### Sense HAT

The Sense HAT board was designed especially for Raspberry Pi as part of the [Astro Pi](https://astro-pi.org/) education programme. There are two on board the International Space Station that can be programmed by competition winners from across European Space Agency member states. The Sense HAT has the following sensors:
* A gyroscope measures and detects changes in the orientation of an object. This is measured as three values, normally called pitch (up and down, like a plane taking off and landing), yaw (left and right, like steering a car), and roll (imagine a corkscrew movement, like barrel rolling a fighter jet).
* An **accelerometer** measures an object’s change in speed (acceleration). At rest, it measures the direction and force of gravity, but in motion it also measures the direction and size of its acceleration.
* A **magnetometer** is used to measure the strength and direction of a magnetic field. They're most often used to measure the Earth’s magnetic field in order to find the direction of north. If your phone or tablet has a compass, it will probably be using a magnetometer. They are also used to detect disturbances in the Earth’s magnetic field caused by anything magnetic; airport scanners use them to detect the metal in concealed weapons, for instance.
* A **temperature** sensor is used to measure how hot or cold the sensor's environment is. It’s exactly like the thermometer that you put in your mouth to take your own temperature, except that it’s an electronic one built into the Sense HAT. It reports the temperature as a number in Celsius.
* A **humidity** sensor measures the amount of water vapour in the air. There are several ways to measure it, but the most common is relative humidity. Relative humidity is a ratio, usually given as a percentage, between the actual amount of suspended water vapour and the maximum amount that could be suspended at the current temperature. If there is 100% relative humidity, the air is saturated with water vapour and cannot hold any more.
* A **pressure** sensor (sometimes called a barometer) measures the force exerted by the tiny molecules that make up air. There’s a lot of empty space between air molecules and so they can be compressed to fit into a smaller space; this is what happens when you blow up a balloon. As your breath fills the balloon, you are forcing more air molecules inside and making them more compressed, and this increases the pressure. If you suck air out of a plastic bottle, you’re decreasing the pressure inside it and so the higher pressure on the outside crushes the bottle.

### Explorer HAT

The [Explorer HAT](https://shop.pimoroni.com/products/explorer-hat?variant=1074827129) add-on board for Raspberry Pi has some useful components built in.

The four **capacitive touch sensors** detect when the metal pads connect with a person or object that conducts electricity. Touching one of the capacitive touchpads on the Explorer HAT triggers an event, so it is acting as a switch or button.

## To emulate or not to emulate
While the Sense HAT is an awesome piece of hardware, it can be difficult to test your program with a range of sensor values in real life, such as really hot or cold conditions. Enter the emulator!

The Sense HAT emulator closely simulates the Sense HAT hardware being attached to your Raspberry Pi; you can read from the sensors or write to the LED matrix using Python. It also has sliders that you can move to change the values of the sensor readings, so you can easily test how your code responds to environmental variables.

There are two emulators for the Sense HAT board: a web-based version and a desktop version.

### Web-based emulator

The [online Sense HAT emulator](https://trinket.io/sense-hat), hosted on Trinket, allows you to share projects via direct URL. You can also download the projects you create as zip files so that you can move them to a Raspberry Pi. You can change the Astro Pi emulator to the Sense HAT emulator by pressing the bottom right icon.

## Desktop emulator

The desktop emulator is perfect for offline use and allows you to integrate your Sense HAT program with any available Python modules, or with other Raspberry Pi features such as the Camera Module.

The desktop emulator is installed by default in the Raspberry Pi OS. You can access it from the Desktop menu, under Programming. If it's not there, [instructions to install the desktop Sense Hat emulator can be found here](https://www.raspberrypi.org/blog/desktop-sense-hat-emulator/).



## Enlaces 1

* https://github.com/raspberrypilearning/physical-computing-with-python
* https://github.com/babalugats76/teach-physical-computing
* https://github.com/osteele/imu-tools
* https://github.com/vongomben/fluid-networks
* https://github.com/GIRA/PhysicalBits
* https://projects.raspberrypi.org/en/projects/laser-tripwire
* https://github.com/Wireframe-Magazine/Code-the-Classics
* https://magpi.raspberrypi.com/books/code-the-classics1
* https://projects.raspberrypi.org/en/projects?software[]=python
* https://projects.raspberrypi.org/en/projects/getting-started-with-mu
* https://projects.raspberrypi.org/en/projects?software%5B%5D=python&hardware%5B%5D=raspberry-pi
* https://projects.raspberrypi.org/en/projects?software%5B%5D=python&hardware%5B%5D=sense-hat
* https://store.rpipress.cc/products/code-the-classics
* https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi




## Enlaces 2

* https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/
* https://www.raspberrypi.org/courses/learn-python
* https://projects.raspberrypi.org/en/projects/physical-computing
* https://projects.raspberrypi.org/en/
* https://thepihut.com/products/camjam-edukit
* https://thepihut.com/products/camjam-edukit-2-sensors
* https://thepihut.com/
* https://www.raspberrypi.org/courses/learn-python
* http://www.gr8computing.com/about/
* https://codewith.mu/en/howto/1.0/install_raspberry_pi
* https://pinout.xyz/
* https://gpiozero.readthedocs.io/en/stable/index.html
* https://machinelearningforkids.co.uk/#!/about
* https://dkoudstaal.gitbook.io/raspberry-pi-worksheets
* https://github.com/edgeimpulse/courseware-embedded-machine-learning
* https://wiki.seeedstudio.com/Wio-Terminal-TinyML-Kit-Course/
* https://wiki.seeedstudio.com/Introduction_to_Artificial_Intelligence_for_Makers/
* https://github.com/tinyMLx/courseware
