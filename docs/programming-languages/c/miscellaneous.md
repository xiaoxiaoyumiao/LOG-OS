# Miscellaneous

* 关于右移位运算的规则
  * 若左操作数类型为 int 或 long，则作算数移位，即使用原数符号位（最高位）填充移位后的空余高位；若左操作数类型为 uint 或 ulong，则作逻辑移位，即使用 0 填充移位后的空余高位。
  * ```
    int a = int.MinValue;
    int b = a >> 3;
    // Before: 10000000000000000000000000000000
    // After:  11110000000000000000000000000000

    uint c = 0b_1000_0000_0000_0000_0000_0000_0000_0000;
    uint d = c >> 3;
    // Before: 10000000000000000000000000000000
    // After:  00010000000000000000000000000000
    ```
  * ref:  [Bitwise and shift operators - C# reference | Microsoft Docs](https://github.com/deemolover/LOG.OS/tree/edf5bd6c0c47ffa5692978295b8e9304f51837c4/en-us/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators/README.md#right-shift-operator-)
* 关于字符串格式化的规则
  * ref: [https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings?redirectedfrom=MSDN#standard-format-specifiers](https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings?redirectedfrom=MSDN#standard-format-specifiers)
* 关于字符串比较：（ref: [https://stackoverflow.com/questions/6371150/comparing-two-strings-ignoring-case-in-c-sharp](https://stackoverflow.com/questions/6371150/comparing-two-strings-ignoring-case-in-c-sharp)）

```
string.Equals(val, "astringvalue", StringComparison.OrdinalIgnoreCase)
```

* 关于字符串分割：使用 `Split` 方法。例如 `str.Split(' ')` 按空格分割字符串。
  * ref: [https://docs.microsoft.com/en-us/dotnet/api/system.string.split?view=net-6.0](https://docs.microsoft.com/en-us/dotnet/api/system.string.split?view=net-6.0)
* 关于基本数据类型和 byte array 之间的转换
  * 使用 BitConverter 类可以把 byte array 对象（用十六进制表示）打印出来。
  * 使用 Encoding.UTF8.GetString(array) 可以把 byte array 对象按 UTF8 编码转换为字符串。
* 关于COM 口数据收发
  * 使用 Serial Port 类
  * [https://docs.microsoft.com/en-us/dotnet/api/system.io.ports.serialport?view=dotnet-plat-ext-5.0](https://docs.microsoft.com/en-us/dotnet/api/system.io.ports.serialport?view=dotnet-plat-ext-5.0)
* 关于预处理指令
  * C# 的预处理机制并不强大，可以使用的如 if else endif 等条件判断以及逻辑运算符。
  * 与 C 中 #ifdef 等效的是 #if，用于判断一个 symbol 是否被 #define 定义过。
  * [https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/preprocessor-directives](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/preprocessor-directives)
* 关于 ?. 运算符
  * `x?.y` 的逻辑为：当 x 为空对象时，该表达式的值为空；否则正常返回 `x.y` 的值。算是一个简单的语法糖。
  * [https://stackoverflow.com/questions/37851873/what-does-mean-after-variable-in-c/37852031](https://stackoverflow.com/questions/37851873/what-does-mean-after-variable-in-c/37852031)
* 关于枚举
  * 使用 `Enum.Parse(EnumClass, enumObjectName)` 来将字符串 `enumObjectName` 解析为同名的枚举值。从枚举值到字符串则直接使用 ToString 即可。
  * [https://docs.microsoft.com/en-us/dotnet/api/system.enum.parse?view=net-6.0](https://docs.microsoft.com/en-us/dotnet/api/system.enum.parse?view=net-6.0)
* 关于 StringBuilder
  * 更高效地构建字符串。
  * [https://docs.microsoft.com/en-us/dotnet/api/system.text.stringbuilder?view=net-6.0](https://docs.microsoft.com/en-us/dotnet/api/system.text.stringbuilder?view=net-6.0)
* 关于模板类
  * C# 中叫 Generic class.
  * [https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/generic-classes](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/generic-classes)
* 关于 switch
  * 希望多个 case 使用同一过程：使用 or 语句或使用空的过程。
    * [https://stackoverflow.com/questions/848472/how-add-or-in-switch-statements](https://stackoverflow.com/questions/848472/how-add-or-in-switch-statements)
    * 更高级的写法：[https://stackoverflow.com/questions/56676260/c-sharp-8-switch-expression-with-multiple-cases-with-same-result](https://stackoverflow.com/questions/56676260/c-sharp-8-switch-expression-with-multiple-cases-with-same-result)
* 关于 lambda 表达式
  * `(input-parameters) => expression` 为一个 expression lambda
  * `(input-parameters) => { <sequence-of-statements> }` 为一个 statement lambda
  * > If a lambda expression doesn't return a value, it can be converted to one of the `Action` delegate types; otherwise, it can be converted to one of the `Func` delegate types.&#x20;
  * ref: [https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions)
