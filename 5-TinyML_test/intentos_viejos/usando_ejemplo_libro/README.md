# Tomemos el repo del libro

Sigamos el video:

https://www.youtube.com/watch?v=AfAyHheBk6Y


```
bazel build tensorflow/lite/micro/examples/hello_world:train
bazel-bin/tensorflow/lite/micro/examples/hello_world/train --save_tf_model --save_dir=/tmp/model_created/
```

```
ls /tmp/model_created/
```

```
bazel build tensorflow/lite/micro/examples/hello_world/quantization:ptq

```

https://tinyml.seas.harvard.edu/AAAI-23/

* https://shawnhymel.com/tag/machine-learning/
* https://www.youtube.com/watch?v=SUzgJm-x4sA
* https://de.mathworks.com/matlabcentral/answers/1631265-matlab-coder-how-do-i-build-tensorflow-lite-for-deep-learning-c-code-generation-and-deployment


Del texto:
* https://github.com/tensorflow/tensorflow/tree/be4f6874533d78f662d9777b66abe3cdde98f901/tensorflow/lite/experimental

De la pagina:
* https://www.tensorflow.org/lite?hl=es-419
