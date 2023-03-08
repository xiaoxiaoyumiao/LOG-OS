# Argument Parsing

## **Command Line Arguments**

在执行 python 脚本时，可以为其附加命令行参数。通过 `sys` 模块的 `argv` 可以得到当前程序的命令行参数，它是一个字符串的列表。

例如，将以下代码保存为 `args.py` ：

```python
import sys

args = sys.argv
for arg in args:
    print(arg)
```

然后在脚本所在的目录中运行该脚本，并附加一些参数，例如执行以下 bash 命令：

```python
python args.py echo
# output:
args.py
echo
```

可以看到， 我们在脚本中获取命令行参数并把它的元素依次打印出来。第一个参数是被运行的脚本自身的名称；第二个参数则是我们附加的字符串 `echo` 。

可以尝试在命令后增加更多的输入，并在脚本中处理它们。但如果对命令行参数已经有所了解（例如使用过一些命令行工具或者使用其他语言实现过接收命令行参数的代码），就会知道命令行参数常常遵循一定的格式，并且我们常常需要实现必要的或可选的参数。如果由自己来实现这些解析规则，未免比较繁琐；通过 `argparse` 包可以更方便地实现这些功能。

## **Argument Parser**

### **Positional & Optional Argument**

以下代码使用 argument parser 实现了一个在运行时必须加上 echo 的程序，其运行结果是输出 echo。

```python
import argparse

# Initialize Parser
parser = argparse.ArgumentParser()
parser.add_argument("echo")

# Parse arguments
args = parser.parse_args()
print(args.echo)
```

将以上代码保存为一个 python 文件（例如命名为 `args.py` ），在其所在目录下运行（以 bash 命令行为例）：

```bash
# try to run without 'echo'
python args.py
# output:
usage: args.py [-h] echo
args.py: error: too few arguments

# run with 'echo'
python args.py echo
# output:
echo
```

回来看这段 python 脚本。它首先构造了一个 `ArgumentParser` 实例，然后通过 `add_argument` 方法向这个实例添加了一个参数定义。`echo` 是我们定义的参数的名字，同时表示这个参数仅接收一个字符串 `echo` 作为值。完成参数定义后，我们调用 `parse_args` 让 parser 解析这个程序接收的命令行参数。注意我们在执行这个程序时，附加了字符串 `echo` 。parser 正确接收到这个参数后，把参数的值存储到解析结果 `args` 中并返回，于是我们可以通过 `args.echo` 访问到这个参数的值。

这里的 echo 是一个 positional argument，这类参数是通过在参数列表中的位置传递值的。 在这个例子中，如果附加的参数列表的第一项不是 `echo` ，那么 parser 就会报错。

与之相对的是 optional argument。这类参数是通过指定的名字传递值。例如对上面的代码做如下拓展：

```python
import argparse

# Initialize Parser
parser = argparse.ArgumentParser()
parser.add_argument("echo",)
parser.add_argument("--count", type=int, default=1)

# Parse arguments
args = parser.parse_args()
for i in range(0, args.count):
    print(args.echo)
```

我们增加了一个参数定义，并赋予了名字 `count` 。但注意这一次它的名字有一个 `--` 前缀，这代表它是一个 optional argument。我们同时在定义中添加了 `type=int` 和 `default=1` 两项配置，前者代表这个参数的值应当被解析为 int，后者代表这个参数具有一个默认值 1。在解析参数后，我们把 count 参数的值作为打印 echo 的次数。

尝试在命令行中执行：

```bash
python args.py echo
# output
echo

python args.py echo --count 2
# output
echo
echo

python args.py --count 2 echo
# output
echo
echo
```

我们在命令后增加了 `--count` （也被称为一个 flag），并在其后紧跟一个数字 2，表明我们希望把 2 传递给 `count` 这个参数。当我们不这样做时，`count` 的值默认为 1，echo 只打印一次。此外可以注意到，因为 `count` 参数的值完全通过名字传递，它在命令中的位置事实上并不会影响 `echo` 的解析。也就是说，positional argument 的解析只依赖于所有 positional argument 的相对位置。parser 将遇到的第一个可解析为 positional argument 的字符串与第一个 positional argument 对照，以此类推。

### Common Usage

接下来讨论如何在 `add_argument` 中进行配置以定义出各种各样的命令行参数。

