# Containers

## Set / 集合

集合不能做slice，index等操作；可以做交并和差（补）运算；

```python
ele in set #判断是否在集合中
x & y   #and
x | y   #or
x - y   #not
x ^ y   #xor
x = {1,2,3} #集合用花括号括起来
x = set(y) #列表、字符串等转集合，可以去重，不知复杂度如何
set_a.add(x) #add one item
set_a.update([a,b,c]) #add items
set_a.remove(x) #remove，必须在集合中，否则出错
len(set_a)
s.issuperset(t)
s >= t
#测试是否 t 中的每一个元素都在 s 中
​
s.union(t)
s | t
#返回一个新的 set 包含 s 和 t 中的每一个元素
​
s.intersection(t)
s & t
#返回一个新的 set 包含 s 和 t 中的公共元素
​
s.difference(t)
s - t
#返回一个新的 set 包含 s 中有但是 t 中没有的元素
​
s.symmetric_difference(t)
s ^ t
#返回一个新的 set 包含 s 和 t 中不重复的元素
​
s.copy()
#返回 set “s”的一个浅复制
```

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

## **Dict / 字典**

字典的键必须是不可变对象，这包括数字、字符串和元组。

```python
a = {}              # create empty dict
a[1] = 2            # add
a["what"] = "guy"   # add
# print(a[2])       # KeyError
a[1] = 3            # modify
del a["what"]       # delete item
a.clear()           # clear all items
​
b = {1:2, 3:4}      # create a dict with items
len(b)              # size of dict
dict.get(key, default=None)
item = b.get(1)     # ret val of given key(1) if exists, otherwise ret None
item = b.get(2, "Nothing")  # will return "Nothing" as b[2] is empty
dict.setdefault(key, default=None)
# deprecated in py3 dict.has_key(somekey)       # ret True if somekey exists as a key
dict.items()        # ret all items of form (key, value)(iterable)
dict.keys()         # ret all keys(iterable)
```

## Collections

`collections.defaultdict(function_factory)`，创建一个`dict`对象，所有value都是function的实例，并且对不存在的key，d\[key\]也有一个该function实例的默认值。例如，`defaultdict(int)`创建一个key到int类型的映射，并且每个不存在的key都有一个默认值value：0.

内建转换函数都是工厂函数。例如，`int(),long(),float(),complex(),str(), unicode(), basestring(),list(), tuple(), type(), dict(), bool(),set(), frozenset(),object() ,classmethod(),staticmethod(), super(), property(), file()`

