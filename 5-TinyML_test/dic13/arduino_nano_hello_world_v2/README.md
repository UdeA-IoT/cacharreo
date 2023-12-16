# Ejemplo

## En construccion...

Las referencias se toman de: https://github.com/Mjrovai/UNIFEI-IESTI01-TinyML-2022.1/tree/main/00_Curse_Folder/2_Applications_Deploy/Class_18


|Clase|Tema|Slides|Doc|Video|Repo|Code|
|---|---|---|---|---|---|---|
|Class 18|TFLite-Micro Overview & Hello World Code Walkthrough|[S](https://github.com/Mjrovai/UNIFEI-IESTI01-TinyML-2022.1/blob/main/00_Curse_Folder/2_Applications_Deploy/Class_18/IESTI01_TinyML_class_18.pdf)|[D](https://github.com/Mjrovai/UNIFEI-IESTI01-TinyML-2022.1/tree/main/00_Curse_Folder/2_Applications_Deploy/Class_18/docs)|[V](https://www.youtube.com/watch?v=GPZ9FeGfizE&feature=youtu.be)|[R](https://github.com/Mjrovai/UNIFEI-IESTI01-TinyML-2022.1/tree/main/00_Curse_Folder/2_Applications_Deploy/Class_18)|[C](https://github.com/Mjrovai/UNIFEI-IESTI01-TinyML-2022.1/tree/main/00_Curse_Folder/2_Applications_Deploy/Class_18/hello_world_V2)|



### Test 1

```cpp
...
// This is tuned so that a full cycle takes ~4 seconds on an Arduino MKRZERO.
const int kInferencesPerCycle = 1000;
...
```

Con $kInferencesPerCycle = 1000$ tenemos las siguientes pruebas:

|Test|```kInferencesPerCycle```|Comportamiento|
|---|---|---|
|$1\times k$|```1000```|Valor por defecto; se puede apreciar el cambio de iluminación en el Led|
|$10\times k$|```10000```|El periodo sube por lo que el cambio en el brillo en el LED se hace mas lento.|
|$k/10$|```100```|El periodo disminuye y por tanto la frecuencia aumenta, el cambio de brillo en el Led no tan perceptible.|
|$k/100$|```10```|Aumenta aun mas la frecuencia por lo que practicamente no se nota el cambio en el brillo en el led.|


### Test 2

```cpp
 // Log the current brightness value for display in the Arduino plotter
// TF_LITE_REPORT_ERROR(error_reporter, "%d\n", brightness);
TF_LITE_REPORT_ERROR(error_reporter, "sen(%f) = %f -> %d", x_value, y_value, brightness);
```


## Referencias

1. https://github.com/TexasInstruments/
2. https://github.com/TexasInstruments/ble_examples
3. https://github.com/TexasInstruments/ti-gpio-py
4. https://github.com/TexasInstruments/edgeai-studio-agent
5. https://github.com/TexasInstruments/tensorflow-lite-micro-examples
6. https://github.com/TexasInstruments/edgeai-demo-monodepth-estimation
7. https://github.com/TexasInstruments/edgeai-yolov5
8. https://github.com/TexasInstruments/edgeai
9. https://github.com/TexasInstruments/edgeai-mmdetection
10. https://github.com/TexasInstruments/edgeai-demo-audio-visual
11. https://github.com/TexasInstruments/edgeai-modelzoo
12. https://github.com/TexasInstruments/edgeai-benchmark
13. https://github.com/TexasInstruments/edgeai-modelmaker
14. https://github.com/TexasInstruments/edgeai-keyword-spotting
15. https://github.com/TexasInstruments/edgeai-gst-apps-6d-pose
16. https://github.com/TexasInstruments/edgeai-gst-apps-human-pose
17. https://github.com/TexasInstruments/tensorflow
18. https://github.com/TexasInstruments/edgeai-robotics-demos
19. https://forum.edgeimpulse.com/t/basic-sinusoidal-predictor-tutorial-help/2079/5
20. 