为方便查阅，首先列出方法原型和可接收的各个参数如下：

```python
ArgumentParser.add_argument(name or flags...[, action]
        [, nargs][, const][, default][, type][, choices]
        [, required][, help][, metavar][, dest])

name or flags - 选项字符串的名字或者列表，例如foo 或者-f, --foo。
action - 在命令行遇到该参数时采取的基本动作类型。
    store_const(使用该选项时赋值为const声明的值)
    store_true(常用于布尔类型，使用该选项时生效，即默认为False)
    store_false
nargs - 应该读取的命令行参数数目。
const - 某些action和nargs选项要求的常数值。
default - 如果命令行中没有出现该参数时的默认值。
type - 命令行参数应该被转换成的类型。
choices - 一个包含参数合法值的 container。
required - 该命令行选项是否可以省略（只针对可选参数）。
help - 参数的简短描述。一个字符串，-h的时候显示。甚至支持把其他参数格式化输出，如
    default=42, help="default: %(default)s"
metavar - 参数在帮助信息中的名字。
dest - 给parse_args()返回的对象要添加的属性名称。
```

接下来列出各种参数特征的实现方法。

首先，可以为 optional argument 指定多个在传参时使用的 flag。

```python
parser.add_argument("--count", "--times", "-c", type=int, default=1)
```

在命令行中就可以通过 `python args.py --times 2 echo` 或者 `python args.py -c 2 echo` 来传值。但注意，只有提供的第一个以 `--` 开头的 flag 会被用作参数的名称（也就是成为 args 的一个属性）。当没有以 `--` 开头的 flag 时，会使用第一个以 `-` 开头的 flag。可选参数的 flag 必须以 `-` 开头。

然后，虽然 optional argument 听起来是 optional 的，但可以通过 required 参数把它变成强制的：

```python
parser.add_argument("--count", type=int, default=1, required=True)
```

在命令行中执行：

```python
python args.py echo
# output
usage: args.py [-h] --count COUNT echo
args.py: error: argument --count is required
```

Optional argument 的值默认存储在返回的 args 的同名属性中，但这个属性的名称其实可以通过 dest 参数另外定义：

```python
# define a destination named "times"
parser.add_argument("--count", dest="times", type=int, default=1)
# Parse arguments
args = parser.parse_args()
# access "times" property
for i in range(0, args.times):
    print(args.echo)
```

有时我们只希望通过 optional argument 的 flag 存在与否来传递布尔类型的信息，但上面的定义方法要求 flag 后面必须跟随一个值。通过 action 参数可以实现这种无需显式传值的 optional argument：

```python
# store true as value when --log is present
parser.add_argument("--log", action="store_true")
# Parse arguments
args = parser.parse_args()
if args.log:
    print(args.echo)
```

通过把 `action` 取为 `store_const` 和配置 `const` 参数则可以 0-1 地为选项赋数值而非布尔值。

在前面的例子中 positional argument 的值和其名字一致，但其传参时的合法值其实是可以另定义的。通过 choices 可以提供一个合法值的集合。

```python
parser.add_argument("echo", choices=["hello", "echo"])
# Parse arguments
args = parser.parse_args()
print(args.echo)
```

此时运行 `python args.py hello` 会得到 `hello` 输出。

最后，parser 还提供了 help 这一方便的功能。在运行时附带一个 `-h` 或者 `--help` 参数，parser 就会打印出它定义的各参数的使用方法。它看起来大概是这样：

```bash
python args.py -h
usage: args.py [-h] echo

positional arguments:
  echo

optional arguments:
  -h, --help  show this help message and exit
```

在 `add_argument` 中使用 `metavar` 和 `help` 配置可以让参数在帮助信息中看起来更漂亮。

```python
parser.add_argument("echo", metavar="greeting", 
        choices=["hello", "echo"], help="Echo things.")
# Parse arguments
args = parser.parse_args()
print(args.echo)
```

帮助信息如下：

```bash
usage: args.py [-h] greeting

positional arguments:
  greeting    Echo things.

optional arguments:
  -h, --help  show this help message and exit
```

## Reference

\[1\] [https://docs.python.org/3/library/argparse.html\#module-argparse](https://docs.python.org/3/library/argparse.html#module-argparse)

