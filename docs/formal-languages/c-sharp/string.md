## String Formatting

ref: [https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings?redirectedfrom=MSDN#standard-format-specifiers](https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings?redirectedfrom=MSDN#standard-format-specifiers)

## String Comparison

```
string.Equals(val, "astringvalue", StringComparison.OrdinalIgnoreCase)
```

ref: [https://stackoverflow.com/questions/6371150/comparing-two-strings-ignoring-case-in-c-sharp](https://stackoverflow.com/questions/6371150/comparing-two-strings-ignoring-case-in-c-sharp)

## Splitting Strings

Use `Split` . For example, `str.Split(' ')` splits string `str` by space.

ref: [https://docs.microsoft.com/en-us/dotnet/api/system.string.split?view=net-6.0](https://docs.microsoft.com/en-us/dotnet/api/system.string.split?view=net-6.0)

## StringBuilder

Construct strings more efficiently (in cases like you have a bunch of strings to concatenate).

ref: [https://docs.microsoft.com/en-us/dotnet/api/system.text.stringbuilder?view=net-6.0](https://docs.microsoft.com/en-us/dotnet/api/system.text.stringbuilder?view=net-6.0)

## Using Byte Arrays

使用 BitConverter 类可以把 byte array 对象（用十六进制表示）打印出来。

使用 Encoding.UTF8.GetString(array) 可以把 byte array 对象按 UTF8 编码转换为字符串。

## Enum from/to Strings

使用 `Enum.Parse(EnumClass, enumObjectName)` 来将字符串 `enumObjectName` 解析为同名的枚举值。从枚举值到字符串则直接使用 ToString 即可。

[https://docs.microsoft.com/en-us/dotnet/api/system.enum.parse?view=net-6.0](https://docs.microsoft.com/en-us/dotnet/api/system.enum.parse?view=net-6.0)