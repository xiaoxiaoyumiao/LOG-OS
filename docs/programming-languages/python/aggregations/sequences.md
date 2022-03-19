# Sequences

## Sequences / 序列

python 中的 `list` 、`tuple` 、`range` 类型可以表示一个序列。

### List / 列表

sort 

```python
# The syntax of the sort() method is:
list.sort(key=..., reverse=...)
# Alternatively, you can also use Python's built-in sorted() function
for the same purpose.

sorted(list, key=..., reverse=...)
```

* key 接受一个函数，该函数应当能通过作用于一个列表元素获取可比较的排序依据值
* ref: [https://www.programiz.com/python-programming/methods/list/sort](https://www.programiz.com/python-programming/methods/list/sort)
* 使用`reversed`可以获取一个翻转的序列拷贝
* ```text
  zip #并行迭代
  for a,b in zip(seq1,seq2):
      pass
  ```

