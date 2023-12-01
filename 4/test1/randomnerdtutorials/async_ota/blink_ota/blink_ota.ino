 /*
  AsyncElegantOTA Demo Example - This example will work for both ESP8266 & ESP32 microcontrollers.
  -----
  Author: Ayush Sharma ( https://github.com/ayushsharma82 )
  
  Important Notice: Star the repository on Github if you like the library! :)
  Repository Link: https://github.com/ayushsharma82/AsyncElegantOTA
*/

#if defined(ESP8266)
  #include <ESP8266WiFi.h>
  #include <ESPAsyncTCP.h>
#elif defined(ESP32)
  #include <WiFi.h>
  #include <AsyncTCP.h>
#endif

#include <ESPAsyncWebServer.h>
#include <AsyncElegantOTA.h>

const char* ssid = "Alberto";
const char* password = "22181224";

AsyncWebServer server(80);

void setup(void) {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  // Print ESP Local IP Address
  Serial.println(WiFi.localIP());

  AsyncElegantOTA.begin(&server);    // Start AsyncElegantOTA
  server.begin();
  Serial.println("HTTP server started");
}

void loop(void) {
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);  
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
}
