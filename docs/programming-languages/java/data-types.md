# Data Types

## primitive type

### Numbers

* 整型：
  * long \(8 Byte\)
  * int \(4 Byte\)
  * short \(2 Byte\)
  * byte \(1 Byte\)
* 长整型以 L 或 l 结尾，十六进制0x开头，八进制0开头，二进制0b或0B开头 
* 数字内部可以用下划线分隔提升易读性 
* Java没有 unsigned 类型
* 浮点类型：
  * float \(4 Byte\)
  * double \(8 Byte\) 
* float 类型以 F 或 f 结尾 
* 非数值：
  * 正无穷大 `Double.POSITIVE_INFINITY`
  * 负无穷大 `Double.NEGATIVE_INFINITY`
  * 非数 `Double.NaN` 
  * 判断非数的方法：`Double.isNaN(x)` 
* 尽量不要使用 char 类型（暂未考证此说法，可能是因为和 C/C++ 中 char 概念的不一致）
* `boolean`（`true`, `false`）不能和整型相互转换

**隐式的类型转换的时候如果出现信息损失，JAVA会报错，因此必须加上强制类型转换**

### Math

```java
/**
Math类的数学函数
可以用import static java.lang.Math.*;全部导入
*/
Math.sqrt(x);
Math.pow(x,a);
Math.floorMod(a,b);//得到一个非负a mod b结果
//Math类包含常用三角函数、指对数函数
Math.PI
Math.E
BigInteger BigDecimal //math包的精确大数计算
/**
运算符
*/
int x = 0;
x += 3.5;//等效为x = (int)(x+3.5)
​
```

### Enumerate

```java
public enum Size {A,B,C,D}
Size.A.toString() // 返回枚举常量名 A
Enum.valueOf(Size.class, "A") // 获取枚举值本身 
Size.values() // 返回所有枚举量构成的数组
```

### Declaration

```java
//变量声明同C，声明后需要显式赋值初始化
//没有声明和定义的区分
int sum;
sum = 0;
int res = 12;
//final声明一个常量
//static把常量设定为类常量
//public把常量设定为c从类外可访问
final int LEN = 8;
```

## Reference

每个引用占据32位的内存空间，指向对象所在的内存的位置。

```text
Object d = new Object();
```

## Arrays

```text
/** 数组 */
int[] a;//定义
int a[];//定义
int[] a = new int[10];//int用0填充，bool用false填充，Obj用null填充
a = new int[] {1,2,3,4,5};//用匿名数组赋值
int[][] d = new int[MAX][MAX];//多维数组
Array.sort(a);//排序方法
//a.length 可以获取数组长度
int[] b = a;//相当于指针拷贝
int[] c = Arrays.copyOf(a,newLength);//内容拷贝
Arrays.toString(a)//数组打印
```

