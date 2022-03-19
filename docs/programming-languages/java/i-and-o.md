# I&O

```java
/**
 IO
*/
//构造Scanner，绑定到标准输入流用于输入
import java.util.*; //Scanner在util包中
Scanner in = new Scanner(System.in);
String a = in.nextLine();//读取一行
String b = in.next(); //读取到下一个空白符前的单词
int c = in.nextInt(); //读取下一个整数
double d = in.nextDouble();
in.hasNext() //判断是否还有输入
//利用Console类可以实现密码读取
Console cons = System.console();
char[] pwd = cons.readPassword("input pwd: ");
System.out.println(string);//换行输出
System.out.print(string);//不换行输出
System.out.printf(format,a,b,...);//格式化输出
//文件IO:
//文件读取：
Scanner in = new Scanner(fileObject,coding);//fileObject为文件对象，coding为编码方式。如
Scanner in = new Scanner(Paths.get("D:\\myfile.txt","UTF-8"));
//文件输出：
PrintWriter out = new PrintWriter(filePathString,coding);
//获取启动路径：
String dir = System.getProperty("user.dir");
```

