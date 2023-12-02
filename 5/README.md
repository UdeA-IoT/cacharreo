# Ejemplo

Referencias principales: 
* https://github.com/tensorflow/tensorflow/tree/be4f6874533d78f662d9777b66abe3cdde98f901/tensorflow/lite/experimental/micro
* https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/examples/hello_world
* https://www.tensorflow.org/lite/microcontrollers/get_started_low_level?hl=es-419
* 

Over the course of this chapter, we will do the following:
1. Obtain a simple dataset.
2. Train a deep learning model.
3. Evaluate the model’s performance.
4. Convert the model to run on-device.
5. Write code to perform on-device inference.
6. Build the code into a binary.
7. Deploy the binary to a microcontroller.

Sobre la actividad.

* The data we’ll be training with is a sine wave
* Our goal is to train a model that can take a value, x, and predict its sine, y. In a realworld application, if you needed the sine of x, you could just calculate it directly.
* The second part of our project will be to run this model on a hardware device. Visually, the sine wave is a pleasant curve that runs smoothly from –1 to 1 and back.
* https://github.com/tensorflow/tensorflow/tree/be4f6874533d78f662d9777b66abe3cdde98f901/tensorflow/lite/experimental/micro/examples/hello_world
* After we get our basic code working, we’ll be deploying in an Arduino Nano 33 BLE Sense

# Parte 1

## Our Machine Learning Toolchain

To build the machine learning parts of this project, we’re using the same tools used by real-world machine learning practitioners.
* Python and Jupyter Notebooks
* Google Colaboratory
* TensorFlow and Keras

## Building Our Model

* Notebook: https://colab.research.google.com/github/tensorflow/tflite-micro/blob/18aec279a0f35af82e4543feae00e1c87a75c8bf/tensorflow/lite/micro/examples/hello_world/train/train_hello_world_model.ipynb

## Converting the Model for TensorFlow Lite

TensorFlow Lite for Microcontrollers. For now, we can think of it as having two main components:
* TensorFlow Lite Converter: This converts TensorFlow models into a special, space-efficient format for use on memory-constrained devices, and it can apply optimizations that further reduce the model size and make it run faster on small devices.
* TensorFlow Lite Interpreter: This runs an appropriately converted TensorFlow Lite model using the most efficient
operations for a given device.

Before we use our model with TensorFlow Lite, we need to convert it. We use the TensorFlow Lite Converter’s Python API to do this. It takes our Keras model and writes it to disk in the form of a FlatBuffer, which is a special file format designed to
be space-efficient.

In addition to creating a FlatBuffer, the TensorFlow Lite Converter can also apply optimizations to the model. These optimizations generally reduce the size of the model, the time it takes to run, or both. This can come at the cost of a reduction in accuracy, but the reduction is often small enough that it’s worthwhile

One of the most useful optimizations is **quantization**. By default, the weights and biases in a model are stored as 32-bit floating-point numbers so that high-precision calculations can occur during training. Quantization allows you to reduce the precision of these numbers so that they fit into 8-bit integers—a four times reduction in size. Even better, because it’s easier for a CPU to perform math with integers than with floats, a quantized model will run faster.

In the following cell, we use the converter to create and save two new versions of our model. The first is converted to the TensorFlow Lite FlatBuffer format, but without any optimizations. The second is quantized. Run the cell to convert the model into these two variants:

```py
# Convert the model to the TensorFlow Lite format without quantization
converter = tf.lite.TFLiteConverter.from_keras_model(model_2)
tflite_model = converter.convert()
# Save the model to disk
open("sine_model.tflite," "wb").write(tflite_model)
# Convert the model to the TensorFlow Lite format with quantization
converter = tf.lite.TFLiteConverter.from_keras_model(model_2)
# Indicate that we want to perform the default optimizations,
# which include quantization
converter.optimizations = [tf.lite.Optimize.DEFAULT]
# Define a generator function that provides our test data's x values
# as a representative dataset, and tell the converter to use it
def representative_dataset_generator():
for value in x_test:
# Each scalar value must be inside of a 2D array that is wrapped in a list
yield [np.array(value, dtype=np.float32, ndmin=2)]
converter.representative_dataset = representative_dataset_generator
# Convert the model
tflite_model = converter.convert()
# Save the model to disk
open("sine_model_quantized.tflite," "wb").write(tflite_model)
```

