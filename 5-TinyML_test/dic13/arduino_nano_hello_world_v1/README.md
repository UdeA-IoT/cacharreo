
# Hello World en el microcontrolador

En esta parte se describirá como cargar el modelo en el Arduino Nano usando la libreria TensorFlow Lite for Microcontrolers. En este ejemplo, el modelo descargado en el micro llevara a cabo una inferencia para generar una señal aproximada de la función seno.

![1](network_model.png)

Antes de descargar el modelo en el micro, fue necesario entrenarlo usando Tensor Flow Lite ([tflite_sinewave_training.ipynb](../tflite_sinewave_training.ipynb)). El resultado final fue un archivo cabecera .h ([sine_model.h](../sine_model.h)) el cual contiene el mdoelo que será cargado en el programa en C.

![2](hello_world_tfmodel.png)

Para usar el modelo, es necerario incluirlo (wrap) en un código que configure permita usarlo en el microcontrolador para obtener el comportamiento deseado.

![3](0.png)


In this chapter, we will build an embedded application that uses our sine model to
create a tiny light show. We’ll set up a continuous loop that feeds an x value into the
model, runs inference, and uses the result to switch an LED on and off, or to control
an animation if our device has an LCD display.

A continuación se describirá el procedimiento para desarrollar una aplicación embebida que usa el modelo (funcion seno en nuestro caso) para controlar la intensidad del brillo de un led de acuerdo a la señal seno generada por el modelo.

## Hardware

