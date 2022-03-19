# Array Basics

```text
import numpy as np
```

## Create Arrays

The basic array type in NumPy is `ndarray`. It is also known by the alias `array`. So when we talk about array, we are referring to the `ndarray` unless specified.

An `ndarray` object stores a matrix, every elements of which have the same data type. The matrix is indexed by a tuple of non-negative integers.

Dimensions of matrices are called axes \(`axis`\).

```python
np.array(
    object, 
    dtype = None, 
    copy = True, 
    order = None, 
    subok = False, 
    ndmin = 0
)
"""
#pointer, dtype, shape, stride
#object: 
    array; 
    object exposing the array interface;
    object whose __array__ returns an array
    nested list
#dtype: data type
#copy: if this is a copy
"""

a = np.array([[1,2],[3,4]])
b = np.array([1+1.j,2+1.j],dtype = np.complex)  # a complex array

# use function of coordinates to create an array from a given shape
np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)
array([[ True, False, False],
       [False,  True, False],
       [False, False,  True]])
```

## Properties

```python
>>> a = np.array([[1,2],[3,4],[5,6]])
>>> a.ndim
2
>>> a.shape
(3, 2)
>>> a.size
6
>>> a.dtype
dtype('int32')
>>> a.dtype.name
'int32'
>>> print(a)
[[1 2]
 [3 4]
 [5 6]]
```

* data types for np:
  * bool
  * int8 int16 int32 int64
  * uint8 uint16 uint32 uint64
  * float float16 float32 float64
  * complex64 complex128

```python
dt = np.dtype(np.int32) # this is an np.dtype object
```

## Special Arrays

Notice that following methods all return array objects.

```python
np.empty(shape) # 未初始化
np.zeros(shape) # 全零数组
np.ones(shape) # 全1数组
np.asarray(data) # 从已有的矩阵结构数据创建数组

# create sequences:
# [x for x in range(start,stop) if x-start % step == 0]:
np.arrange(start,stop,step,dtype)
# [start+x*(stop-start)/(num-1) for x in range(num)]
np.linspace(start,stop,num,endpoint=True)
# [base**(start+x*(stop-start)/(num-1)) for x in range(num)]
np.logspace(start,stop,num,endpoint=True,base=10.0)

# create a 1-dim array from an object exposing the buffer interface
np.frombuffer(buffer)

# create a 1-dim array from an iterable object
np.fromiter(iterable)
```

## Indexing, Slicing & Iterating

```python
a = np.array([[1,2],[3,4],[5,6]])

# Indexing:
a[2, 3]

# Slicing
a[0:2, 1:2] # [[2],[4]]
a[0:2, 1] # [2, 4]
# use ... or : to take the whole slice
a[:, 1] # [2,4,6]

# 取a的[0,0],[1,1],[2,0]索引并返回数列
a[[0,1,2],[0,1,0]] # [1,4,5]

#数组Iteration:
#nditer迭代
for x in np.nditer(a):
    #...
#默认按内存存储顺序访问，指定C风格为行优先，Fortran风格为列优先
order = 'C'
order = 'F'
#通过指定读取模式修改数组元素：
op_flags=['readwrite']
#flat迭代
for x in a.flat:
    #...
```

## Arithmetic Operations

```python
b = a.reshape(2,3)
b = np.transpose(a,axes)#对换
b = a.T() #转置
b = np.swapaxes(a,axis1,axis2)#对应轴的索引，从0开始算
b = np.expand_dims(a,axis)#扩展一个新轴
b = np.squeeze(a,axis)#删除长度为1的维度
b = np.concatenate((arr1,arr2,...),axis)#沿axis连接相同宽度的arr形成新数组
b = np.stack((arr1,arr2,...),axis)#沿axis堆叠相同形状的arr形成新数组

np.add(a,b) or a+b
np.subtract(a,b) or a-b
np.multiply(a,b) or a*b
np.divide(a,b) or a/b 
np.power(a,b) or a**b
np.mod(a,b) or a%b
#以上都是逐项运算，要求同型
np.dot(a,b) or a@b #矩阵乘积
np.linalg.det(a)
np.linalg.solve(a)
np.linalg.inv(a)

np.sum(a, axis=None, dtype=None, out=None, keepdims=np._NoValue)
```

See also [Python - Emulating numeric types](../../programming-languages/python/numerical.md#emulating-numbers).

## Reference

\[1\] [https://numpy.org/devdocs/user/quickstart.html](https://numpy.org/devdocs/user/quickstart.html)

