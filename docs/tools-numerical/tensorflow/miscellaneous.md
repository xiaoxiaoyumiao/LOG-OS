# Miscellaneous

* tensorflow 2 有单独的 cpu 版本，安装 tensorflow-cpu 即可。
* CUDA 和 tensorflow 版本对照
  * [https://www.tensorflow.org/install/source\#gpu](https://www.tensorflow.org/install/source#gpu)
* 找不到 libcublas.so 时重定义 `LD_LIBRARY_PATH` 可以消除报错
  * [https://stackoverflow.com/questions/55224016/importerror-libcublas-so-10-0-cannot-open-shared-object-file-no-such-file-or](https://stackoverflow.com/questions/55224016/importerror-libcublas-so-10-0-cannot-open-shared-object-file-no-such-file-or)
  * [https://github.com/tensorflow/tensorflow/issues/26182\#issuecomment-684993950](https://github.com/tensorflow/tensorflow/issues/26182#issuecomment-684993950)
  * [https://github.com/tensorflow/tensorflow/issues/28660](https://github.com/tensorflow/tensorflow/issues/28660)
* tfhub 在大陆访问受限，可以使用 tfhub 在中国的镜像地址：

```python
# hub.Module("https://tfhub.dev/google/elmo/2")
hub.Module("https://hub.tensorflow.google.cn/google/elmo/2")
```

* reshape
  * [https://www.tensorflow.org/api\_docs/python/tf/reshape](https://www.tensorflow.org/api_docs/python/tf/reshape)

```text
tf.reshape(
    tensor, shape, name=None
)
```

