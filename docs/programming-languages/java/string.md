# String

* `String`
* `StringBuffer` 
* `StringBuilder`

```text
/** 字符串操作 */
String a = "test";
String b = a.substring(0,2);//取子串，左闭右开区间
String c = a+b;//支持连接字符串
//任何Java对象都可以转换为字符串
String d = String.join(seperator,string_A,string_B,...);//Python的join
//字符串修改通过取子串后连接来实现
a.equals(b); //判断字符串a，b是否内容相等，返回bool
a.compareTo(b); //判断相等，返回数值？
//字符串的值可以为null，注意和空串不一样。null串类似空指针，调用方法会出错
str == null
//码点和代码单元：一个字符对应一个码点，但可能对应1或2个代码单元
a.length(); //取代码单元长度
a.codePointCount(0,a.length()); //取码点数量
a.charAt(n); //取索引n的代码单元
int k = a.codePointAt(a.offsetByCodePoints(0,n)); //取索引n的码点
//注意上面这个方法不要大量使用[Facepalm]复杂度会很高
a.trim() //strip
a.toLowerCase()
a.toUpperCase()
//格式化生成字符串：
String a = String.format(format,a,b,...);
StringBuilder s = new StringBuilder(str); //用于高效字符串运算的类，主要方法有：
//把缓冲区内容转化为字符串输出
s.toString();
//把串压入缓冲区
s.append(String str)
s.append(char c)
//把缓冲区内容反转
s.reverse();
//在第offset个字符（从0开始计数）之前插入给定字符串或字符
s.insert(int offset,String str)
s.insert(int offset,char c)
//删除子串，左闭右开区间
s.delete(int startIndex,int endIndex)
​
将char转换为String大致有6种方法。总结如下：
​
1. String s = String.valueOf('c'); //效率最高的方法
​
2. String s = String.valueOf(new char[]{'c'}); //将一个char数组转换成String
​
3. String s = Character.toString('c');
// Character.toString(char)方法实际上直接返回String.valueOf(char)
​
4. String s = new Character('c').toString();
​
5. String s = "" + 'c';
// 虽然这个方法很简单，但这是效率最低的方法
// Java中的String Object的值实际上是不可变的，是一个final的变量。
// 所以我们每次对String做出任何改变，都是初始化了一个全新的String Object并将原来的变量指向了这个新String。
// 而Java对使用+运算符处理String相加进行了方法重载。
// 字符串直接相加连接实际上调用了如下方法：
// new StringBuilder().append("").append('c').toString();
​
6. String s = new String(new char[]{'c'});
​
```

## Regular Expressions

参考引用 \[1\]。

```text
import java.util.regex.*;
String content = "some_content";
String pattern = "some_pattern";
isMatch = Pattern.matches(pattern,content);
```

## Template Literals

类似字符串格式化的语法糖，使用反引号可以创建一个 template literal，它能嵌入表达式。

```text
`string text ${expression} string text`
```

## Reference

[\[1\] JAVA 正则表达式实例](https://www.cnblogs.com/hshshs/p/8315904.html)

\[2\] [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template\_literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)

