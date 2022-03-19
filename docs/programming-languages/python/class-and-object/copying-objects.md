# Copying Objects

Python 的对象赋值一般来说并不拷贝对象，而是像创建指针一样把变量绑定到对象上。但有时我们需要拷贝对象（例如，为了避免对原对象进行不必要的修改）。

## copy

标准库中的 `copy` 模块能满足基本的复制需求。浅拷贝复制对象时保持其成员的值，对象拥有的对其他对象的引用不会改变；深拷贝则会递归地处理对象包含的引用，并把它们指向的对象也一同复制。

```python
copy.copy(x)
# Return a shallow copy of x.

copy.deepcopy(x[, memo])
# Return a deep copy of x.
```

## Reference

\[1\] [https://docs.python.org/3/library/copy.html](https://docs.python.org/3/library/copy.html)



