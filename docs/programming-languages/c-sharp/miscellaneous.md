# Miscellaneous

## Right Bit Shift (`>>`)

若左操作数类型为 int 或 long，则作算数移位，即使用原数符号位（最高位）填充移位后的空余高位；若左操作数类型为 uint 或 ulong，则作逻辑移位，即使用 0 填充移位后的空余高位。

```
int a = int.MinValue;
int b = a >> 3;
// Before: 10000000000000000000000000000000
// After:  11110000000000000000000000000000

uint c = 0b_1000_0000_0000_0000_0000_0000_0000_0000;
uint d = c >> 3;
// Before: 10000000000000000000000000000000
// After:  00010000000000000000000000000000
```

ref:  [Bitwise and shift operators - C# reference | Microsoft Docs](https://github.com/deemolover/LOG.OS/tree/edf5bd6c0c47ffa5692978295b8e9304f51837c4/en-us/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators/README.md#right-shift-operator-)

## Using COM Port

Use `SerialPort` class.

ref: [https://docs.microsoft.com/en-us/dotnet/api/system.io.ports.serialport?view=dotnet-plat-ext-5.0](https://docs.microsoft.com/en-us/dotnet/api/system.io.ports.serialport?view=dotnet-plat-ext-5.0)

## Preprocessor Directives

* C# 的预处理机制并不强大，可以使用的如 if else endif 等条件判断以及逻辑运算符。
* 与 C 中 #ifdef 等效的是 #if，用于判断一个 symbol 是否被 #define 定义过。
* [https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/preprocessor-directives](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/preprocessor-directives)

## Null-Conditional Operator (`?.`, `?[]`)
* `x?.y` 的逻辑为：当 x 为空对象时，该表达式的值为空；否则正常返回 `x.y` 的值。算是一个简单的语法糖。
* [https://stackoverflow.com/questions/37851873/what-does-mean-after-variable-in-c/37852031](https://stackoverflow.com/questions/37851873/what-does-mean-after-variable-in-c/37852031)

## Generic Class
* This is analogous to the templates in C++.
* [https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/generic-classes](https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/generic-classes)

## Switch Fall-through
* 使用 or 语句或使用空的过程。 [https://stackoverflow.com/questions/848472/how-add-or-in-switch-statements](https://stackoverflow.com/questions/848472/how-add-or-in-switch-statements)
* 更高级的写法：[https://stackoverflow.com/questions/56676260/c-sharp-8-switch-expression-with-multiple-cases-with-same-result](https://stackoverflow.com/questions/56676260/c-sharp-8-switch-expression-with-multiple-cases-with-same-result)

## Lambda Expression
* **expression lambda** looks like this: `(input-parameters) => expression` 
* **statement lambda** looks like this:  `(input-parameters) => { <sequence-of-statements> }` 
* > If a lambda expression doesn't return a value, it can be converted to one of the `Action` delegate types; otherwise, it can be converted to one of the `Func` delegate types.
* ref: [https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions)

## Method Invoke

- delegate 类型的对象可以通过其 Invoke 方法被调用，而直接调用其自身的写法算是一种语法糖，它们编译结果相同。使用 Invoke 的一种好处是可以通过 `?.` 语法判空。
- ref: https://stackoverflow.com/questions/7907067/difference-between-actionarg-and-action-invokearg

```
    Action<string> x = Console.WriteLine;
    x("1");
```

## `=>` for Expression Body Definition

C# 存在一种简化 property 书写的语法糖，称作 expression bodied member. 这种语法也可以用来定义 method。

(C# 6) `PropertyType PropertyName => expression;` 定义了一个只读的 property。

(C# 7)  更一般的语法糖：

```c#
      public string Name
      {
          get => locationName;
          set => locationName = value;
      }
```

ref:
    - https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/statements-expressions-operators/expression-bodied-members
    - https://stackoverflow.com/questions/36372457/lambda-for-getter-and-setter-of-property
    - https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-operator

## Custom Sorting

```c#
    List<Order> SortedList = objList.Sort((x, y) => x.OrderKey.CompareTo(y.OrderKey));
```

- 这里 `OrderKey` 成员已经是可比较的，因此可以直接使用其 `CompareTo` 方法。

ref: https://stackoverflow.com/questions/3309188/how-to-sort-a-listt-by-a-property-in-the-object

## IEnumerable，IEnumerator & Coroutines
ref: 
    - https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/iterators
    - https://docs.microsoft.com/en-us/dotnet/api/system.collections.ienumerator?view=net-6.0