To prove these models are still accurate after conversion and quantization, we use both of them to make predictions and compare these against our test results. Given that these are TensorFlow Lite models, we need to use the TensorFlow Lite interpreter to do so.

Because it’s designed primarily for efficiency, the TensorFlow Lite interpreter is slightly more complicated to use than the Keras API. To make predictions with our
Keras model, we could just call the predict() method, passing an array of inputs.

With TensorFlow Lite, we need to do the following:
1. Instantiate an Interpreter object.
2. Call some methods that allocate memory for the model.
3. Write the input to the input tensor.
4. Invoke the model.
5. Read the output from the output tensor.

For now, run the following cell to make predictions with
both models and plot them on a graph, alongside the results from our original, unconverted model:

```py
# Instantiate an interpreter for each model
sine_model = tf.lite.Interpreter('sine_model.tflite')
sine_model_quantized = tf.lite.Interpreter('sine_model_quantized.tflite')
# Allocate memory for each model
sine_model.allocate_tensors()
sine_model_quantized.allocate_tensors()
# Get indexes of the input and output tensors
sine_model_input_index = sine_model.get_input_details()[0]["index"]
sine_model_output_index = sine_model.get_output_details()[0]["index"]
sine_model_quantized_input_index = sine_model_quantized.get_input_details()[0]
["index"]
sine_model_quantized_output_index = \
sine_model_quantized.get_output_details()[0]["index"]
# Create arrays to store the results
sine_model_predictions = []
sine_model_quantized_predictions = []
# Run each model's interpreter for each value and store the results in arrays
for x_value in x_test:
    # Create a 2D tensor wrapping the current x value
    x_value_tensor = tf.convert_to_tensor([[x_value]], dtype=np.float32)
    # Write the value to the input tensor
    sine_model.set_tensor(sine_model_input_index, x_value_tensor)
    # Run inference
    sine_model.invoke()
    # Read the prediction from the output tensor
    sine_model_predictions.append(
    sine_model.get_tensor(sine_model_output_index)[0])
    # Do the same for the quantized model
    sine_model_quantized.set_tensor\
    (sine_model_quantized_input_index, x_value_tensor)
    sine_model_quantized.invoke()
    sine_model_quantized_predictions.append(
    sine_model_quantized.get_tensor(sine_model_quantized_output_index)[0])

# See how they line up with the data
plt.clf()
plt.title('Comparison of various models against actual values')
plt.plot(x_test, y_test, 'bo', label='Actual')
plt.plot(x_test, predictions, 'ro', label='Original predictions')
plt.plot(x_test, sine_model_predictions, 'bx', label='Lite predictions')
plt.plot(x_test, sine_model_quantized_predictions, 'gx', \
label='Lite quantized predictions')
plt.legend()
plt.show()
```

We can see from the graph that the predictions for the original model, the converted model, and the quantized model are all close enough to be indistinguishable. Things are looking good!

Since quantization makes models smaller, let’s compare both converted models to see the difference in size. Run the following cell to calculate their sizes and compare them:

```py
import os
basic_model_size = os.path.getsize("sine_model.tflite")
print("Basic model is %d bytes" % basic_model_size)
quantized_model_size = os.path.getsize("sine_model_quantized.tflite")
print("Quantized model is %d bytes" % quantized_model_size)
difference = basic_model_size - quantized_model_size
print("Difference is %d bytes" % difference)
```

