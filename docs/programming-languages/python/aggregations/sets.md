# Sets

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
a = set('abracadabra') # 可以从字符串转换

len(set_a) # 获取集合的大小。
set_a.add(x) # 将一个元素加入当前集合。
set_a.update([a,b,c]) # 将另一个容器的元素加入当前集合。
set_a.remove(x) # 移除元素 x，x 不在集合中时产生一个 KeyError。

s.issuperset(t)
s >= t # 判断 t 是否为 s 的子集
​
s.union(t)
s | t # 集合并集运算
​
s.intersection(t)
s & t # 集合交集运算
​
s.difference(t)
s - t # 集合差集运算
​
s.symmetric_difference(t)
s ^ t # 集合对称差运算
​
s.copy()
# 返回一个浅复制
```

## Reference

\[1\] [https://docs.python.org/3.7/library/stdtypes.html\#set-types-set-frozenset](https://docs.python.org/3.7/library/stdtypes.html#set-types-set-frozenset)

