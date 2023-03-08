# Miscellaneous

* `__future__`&#x20;
  * A pseudo-module which programmers can use to enable new language features which are not compatible with the current interpreter.
  * ref: [https://docs.python.org/3/glossary.html](https://docs.python.org/3/glossary.html)
* 环境变量
  * `os.environ` 是运行 python 解释器时从系统读入环境变量得到的 dict 对象，在运行后修改环境变量不会改变这个 dict 的值，但可以直接修改这个 dict ，从而改变 python 程序看到的环境变量。在使用交互式解释器时很有作用。
  * ref: [https://docs.python.org/3/library/os.html#os.environ](https://docs.python.org/3/library/os.html#os.environ)
* Hashing
  * An object is _hashable_ if it has a hash value which never changes during its lifetime (it needs a `__hash__()` method), and can be compared to other objects (it needs an `__eq__()` method). Hashable objects which compare equal must have the same hash value.
  * REF: [https://docs.python.org/3/glossary.html#term-hashable](https://docs.python.org/3/glossary.html#term-hashable)
