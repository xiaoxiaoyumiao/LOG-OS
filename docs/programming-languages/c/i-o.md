# I/O

## **控制台 IO**

```csharp
string firstStr, secondStr;
​
// 输出内容到控制台
Console.WriteLine("请输入第一个字符串：");
​
// 接收用户输入，为变量赋值
firstStr = Console.ReadLine();
​
// 输出内容到控制台
Console.WriteLine("请输入第二个字符串：");
​
// 接收用户输入，为变量赋值
secondStr = Console.ReadLine();
​
// 输出内容到控制台
Console.WriteLine("你输入的第一个字符串是：{0}；第二个字符串是：{1}",firstStr,secondStr);
```

```csharp
using System.IO;
using System.Text;
```

## **文件 IO**

文件编码方式（UTF-8之类）的参数是System.Text.Encoding。

使用File接口：

[https://www.cnblogs.com/ldyblogs/p/file.html](https://www.cnblogs.com/ldyblogs/p/file.html)

```csharp
FileStream.TextFile=File.Open(@"c:\tempuploads\newFile.txt",FileMode.Append);
　byte [] Info = {(byte)'h',(byte)'e',(byte)'l',(byte)'l',(byte)'o'};
　TextFile.Write(Info,0,Info.Length);
　TextFile.Close();
}
​
File.Exists(filePath) // check if file exists
```

FileStream文件流构造文件读写：

```csharp
byte[] byData = new byte[100];
char[] charData = new char[1000];
public void Read()
{
    try
    {
        FileStream file = new FileStream("E:\\test.txt", FileMode.Open);
        file.Seek(0, SeekOrigin.Begin);
        file.Read(byData, 0, 100); 
        //byData传进来的字节数组,用以接受FileStream对象中的数据,第2个参数是字节数组中开始写入数据的位置,它通常是0,表示从数组的开端文件中向数组写数据,最后一个参数规定从文件读多少字符.
        Decoder d = Encoding.Default.GetDecoder();
        d.GetChars(byData, 0, byData.Length, charData, 0);
        Console.WriteLine(charData);
        file.Close();
    }
    catch (IOException e)
    {
        Console.WriteLine(e.ToString());
    }
}
​
public void Write()
{
    FileStream fs = new FileStream("E:\\ak.txt", FileMode.Create);
    //获得字节数组
    byte[] data = System.Text.Encoding.Default.GetBytes("Hello World!"); 
    //开始写入
    fs.Write(data, 0, data.Length);
    //清空缓冲区、关闭流
    fs.Flush(); // necessary!
    fs.Close();
}
```

直接使用流读写类：

[https://www.cnblogs.com/vaevvaev/p/6804423.html](https://www.cnblogs.com/vaevvaev/p/6804423.html)

```csharp
public void Read(string path)
{
    StreamReader sr = new StreamReader(path,Encoding.Default);
    String line;
    while ((line = sr.ReadLine()) != null) 
    {
        Console.WriteLine(line.ToString());
    }
}
​
public void Write(string path)
{
    FileStream fs = new FileStream(path, FileMode.Create);
    StreamWriter sw = new StreamWriter(fs);
    //开始写入
    sw.Write("Hello World!!!!");
    //清空缓冲区
    sw.Flush();
    //关闭流
    sw.Close();
    fs.Close();
}
```

