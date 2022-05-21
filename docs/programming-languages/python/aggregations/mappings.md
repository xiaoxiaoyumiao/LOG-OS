# Mappings

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

