# TensorFlow

**Fecha**: 12/12/2023

Se intento instalar localmente TensorFlow de manera que las pruebas de los ejemplos de la pagina oficial lograran pasar. Para ello, se siguió el enlace https://shawnhymel.com/2034/how-to-install-tensorflow-on-windows/. Debido a problemas con la aplicación de algunos comandos en la maquina local, los comandos aplicados variaron un poco respecto a la guia original. Todas las imagenes del procedimiento realizado se encuentran en el directorio [imagenes_instalacion](imagenes_instalacion/).

La siguiente tabla muestra el comando de la guia y el aplicado como metodo de comparación:

|Comando tutorial|Comando aplicado|Observaciones|
|---|---|---|
|```conda create --name tensorflow-cpu```|```conda create --name tensorflow-cpu python=3.7```|Problemas en la instalación local de anaconda disponible en la maquina en la que se ejecutaron los comandos.|   
|```conda activate tensorflow-cpu```|```conda activate tensorflow-cpu```||
|```python --version```|```python --version``|La instalación se hizo en el primer comando.|
|```conda install python=3.7```||La instalación se hizo en el primer comando por lo que la aplicacion de este no fue necesaria.|
|```conda install jupyter```|```pip3 install jupyter```|Problemas con Conda para la busqueda de las librerias a instalar|
|```python -m pip install <wheel_url>```|```pip3 install tensorflow_cpu==2.2.0```|La wheel pip recomendada en la guia no se encontraba ya en el link oficial: https://www.tensorflow.org/install/pip?hl=es-419#package-location|
||```pip3 install protobuf==3.20.0```|Fue necesario hacer un downgrade de esta biblioteca para que pudiera importarse sin errores TensorFlow|

Para despues de aplicar los comandos anteriores, si se esta en la terminal se VSCode intente seguir los siguientes enlaces para configurarla con el entorno:
* https://code.visualstudio.com/docs/python/environments
* https://saturncloud.io/blog/activating-anaconda-environment-in-vscode-a-guide-for-data-scientists/
* https://medium.com/analytics-vidhya/efficient-way-to-activate-conda-in-vscode-ef21c4c231f2

## Conclusión

> Como no nos dio la configuración del entorno como queriamos, la recomendacion es trabajar desde la nube.


## Referencias principales

1. https://github.com/ferrcho024/Project_to_C/tree/main/tinyML/1_helloworld/arduino_nano
2. https://shawnhymel.com/2034/how-to-install-tensorflow-on-windows/
3. https://shawnhymel.com/1961/how-to-install-tensorflow-with-gpu-support-on-windows/
4. https://www.educative.io/answers/conda-install


## Anexo - Comandos hechos a la loca

A continuación se encuentran intentos a la loca para ver si daban los resultados deseados. Al final nos quedo grande la cosa. De todas maneras aqui quedan:


```
conda create --name tensorflow-cpu python=3.7
```

```
python --version
```

```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

**En WSL**

```
pip3 install jupyter
pip3 install tensorflow_cpu==2.2.0	
pip3 install protobuf==3.20.0
pip2 install numpy==1.23.4
sudo apt update && sudo apt install bazel-1.1.0
```

**Pendiente**: Mirar si por aca: https://github.com/protocolbuffers/protobuf/blob/main/src/README.md#c-installation---windows