Our quantized model is smaller than the original version, which is great—
but it’s only a minor reduction in size. In addition to weights, the model contains all the logic that makes up the architecture of our deep learning network, known as its **computation graph**.

## Converting to a C File


The final step in preparing our model for use with TensorFlow Lite for Microcontrollers is to convert it into a C source file that can be included in our application.

In the file, the model is defined as an array of bytes. Fortunately, there’s a convenient Unix tool named xxd that is able to convert a given file into the required format.

The following cell runs xxd on our quantized model, writes the output to a file called *sine_model_quantized.cc*, and prints it to the screen:

```py
# Install xxd if it is not available
!apt-get -qq install xxd
# Save the file as a C source file
!xxd -i sine_model_quantized.tflite > sine_model_quantized.cc
# Print the source file
!cat sine_model_quantized.cc
```

The output is very long:

```py
unsigned char sine_model_quantized_tflite[] = {
0x1c, 0x00, 0x00, 0x00, 0x54, 0x46, 0x4c, 0x33, 0x00, 0x00, 0x12, 0x00,
0x1c, 0x00, 0x04, 0x00, 0x08, 0x00, 0x0c, 0x00, 0x10, 0x00, 0x14, 0x00,
// ...
0x00, 0x00, 0x08, 0x00, 0x0a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x09,
0x04, 0x00, 0x00, 0x00
};

unsigned int sine_model_quantized_tflite_len = 2512;
```

To use this model in a project, you could either copy and paste the source or download the file from the notebook.

## Wrapping Up

we’ll write code to run our model on microcontrollers.

# Parte 2

## The “Hello World” of TinyML: Building an Application

**Archivos**:
* **Libro**: 
  * [hello_world_test.cc](https://github.com/tensorflow/tensorflow/blob/be4f6874533d78f662d9777b66abe3cdde98f901/tensorflow/lite/experimental/micro/examples/hello_world/hello_world_test.cc)
  * [micro_test.h](https://github.com/tensorflow/tensorflow/blob/be4f6874533d78f662d9777b66abe3cdde98f901/tensorflow/lite/experimental/micro/testing/micro_test.h)
* **Pagina mas actualizada** [[link]](https://github.com/tensorflow/tflite-micro/tree/main): 
  * [hello_world_test.cc](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/examples/hello_world/hello_world_test.cc) 


Vamos a instalar bazel: https://bazel.build/?hl=es-419

1. Averiguar la version de windows
2. Instalar los requisitos previos: https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170
3. Descarga Bazel (https://github.com/bazelbuild/bazelisk):
   * Para WindowsSi no se tiene instalado el Chocolatey instalelo (https://chocolatey.org/)
   * Si lo tiene instalado ejecute como administrador:
  
     ```
     choco install bazelisk
     ```

4. Verificar la instalación:
   
   ```
   bazel version
   ```

En una ruta conocida descargue el tensor flow (vamos a hacerlo con el nuevo):

Siguiendo: https://www.tensorflow.org/lite/microcontrollers?hl=es-419

Vamos para el repo: https://github.com/tensorflow/tflite-micro.git

Se van a correr los scripts.

Antes de usar bazel: https://bazel.build/start/cpp?hl=es-419 tener en cuenta:
* WORKSPACE file 
* BUILD files

Veamos el siguiente foro: https://github.com/bazelbuild/bazel/issues/17655

https://bazel.build/concepts/dependencies?hl=es-419


Parece que hay este problema: https://www.tensorflow.org/install/gpu?hl=es-419

Toca probar en el WSL si da:

Tampoco dio.



El de Tensor Flow


* https://stackoverflow.com/questions/53920822/how-to-write-the-xxd-command-in-cmd-in-windows
* https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/format-hex?view=powershell-7.4
* https://isc.sans.edu/diary/Dumping+File+Contents+in+Hex+in+PowerShell/25118
* https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/format-hex?view=powershell-7.4&viewFallbackFrom=powershell-6
* https://community.chocolatey.org/packages/xxd

