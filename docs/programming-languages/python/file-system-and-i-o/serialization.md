# Serialization

## Introduction

序列化（Serialization）是在对象与（字节）序列之间建立映射的过程。通过序列化方法可以把对象编码为方便存储的序列，以及从已有的序列中解码得到对象（即反序列化）。在想要存储或者传输一些具有复杂结构的对象的时候，就可以考虑序列化。

序列化的核心在于映射的规则。在处理的对象结构相对固定或比较简单的时候，自己实现一套映射的规则也是可以的，但如果对象较为复杂，或者希望序列化后的对象能被其他人也方便地读取和使用，那么不妨采用标准的序列化模块。

## **JSON & Pickle**

`json` 和 `pickle` 两个模块提供的基本方法大致相同，但针对的数据类型和序列化的方法不同。

`dump` 把序列化的数据存储在文件中。

`load` 从文件中读取序列化的数据并反序列化。

`dumps` 直接返回序列化的数据。\(s 或许是 sequence 的缩写）

`loads` 接收序列本身并反序列化为数据。

JSON 是非常通用的序列化协议，但因此也只能序列化 Python 的一部分内置类型和由它们复合而成的数据结构；Pickle 则可以处理大部分 Python 数据类型，但也只能用于 Python。

Pickle 并不安全，使用时需要保证序列化数据来源是可信的。

JSON 协议编码得到的序列是可读文本（如使用 unicode 或 utf-8 编码），而 Pickle 协议编码得到的是二进制序列。因此在从文件读或者向文件写序列化对象的时候，要注意相应地设置文件被打开的模式。对 JSON 而言，应当使用 "r" 或者 "w" 模式，对 Pickle 而言则应当使用 "rb" 或者 "wb"。同时，调用 `dumps` 和 `loads` 时注意 JSON 的序列化数据格式为 str，而 Pickle 的序列化数据格式为 bytes。

在对象结构比较简单时，JSON 序列可以用 eval 反序列化。

```text
json.dump(data, file)
data = json.load(file)

string = json.dumps(data)
data = json.loads(string)
data = eval(string)

pickle.dump(data, file)
data = pickle.load(file)
```

## Reference

\[1\] [https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)

