# Ejemplo tomado de Digikey

## El flujo de trabajo de desarrollo de la OTA

En general, el proceso para configurar una actualización OTA en el ESP32 implica los siguientes pasos:
1. Configurar la tabla de particiones del ESP32
2. Descargar el firmware que soporta OTA
3. Desarrollar una herramienta que actúe como servidor y empuje el nuevo firmware
4. Descargue el último firmware en el ESP32
5. Cambiar a la nueva aplicación

Vemos a ver este manual: https://github.com/espressif/esp-idf/tree/1067b28/examples/system/ota

Si todo esta bien el microcontrolador debera empezar a parpadear..

## Referencias

1. https://learn.adafruit.com/bluefruit-nrf52-feather-learning-guide/using-the-bootloader
2. https://learn.adafruit.com/introducing-adafruit-ble-bluetooth-low-energy-friend/field-updates
3. https://learn.adafruit.com/bluefruit-le-python-library
4. https://www.arduino.cc/reference/en/libraries/arduinoota/
5. https://www.luisllamas.es/como-programar-el-esp8266-por-wifi-con-arduino-ota/
6. https://esp8266-arduino-spanish.readthedocs.io/es/latest/ota_updates/readme.html
7. https://www.aranacorp.com/es/programacion-de-un-esp8266-a-traves-de-wifi-con-el-ide-de-arduino-ota/
8. https://docs.espressif.com/projects/arduino-esp32/en/latest/
9. https://docs.espressif.com/projects/arduino-esp32/en/latest/ota_web_update.html
10. https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/ota.html