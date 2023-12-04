# Usando Make

Inicialmente se estudia la estructura del directorio: tensorflow/lite/micro/examples/hello_world [[link]](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/examples/hello_world)


Dentro de estos esta [hello_world_test.cc](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/examples/hello_world/hello_world_test.cc)


Estamos intentando probar los siguientes comandos:  https://www.tensorflow.org/lite/microcontrollers/library?hl=es-419


Comandos probados:

```
make -f tensorflow/lite/micro/tools/make/Makefile hello_world_test
```

```
make -f tensorflow/lite/micro/tools/make/Makefile hello_world_bin
```

Antes de intentar usar un docker: https://github.com/tensorflow/tensorflow/tree/be4f6874533d78f662d9777b66abe3cdde98f901

Requisitos:
1. Instalar tensor flow (no lo tenia instalado antes de empezar)

```
pip install tensorflow
```

Despues de esto intentaremos usar nuevamente el blaze






## Referencias

1. https://wiki.seeedstudio.com/Wio-Terminal-TinyML/#download-pdf
2. https://www.digikey.com/en/maker/projects/tinyml-getting-started-with-tensorflow-lite-for-microcontrollers/c0cdd850f5004b098d263400aa294023
3. https://www.digikey.com/en/maker/profiles/72825bdd887a427eaf8d960b6505adac
4. https://github.com/tinyMLx/appendix