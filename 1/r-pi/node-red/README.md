# rPi + Node-RED

Logueo por ssh

```
ssh tigarto@192.168.1.31
```
Logueo usando ssh

![1](1_log-ssh.png)

Flow 1

```json
[
    {
        "id": "a81bd2735ebc682b",
        "type": "tab",
        "label": "Flow 1",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "651f7c81d07f3f91",
        "type": "rpi-gpio out",
        "z": "a81bd2735ebc682b",
        "name": "Red LED",
        "pin": "17",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "bcm": true,
        "x": 480,
        "y": 180,
        "wires": []
    },
    {
        "id": "6eb584b004d1f161",
        "type": "inject",
        "z": "a81bd2735ebc682b",
        "name": "On",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "1",
        "payloadType": "str",
        "x": 190,
        "y": 120,
        "wires": [
            [
                "651f7c81d07f3f91",
                "a55d4cb53a1fee0b"
            ]
        ]
    },
    {
        "id": "655ea2086d0bf295",
        "type": "inject",
        "z": "a81bd2735ebc682b",
        "name": "Off",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "0",
        "payloadType": "str",
        "x": 190,
        "y": 240,
        "wires": [
            [
                "651f7c81d07f3f91",
                "a55d4cb53a1fee0b"
            ]
        ]
    },
    {
        "id": "a55d4cb53a1fee0b",
        "type": "debug",
        "z": "a81bd2735ebc682b",
        "name": "msg.payload",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "statusVal": "",
        "statusType": "auto",
        "x": 570,
        "y": 80,
        "wires": []
    }
]
```

flow2:

```json
[
    {
        "id": "e253cdbafd0ec549",
        "type": "tab",
        "label": "Flow 2",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "2242eed60d6bc5ca",
        "type": "rpi-gpio out",
        "z": "e253cdbafd0ec549",
        "name": "Red LED",
        "pin": "17",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "bcm": true,
        "x": 720,
        "y": 280,
        "wires": []
    },
    {
        "id": "03a770c6a86c3407",
        "type": "debug",
        "z": "e253cdbafd0ec549",
        "name": "msg,payload",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "statusVal": "",
        "statusType": "auto",
        "x": 490,
        "y": 100,
        "wires": []
    },
    {
        "id": "ae8e77bef88ccdcc",
        "type": "rpi-gpio in",
        "z": "e253cdbafd0ec549",
        "name": "Button",
        "pin": "4",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "bcm": true,
        "x": 150,
        "y": 220,
        "wires": [
            [
                "03a770c6a86c3407",
                "db763ea9d08af420"
            ]
        ]
    },
    {
        "id": "db763ea9d08af420",
        "type": "switch",
        "z": "e253cdbafd0ec549",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "repair": false,
        "outputs": 2,
        "x": 330,
        "y": 280,
        "wires": [
            [
                "0bd645c2410ec981"
            ],
            [
                "dc8745fc1c7c2e1c"
            ]
        ]
    },
    {
        "id": "0bd645c2410ec981",
        "type": "change",
        "z": "e253cdbafd0ec549",
        "name": "change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 510,
        "y": 220,
        "wires": [
            [
                "2242eed60d6bc5ca"
            ]
        ]
    },
    {
        "id": "dc8745fc1c7c2e1c",
        "type": "change",
        "z": "e253cdbafd0ec549",
        "name": "change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 510,
        "y": 340,
        "wires": [
            [
                "2242eed60d6bc5ca"
            ]
        ]
    }
]
```

flow3

```json
[
    {
        "id": "3ff1b4dac67bc190",
        "type": "tab",
        "label": "Flow 3",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "2714b86db734fc85",
        "type": "rpi-gpio out",
        "z": "3ff1b4dac67bc190",
        "name": "Red LED",
        "pin": "17",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "bcm": true,
        "x": 660,
        "y": 180,
        "wires": []
    },
    {
        "id": "eee1578fb0b0af91",
        "type": "delay",
        "z": "3ff1b4dac67bc190",
        "name": "",
        "pauseType": "delay",
        "timeout": "5",
        "timeoutUnits": "seconds",
        "rate": "1",
        "nbRateUnits": "1",
        "rateUnits": "second",
        "randomFirst": "1",
        "randomLast": "5",
        "randomUnits": "seconds",
        "drop": false,
        "allowrate": false,
        "outputs": 1,
        "x": 280,
        "y": 280,
        "wires": [
            [
                "723cc2be63703bb9",
                "c7ecd796513c0846"
            ]
        ]
    },
    {
        "id": "c7ecd796513c0846",
        "type": "rpi-gpio out",
        "z": "3ff1b4dac67bc190",
        "name": "Green LED",
        "pin": "27",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "bcm": true,
        "x": 670,
        "y": 280,
        "wires": []
    },
    {
        "id": "4e134e0c9ca33ce8",
        "type": "inject",
        "z": "3ff1b4dac67bc190",
        "name": "Start",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "1",
        "payloadType": "str",
        "x": 130,
        "y": 180,
        "wires": [
            [
                "eee1578fb0b0af91",
                "2714b86db734fc85"
            ]
        ]
    },
    {
        "id": "723cc2be63703bb9",
        "type": "change",
        "z": "3ff1b4dac67bc190",
        "name": "change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 470,
        "y": 220,
        "wires": [
            [
                "2714b86db734fc85"
            ]
        ]
    }
]
```

## Referencias

* https://www.raspberrypi.org/curriculum/key-stage-4
* https://www.deviceplus.com/raspberry-pi/the-ultimate-guide-to-taking-screenshots-on-a-raspberry-pi/
* https://randomnerdtutorials.com/getting-started-node-red-raspberry-pi/
* https://randomnerdtutorials.com/install-node-red-raspberry-pi/
* https://projects.raspberrypi.org/en/projects/getting-started-with-node-red
* https://help.ubidots.com/en/articles/1958375-how-to-install-node-red-in-raspberry-pi
* https://nodered.org/docs/getting-started/raspberrypi
  
