# Miscellaneous

### 关于javadoc

使用`/** ... */`可以生成文档。 需要注释的地方：

* 包（需要在包的目录中添加一个单独的文件package-info.java（仅由注释构成）或者package.html（由`<body></body>`构成）
* 公有类和接口
* 公有和受保护的域和方法

```text
/**
 * @param 方法参数描述
 * @return 返回值描述
 * @throws 异常类描述
 * 可以在注释中运用HTML语法。特别地，代码块用{@code }
 * @see 引用 可以制造一个指向某个类/方法/域的超链接，
 *      如see packagename.classname#methodname(argnames)
 *      当然也可以是一个<a ></a>超链接
 */
```

最后，运行命令： javadoc -d docDirectory nameOfPackage

### 多文件编译

直接编译包含main的文件即可，java会自动查找用到的类的.class文件 方法可以访问该类所有成员的私有field

### 关于final

类中的final修饰的field：必须在构造函数中初始化并且之后不能再修改的变量 注意：对于可变类的field，被final修饰只表示其不会再指向其他对象，其内容仍然可以更改

### 关于private，public和不标记

在完全不标记的情况下，field是包可见的，包中的所有方法都可以访问； public意味着任何类都可以使用； private意味着只有定义它的类可以使用；

### 关于main函数

每个类都可以有一个main方法（注意用public static void修饰），这可以用于单元测试。运行 java ClassName 就可以单独运行这个类ClassName中的main函数的内容。

### 关于传参

* java 是 call by value
* 方法参数会覆盖实例同名field。

### 关于构造器

在构造函数第一行调用this\(...\)将会调用相应的另一个构造函数。 这样的构造函数必须写在首行 可以用初始化块{}来对部分field初始化，它会在构造函数调用前执行。

### 关于package和import

和python机制类似，import之后就不需要写出包名 java编译器可以查看文件的内部，所以和c的include有着微妙的不同 利用代码最开头的语句 package packagepath.packagename; 可以把本文件中定义的类放到名为packagename的包里。否则，它被放在default package包中。要注意定义的包名和文件目录之间的一致性，并且从根目录编译运行目标文件： javac packagepath/packagename/classname.java java packagepath.packagename.classname

### 关于Wrapper包装器

不可变final，包装基础类型 定义arraylist不能使用基础类型，因此应当使用wrapper如 \`ArrayList&lt;Integer&gt; list = new ArrayList&lt;&gt;\(\);' 这种情形下调用add的时候，会把基本类型参数自动装箱为wrapper；查询操作时则会自动拆箱 wrapper类还包含了很多有用的静态方法

### 关于可变参数方法

printf\(String format, Object... args\) 可以传一个Object\[\]给最后一个参数

### 关于Class类

任一类型T.class会返回其对应的Class类对象，Class类描述这个类型

### 关于异常处理

System.gc\(\) 建议JVM进行垃圾收集 除零错误是运行时错误，编译可通过，运行时抛出ArithmeticException类 catch异常：寻找能处理异常的代码 Throwable： Error + Exception try{}包裹代码块，伴随catch语句，finally的代码必然会执行 如果一个方法不知道怎么处理这个异常，就应该声明抛出异常throws exception{}，交给调用这个方法的函数来解决

### 流

数据从硬盘存储空间流向jAVA中的内存地址

字节流和字符流的概念

IOstream字节流 IOstreamReader/Writer java.io包的字符流，用于字节转字符；和别的流对接需要管道 unsupportedEncodingException 不支持的编码格式 BufferedReader 带缓冲，此时可以操作

### 串行化

把内存中的状态存储于硬盘或者发送给其他电脑 需要实现Serializable接口

### 课间随笔

面向对象：封装，继承，多态 主动对象：Java中含有main方法的对象。它是一组属性和一组服务的封装体，其中的主动服务可以主动执行 final class 不可被继承 abstract class 抽象类 extends superclassName 继承\[superclassnName\]父类（Java不能继承多个父类） 所有类默认继承OBJECT native 调用其他语言的代码 this\(0,0\)调其他构造函数的构造函数要放在第一行？ super\(\)放在子类构造函数的第一句，构造父类

静态方法可以用来实现工厂模式 main函数是静态的 允许在声明成员变量的时候就对其赋值

事件适配器模式 抽象方法（abstract）不能有方法体！ 含抽象方法的类必然为抽象类，抽象类不能被实例化

## OOP：接口

Arrays.sort\(\)可以对implements Comparable的类的数组排序。 基本类型比较的方法：Integer.compare, Double.compare（返回值为1，0，-1，可以避免舍入带来的错误）

```text
public ClassName implements InterfaceName {
    //实现接口的所有方法，并声明为public
    public ReturnValue interfaceMethod(Args){
        //...
    }
}
//不能new接口实例，但可以创建接口变量，然后引用实现了接口的类对象
InterfaceName x = new ClassName(...);
//接口可以继承接口
public interface B extends A {...}
//接口不能包含实例域，但可以包含常量，并缺省public static final；高版本支持定义简单的静态方法，不过更加建议定义一个接口专用的伴随类
//可以在接口里写一个方法的默认实现default，这样继承者就不需要把所有方法实现一遍：
public interface IntName{
    default int methodName(Args){...}
}//这种方法还可以解决类定义跟不上接口更新的情景
//一个类可以继承复数个接口
class ClassName implements A,B,C {...}
//两个接口的默认方法冲突的情况下，规定必须重写；但如果超类中已有实现，超类的版本会覆盖接口的版本
```

## OOP：泛型

## 实践：多线程

## 实践：网络编程

IP地址：32位，4个字节 主机名hostname+端口号port number 服务类型service：http，ftp，……

### 传输协议

TCP： 面向连接，可靠 相应类：URL，URLConenction，Socket，ServerSocket UDP：不可靠的数据包式数据传输 相应类：DatagramPacket，DatagramSocket，MulitcastSocket

## 实践：WEB编程

安装tomcat HttpServlet类，开发：重写doGet\(\),doPost\(\),doPut\(\),doDelete\(\) 需要修改web.xml

HTTP session, Cookie ServletConfig 保存servlet的配置信息

forms： &lt;% any java code %&gt;; [jsp:scriptlet?&lt;/jsp:scriptlet](jsp:scriptlet?%3C/jsp:scriptlet) expression: &lt;%= expr %&gt; declaration:&lt;! declare %&gt;

### MVC design pattern

Model+View+Controller

