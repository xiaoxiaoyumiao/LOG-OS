# Class & Object

## Class Definition

```python
class className(Base):#如果要继承的话就写上Base，否则放空；支持重载
    #内置可继承list，dict，object，file，str，set
    def __init__(self,args):
        self.data1 = args[0]
        self.data2 = args[1]
        #pass

    def method1(self,x):
        self.data1 = x
        return x

    def method2(self,x):
        x = x+1
        self.method1(x)
        #...
```

## super

```python
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')

    def bar(self,message):
        print ("%s from Parent" % message)

class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild,self).__init__()    
        print ('Child')
```

## Rewriting Internal Methods

Refer to [Numerical](numerical.md#emulating-numbers)

```python
算术运算符的重载:
            方法名                  运算符和表达式      说明
            __add__(self,rhs)        self + rhs        加法
            __sub__(self,rhs)        self - rhs         减法
            __mul__(self,rhs)        self * rhs         乘法
            __truediv__(self,rhs)   self / rhs          除法
            __floordiv__(self,rhs)  self //rhs          地板除
            __mod__(self,rhs)       self % rhs       取模(求余)
            __pow__(self,rhs)       self **rhs         幂运算
​
__str__(self) 返回字符串化的信息
__repr__(self) 返回字符串的表示方法，一般自定义类中__str__会使用__repr__的内容
```

## Static Method

```text
class Myclass:
    # 实例方法
    def instancemethod(self):
        pass
    # 静态方法
    @staticmethod
    def staticmethod():
        pass
    # 类方法
    @classmethod
    def classmethod(self):
        pass
```

## keyword: del

目前只知道作用在变量上，相当于解除引用