La plataforma a usar sera un  Arduino Nano 33 BLE Sense ([link](https://store-usa.arduino.cc/products/arduino-nano-33-ble-sense?selectedStore=us)).

![4](arduino_nano_33-iot.png)

Los compentes necesarios para el montaje son:

|#|Componente|Cantidad|
|---|---|---|
|1|Arduino Nano 33 BLE Sense|1|
|2|Resistencia de 220|1|
|3|Led|1|

A continuación se muestra el diagrama de conexiones:

![bb](hello_world_v1_bb.png)

Finalmente, se muestra el esquematico asociado.

![sch](hello_world_v1_sch.png)

## Desarrollo de la aplicación - Sofware

Con los elementos de hardware listos, se procede a desarrollar el software. En el caso vamos a dividir el analisis del programa en varias partes:
* Incluir dependencias
* Declarar variables globales.
* Inicializar (setup)
* Programa principal (loop)



## Incluir dependencias

Se resume en dos pasos principales:

1. Incluir los encabezados de TensorFlow Lite for Microcontrollers:

    ```ino
    // Tensor Flow Lite Headers
    #include <TensorFlowLite.h>
    
    #include "tensorflow/lite/micro/all_ops_resolver.h"
    #include "tensorflow/lite/micro/micro_error_reporter.h"
    #include "tensorflow/lite/micro/micro_interpreter.h"
    #include "tensorflow/lite/schema/schema_generated.h"
    #include "tensorflow/lite/version.h"
    
    #include "tensorflow/lite/c/common.h"
    ...
    ```

2. Incluir el encabezado del modelo:

    
    ```ino
    ...
    // Our model
    #include "sine_model.h"
    ...
    ```

## Variables globales

En esta parte, ee definen las variables globales de la aplicación. Para el ejemplo se tienen:
1. Variables globales asociadas a la aplicación en cuestión:
  
   ```ino
   ...
   // Some settings
   constexpr int led_pin = 2;
   constexpr float pi = 3.14159265;                  // Some pi
   constexpr float freq = 100;                       // Frequency (Hz) of sinewave
   constexpr float period = (1 / freq) * (1000000);  // Period (microseconds)
   ...
   ```
  
2. Apuntadores a estructuras de datos y clases propias de Tensor Flow Lite:

   ```ino
   ...
   // TFLite globals, used for compatibility with Arduino-style sketches
   namespace {
     tflite::ErrorReporter* error_reporter = nullptr;
     const tflite::Model* model = nullptr;
     tflite::MicroInterpreter* interpreter = nullptr;
     TfLiteTensor* model_input = nullptr;
     TfLiteTensor* model_output = nullptr;

     // Create an area of memory to use for input, output, and other TensorFlow
     // arrays. You'll need to adjust this by combiling, running, and looking
     // for errors.
     constexpr int kTensorArenaSize = 5 * 1024;
     uint8_t tensor_arena[kTensorArenaSize];
   } // namespace
   ...
   ```

   En la parte anterior, hay dos lineas de código muy importantes las cuales son:

   ```ino
   ...
   constexpr int kTensorArenaSize = 5 * 1024;
   uint8_t tensor_arena[kTensorArenaSize];
   ...
   ```
     
   En estas lineas lo que se hace es definir la **Tensor Arena**. Esta es un area de memoria que se asocia al modelo para que este pueda ejecutarse. El tamaño no tiene que ser exacto y como no se tiene certeza de que tanto se necesita, este se define a ensayo y error teniendo en cuenta de respetar las limitaciones de memoria del microcontrolador. Un tip es elegir el tamaño de la forma $n\times 1024$, comenzando por un valor alto como punto de partida para que el modelo funcione y luego bajandolo hasta que el modelo no ejecute. El ultimo numero menor para el cual el modelo funcionó el tamaño correspondiente de la **Tensor Arena**.

## Inicialización

Esta parte esta asociada al codigo que se coloca en la función de inicialización (```setup()```):
1. **Inicialización de los modulos del microcontrolador**: En está parte se configuran los modulos del microcontrolador asi como los puertos de entrada y salida. Para el caso solo se hizo enfasis en la inicialización del puerto que se conectará al LED:
   
   
   ```ino
   ...
   // Let's make an LED vary in brightness
   pinMode(led_pin, OUTPUT);
   ...
   ```

2. **Configurar un registro para logging**: Cuando se desarrolla una aplicación para una placa de desarrollo, una de las cosas mas importantes es el proceso de debugging. Normalmente, este procedimiento se desarrolla imprimiendo mensajes haciendo uso de la interfaz serial. Tensor Flow Lite posee diferentes funciones y clases para facilitar esta tarea. Para esto, lo que se suele hacer es usar una instancia de la clase MicroErrorReporter definida en [micro_error_reporter.h](https://github.com/biagiom/tflite-micro-lib/blob/master/tensorflow/lite/core/api/error_reporter.h). 
   

   ```ino
   ...
   // Set up logging (will report to Serial, even within TFLite functions)
   static tflite::MicroErrorReporter micro_error_reporter;
   error_reporter = &micro_error_reporter;
   ...
   ```

3. **Mapear el modelo**: En esta parte lo que se hace es tomar el matriz asociada al modelo (definida en el archivo [sine_model.h](./nano_33_ble_tflite_sine/sine_model.h)) y pasarla mediante el metodo ```GetModel()``` el cual retorna un puntero (a una estructura ```Model``` definida en [schema_generated.h](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/schema/schema_generated.h)) con la representación del modelo.


   ```ino
   ...
   // Map the model into a usable data structure
   model = tflite::GetModel(sine_model);
   ...
   ```

4. Creación de un **```AllOpsResolver```**: El siguiente paso es la creación de una instancia de la clase ```AllOpsResolver``` (**Duda**: Parece que cambio en la implementación nueva. Ver siguiente [link](https://github.com/arduino/ArduinoTensorFlowLiteTutorials/issues/15)). Esta clase permite al interprete de Tensor Flow Lite for microcontrolers acceder a todas las *operaciones* de machine learning (llevadas a cabo para realizar la transformación de las entradas en salidas) ejecutadas por el modelo.  
  
   ```ino
   ...
   // This pulls in all the operation implementations we need.
   // NOLINTNEXTLINE(runtime-global-variables)
   static tflite::AllOpsResolver resolver;
   ...
   ```

5. **Inicializar el interprete**: En esta parte se crea un objeto de la clase ```MicroInterpreter```. Esta clase es el corazon de TensorFlow Lite for Microcontrollers y constituye la pieza magica de codigo que ejecutará el modelo con los datos que se le pasen. Como se puede ver, al microinterprete se le pasan la mayoria de todos los objetos que se han creado: 
      
   ```ino
   ...
   // Build an interpreter to run the model with.
   static tflite::MicroInterpreter static_interpreter(
      model, resolver, tensor_arena, kTensorArenaSize, error_reporter);
   interpreter = &static_interpreter;
   ...
   ```
   
   Posteriormente, posteriormente el microinterprete hace una llamada al método ```AllocateTensors()```. Este metodo recorre todos los tensores definidos por el modelo y asigna, a cada uno de ellos, memoria en el **Tensor Arena**. Es fundamental llamar ```AllocateTensors()``` antes de intentar ejecutar la inferencia, porque de lo contrario la inferencia fallará.

   ```ino
   ...
   // Allocate memory from the tensor_arena for the model's tensors.
   TfLiteStatus allocate_status = interpreter->AllocateTensors();
   if (allocate_status != kTfLiteOk) {
     TF_LITE_REPORT_ERROR(error_reporter, "AllocateTensors() failed");
     return;
   }
   ...
   ```

6. **Definir entradas y salidas del modelo**: 

   ```ino
   ...
   // Obtain pointers to the model's input and output tensors.
   model_input = interpreter->input(0);
   model_output = interpreter->output(0);
   ...
   ```


### Main loop


As discussed earlier, the program we’re building consists of a continuous loop that
feeds an x value into the model, runs inference, and uses the result to produce some
sort of visible output (like a pattern of flashing LEDs), depending on the platform.
Because the application is complex and spans multiple files, let’s take a look at its
structure and how it all fits together.



Once all variables are set up, we can implement the loop() function to execute
the actual operation. In this loop, we read the potentiometer value from pin A0.
Similar to the baseline code, it calculates an average of 20 successive readings to get
a stable value. The value is mapped between 0 and 1 and is copied to the model’s
input tensor. Next, we run MicroInterpreter ->Invoke() to make the inference. The
output is obtained from the output tensor. Since the model output is ranged between
0 and 1, the value is multiplied by 255 and then applied to the LED pin to control the
brightness. The whole code inside loop() is as follows:



(**En construcción...**) En el Loop principal lo que se hace es:
1. Usar el modelo para hacer la prediccion.
2. Imprimir los valores inferidos por serial.
3. Cambiar la intensidad del led.


## Pruebas

### Conexiones

Esquematico

![sch](hello_world_v1_sch.png)

Conexiones

![bb](hello_world_v1_bb.png)

1. ss

```ino
...
// Some settings
constexpr int led_pin = 2;
constexpr float pi = 3.14159265;                  // Some pi
constexpr float freq = 0.5;                       // Frequency (Hz) of sinewave
constexpr float period = (1 / freq) * (1000000);  // Period (microseconds)
...
```
2. Tensor arena

```ino
constexpr int kTensorArenaSize = 2 * 1024;

```

![](test_arena.png)

---

1. https://www.tensorflow.org/lite/microcontrollers/get_started_low_level?hl=es-419#run_inference
2. https://www.digikey.com/en/maker/projects/intro-to-tinyml-part-2-deploying-a-tensorflow-lite-model-to-arduino/59bf2d67256f4b40900a3fa670c14330
3. https://github.com/Mjrovai/UNIFEI-IESTI01-TinyML-2022.1/tree/main/00_Curse_Folder/2_Applications_Deploy/Class_16
4. https://github.com/arduino/ArduinoTensorFlowLiteTutorials?tab=readme-ov-file
5. https://github.com/TexasInstruments
6. 


Fritzing parts: https://forum.fritzing.org/t/arduino-nano-rp2040-parts/12996/5

