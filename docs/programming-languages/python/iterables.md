# Iterables

## **Comprehension / 解析式**

列表语法：`[expression for variable in list if conditions]`

生成的是一个列表类型。

同理字典：`{value_exp : key_exp for key,value in dict}`

```python
nums = [n*2 for n in numbers]   #单层循环
words = [word for sent in document for word in sent] #嵌套循环，注意顺序
nums = [n*2 for n in numbers if n>0]    #带条件判断的循环
#另外注意在括号表达式中是可以换行的。比如：
nums = [n*2
    for n in numbers
    if n>0
]
>>> str = "what"
>>> tmp = {index:value for index,value in enumerate(str)}
>>> tmp
{0: 'w', 1: 'h', 2: 'a', 3: 't'}
```

## Built-in Functions for Iterables

```python
# Apply func to every element in iterable; return an iterator (Python 3)
# Multiple iterables can be accepted, in which case
# the func must take elements from every iterabls in parallel. 
map(func, iterable, ...)

# Construct an iterator from those elements of iterable 
# for which func returns true.
# If func is None, the identity function is used.
# Equivalent to (item for item in iterable if func(item))
filter(function, iterable)
```

## Reference

\[1\] [https://stackoverflow.com/questions/25082410/apply-function-to-each-element-of-a-list](https://stackoverflow.com/questions/25082410/apply-function-to-each-element-of-a-list)

\[2\] [https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)

