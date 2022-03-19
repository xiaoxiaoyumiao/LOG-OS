# Logging

## Introduction

logging 是 python 标准库中专门用来管理程序输出的模块。

## Basics

```python
import logging
logging.warning('Watch out!')  # will print a message to the console
# output
WARNING:root:Watch out!
```

logging 机制的基本对象是 logger 和 handler。logger 对象构成树状结构，接收用户程序的输出调用，控制 logging 内容；handler 将 logger 的输出写入标准输出流、文件等特定位置。此外还有 filter 和 formatter 对象实现对输出进行更精细的定制。

 初始状态下总是存在一个 root logger。logger 需要 handler 才能完成输出，在 `warning` 函数被上述代码调用时，`warning` 函数会检查 root logger 是否拥有至少一个 handler，若没有则会通过 `logging.basicConfig` 为其创建一个默认的 handler（它会把 log 打印到标准输出流）。如果希望为 root logger 分配自定义的 handler，可以像这样定义：

```python
fout = logging.FileHandler('example.log', encoding='utf-8')
sout = logging.StreamHandler(sys.stdout)
logging.basicConfig(handlers=[fout, sout], level=logging.DEBUG)
# logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
```

上述代码做了不少事情。首先观察前两行，我们调用了 `FileHandler` 和 `StreamHandler` 两个类的构造函数，它们都是 `logging.Handler` 的子类。前者的构造函数接收了一个文件名参数 `example.log` 和一个字符编码参数 `utf-8` ，它将会把输出写入 `example.log` 文件。后者的构造函数接收一个 stream 或者说 file 对象，这里使用了标准输出流，因此它将会把输出写入标准输出流。不难知道使用 `StreamHandler` 也可以实现向文件写入输出，只需要先调用 `open` 获得一个文件的 file 对象，然后作为参数传入即可。

在调用 `basicConfig` 函数时，我们将创建的两个 handler 构建为一个列表传给 `handlers` 参数，它们将用于 root logger；同时设置了 `level` 参数，它设定了输出的等级。每一次输出都伴随一个等级信息，所有可能的等级按从低到高排序如下：

| Level | When it’s used |
| :--- | :--- |
| `DEBUG` | Detailed information, typically of interest only when diagnosing problems. |
| `INFO` | Confirmation that things are working as expected. |
| `WARNING` | An indication that something unexpected happened, or indicative of some problem in the near future \(e.g. ‘disk space low’\). The software is still working as expected. |
| `ERROR` | Due to a more serious problem, the software has not been able to perform some function. |
| `CRITICAL` | A serious error, indicating that the program itself may be unable to continue running. |

logging 包含了与各等级相对应的 log 方法（并且我们已经调用了前四个）。

把 `level` 设定为 `DEBUG` 后，等级不低于 `DEBUG`  的 log 就都会被输出。执行上述代码后，应当可以看到四行语句都输出到了标准输出，同时可以找到文件 `example.log` ，它同样包含了输出内容。在需要灵活设定 level 的场合，除了使用较为繁琐的条件语句（例如 switch 之类），使用 `getattr` 或许可以简化代码：

```python
# suppose loglevel stores string representation like "DEBUG" or "ERROR"
numeric_level = getattr(logging, loglevel.upper(), logging.DEBUG)
logging.basicConfig(level=numeric_level, ...)
```

`basicConfig` 只需要在全局被调用一次；同时，之后的调用都不会生效。这意味着你只需要在主过程中调用一次即可配置 root logger 的输出等级、handler 等，这些配置会传递到代码中包含的使用 root logger 的其他模块。

## LogRecord & Formatter

目前的输出都具有同一种默认格式：

```text
DEBUG:root:This message should go to the log file
INFO:root:So should this
WARNING:root:And this, too
ERROR:root:And non-ASCII stuff, too, like Øresund and Malmö
```

事实上输出的格式是可以定制的。你只需要提供一个字符串模板作为格式化的参数。logging 使用的字符串模板是 % 风格的，例如：

```python
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
```

事实上几个基本的 log 方法都支持通过这种老式的格式化风格输出：

```python
logging.warning('%s before you %s', 'Look', 'leap!')
```

为了写出正确的字符串模板，显然需要知道输出的各个要素对应的变量名是什么。事实上，logger 每次 log 时生成的是一个 `logging.LogRecord` 对象，handler 即把 `LogRecord` 对象格式化（即 format）并写入相应位置（官方用语为 emit）。格式化时使用的变量名对应 `LogRecord` 的各个同名的成员变量。部分常用的成员变量如下，可以完成对 log 的产生时间、代码位置、进程/线程、等级等信息的追踪。完整列表请参考 ref: \[4\]。

| Attribute name | Format | Description |
| :--- | :--- | :--- |
| asctime | `%(asctime)s` | Human-readable time when the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord) was created. By default this is of the form ‘2003-07-08 16:49:45,896’ \(the numbers after the comma are millisecond portion of the time\). |
| funcName | `%(funcName)s` | Name of function containing the logging call. |
| levelname | `%(levelname)s` | Text logging level for the message \(`'DEBUG'`, `'INFO'`, `'WARNING'`, `'ERROR'`, `'CRITICAL'`\). |
| message | `%(message)s` | The logged message, computed as `msg % args`. This is set when [`Formatter.format()`](https://docs.python.org/3/library/logging.html#logging.Formatter.format) is invoked. |
| name | `%(name)s` | Name of the logger used to log the call. |
| process | `%(process)d` | Process ID \(if available\). |
| processName | `%(processName)s` | Process name \(if available\). |
| thread | `%(thread)d` | Thread ID \(if available\). |
| threadName | `%(threadName)s` | Thread name \(if available\). |

## Reference

\[1\] [https://docs.python.org/3/library/logging.html\#logging.basicConfig](https://docs.python.org/3/library/logging.html#logging.basicConfig)

\[2\] [https://docs.python.org/3/glossary.html\#term-file-object](https://docs.python.org/3/glossary.html#term-file-object)

\[3\] [https://docs.python.org/3/howto/logging.html\#logging-basic-tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)

\[4\] [https://docs.python.org/3/library/logging.html\#logging.LogRecord](https://docs.python.org/3/library/logging.html#logging.LogRecord)

