# Basics

### Basics

#### 编译和运行工具

```
# 单文件编译方法：rustc [filename]
```

cargo创建新项目目录：

```
PS cargo new [dir_name]  Created binary (application) [dir_name] package
```

目录会自动git仓库化，其中包含一个src文件夹和一个toml文件，src目录下有一个main.rs文件。使用`cargo new --vcs=git`似乎可以避免初始化为git仓库。

TOML文件使用的是专用的TOML格式，用来描述cargo的配置选项。初始有\[package]和\[dependencies]两个段，package段包含对当前包的信息描述，dependencies段包含这个包的依赖。Rust把包称为`crates`。

src目录用来包含所有的代码文件。

构建运行cargo项目（假设项目名为hello\_cargo）：

```
# 目标hello_cargo构建到target/debug/中
PS cargo build  
Compiling hello_cargo v0.1.0 (DIRECTORY\hello_cargo)    
Finished dev [unoptimized + debuginfo] target(s) in 0.56s    

# 一条龙构建运行
PS cargo run 

# 检查可编译性但不生成可执行文件
PS cargo check 

# 构建release文件到target/release/中
PS cargo build --release
```

[https://learnku.com/rust/t/39451](https://learnku.com/rust/t/39451)

VSCODE中安装一个RUST扩展即可，在设置中修改rust-client.channel为stable；设置editor.formatOnSave为true可以在保存时格式化代码（有rust-fmt的话）

```
cargo doc --open
```

#### Hello world

```
// use相当于import，如果没有这一句，下面使用io函数的时候就得写成std::io::[somefunc]，这一点和C类似
// 语句statement应当以分号(;)结尾
use std::io;​
// main函数的写法：
fn main(){    
    // 函数和宏：名字结尾带一个感叹号的是宏(Rust macro)    
    // 字符串："something"表示了一个内容为something的字符串对象    
    println!("hello world");        
    // let关键字声明一个variable，其名字为foo，并被绑定到值5上，且不可修改（immutable）
    let foo1 = 5;    
    // 使用mut关键字声明一个可修改的variable    
    let mut foo2 = 3;        
    // String::new是一般意义上的构造函数，返回一个String类型的实例    
    // ::表明new是String的associated function（类似静态函数）    
    // String是可修改的UTF-8文本    
    let mut guess = String::new();        
    // io函数，返回std::io::Stdin实例
    io::stdin()        
        // 此处传参&表示传引用，mut表示是可变变量        
        // 返回io::Result描述结果，是enum变量，可以取值Ok或者Err        
        .read_line(&mut guess)
        // io::Result的expect方法，调用expect会在取值为Err时crash掉并打印传入的错误信息。
        // 这里不调用的话会被编译器警告        
        .expect("Readln failed");
    // 字符串格式化：println!使用格式化输出    
    println!("You guessed: {}", guess);
}​​
```

引用外部crate时，需要修改toml文件中的\[dependency]段。例如我们需要生成随机数，要用到`rand` crate，于是我们在toml文件中添加：

```
[dependencies]rand = "0.5.5"
```

然后执行构建，cargo就会拉取兼容的crates。一旦拉取，cargo不会主动再更新，要把依赖更新到最新版本，需要执行更新指令：

```
cargo update
```

然后可以使用随机数生成：

```
use rand::Rng;
```

这里的`Rng`是一个**trait**，定义了随机数生成相关的方法。

rust允许将同一个变量名多次绑定到不同类型的值上去（类似python），称为**shadow**。

显式指定变量类型的方法为`let [varname]: [typename] = [value];`

#### 可变性mutability

```
let x = 5; 
// 默认变量是不可变的。constant的规定更严格一些：const MAX_POINTS : u32 = 100;
```

#### shadowing

重复使用 let 以同一变量名创建变量时，新变量覆盖旧变量（或者说该变量名被绑定到了新值上），这种覆盖称为 shadowing。（python 支持类似的机制）shadowing 会随着新变量的销毁（如程序退出新变量的 scope）而失效，此时该变量名将重新绑定到旧值。

```
let x = 5;
let x = x + 1;
```

shadow 机制中，同一变量名可以绑定到不同的值类型。而通过将变量声明为 mut 以能够修改其值时，变量的类型是无法改变的。

#### ownership

* Each value in Rust has a variable that’s called its _owner_.
* There can only be one owner at a time.
* When the owner goes out of scope, the value will be dropped.

超出作用域scope的变量拥有的内存会直接被drop掉。下面讨论各种情况：

```
// 5 是一个栈上的基本类型（见下讨论），y 会直接从 x 拷贝这个值，栈上有两个 5
let x = 5;
let y = x;​
// 由于 String 的内容放在堆中，所以s2获得的是指向堆上内容的指针；
// 同时，为了保证退出作用域时不发生double-free，
// s1 对堆上内容的所有权失效，读 s1 会 CE。
// 这个过程相当于一次 move
let s1 = String::from("what");
let s2 = s1;​
// 为了做深拷贝，必须调用 clone 方法
let s1 = String::from("what");
let s2 = s1.clone();
```

有drop trait的变量无法附加copy trait。

函数传参和返回值时发生的事情类似。

但大多数时候我们希望变量把值传给函数后还能继续使用，如果让函数在返回值时再把所有权通过赋值退回来就太麻烦了。因此 rust 设计了 reference 机制。创建一个 reference 的过程称为 borrowing。

```
// 引用类型的参数
fn func_name(s: &String) -> usize {
    s.len()
}

fn main() {
    let s1 = String::from("what");
    let len = func_name(&s1); // 传引用
}
```

为此带来的代价是，borrow来的值默认无法被修改（immutable）。为了能够修改参数，需要把parameter和argument声明为mut的。

```
fn main() {
    let mut s = String::from("hello");

    change(&mut s);
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}
```

可变引用有一些奇怪的规则：

* 同一块数据在任一时刻最多只能有一个可变引用（持有者本身不算）
  * 如果一个可变引用被销毁了，那之后就可以创建新的可变引用
* 同一块数据在任一时刻不能同时拥有可变和不可变的引用
* 同一块数据可以拥有多个不可变引用

#### 基本类型

基本类型分为**scalar**和**compound**。这些类型都是在栈上分配的。

有copy trait的类型有所有scalar和tuple。

scalar包括：

* 整数值（i32, u32等，i表示有符号，u表示无符号，后面的数字表示位数；特别地`isize`和`usize`的宽度取决于机器架构）
  * ```
    // 类型转换：
    let i: usize = 1;
    a = i as i32;
    ```
  *
* 浮点（f64, f32，默认f64）
* 布尔值（`true`,`false`）
* 字符（rust的字符是unicode编码，4字节宽）

compound包括：

* tuple
  * 使用圆括号括起多个类型，长度不可变：
  * 可以被**destructure**，拆到多个变量，这个语法类似于python
  * 还可以用点号来索引tuple的元素
  * 这两种复值方法都不会破坏tuple本身，应该是相当于把值拷贝出来了
  * ```
    let tup: (i32, f64) = (50, 0.1);
    let (x, y) = tup;
    let tup: (i32, f64) = (50, 0.1);
    let x = tup.0;
    let y = tup.1;
    ```
* array
  * 使用方括号扩起多个相同类型的值，长度不可变；可变的是vector
  * 数组元素用方括号索引，运行时越界访问会抛出out of bounds异常
  * 循环遍历数组带来的索引合法性检查会影响性能，因此推荐的是使用iter()方法遍历。参见控制流部分。
  * ```
    let a = [1,2,3];
    let a: [i32; 3] = [1,2,3]; // 声明数组类型
    let a = [3; 5]; // 含有5个3的数组
    let ele = a[0];
    ```
  * 数组可以切片（slice），可参考字符串一节，其类型为`&[EleType]`，切片语法同字符串

#### 基本运算符

```
1 + 1
1 - 1
1 * 1
1 / 2
1 % 2
1 == 0
1 != 0
```

#### 函数

rust习惯使用snake case命名函数，即小写加下划线分隔

使用fn关键字可以定义一个函数。函数定义位置的先后不影响调用（和C不同）

严格来说parameter是函数参数，而argument是传入的实际值，不过实际常混用。rust的函数定义方式：

```
fn func_name(x: i32, y: i32) -> i32 {
	x + y
} // 返回x+y
```

return语句依然可以使用，一般用于提前返回。

#### statement和expression

函数定义、变量赋值等都属于statement；

除了一般意义上的表达式外，{ }也是一个表达式。

```
let y = {
	let x = 3;
	x + 1
};
```

#### 控制流

if表达式（注意是一个表达式expression）实现一个条件分支，条件表达式不需要加括号，其返回值必须是bool变量（而不能是int之类）。

```
if num < 5 {

} else if {
    
} else {

}

// 条件表达式每个分支的返回值（如果返回了）必须是相同类型，否则CE
let number = if cond { 1 } else { 2 };
```

loop表达式实现一个无限循环。

```
loop {
	instructions;
}
```

使用`break`可以跳出循环，还可以顺带返回值：

```
loop {
	instructions;
	break 1; // return 1
}
```

while结构也是有的：

```
while cond {
	instructions;
}
```

for循环遍历区间：

```
// 1..4是(1..4)的略写（会被编译器提示省略圆括号……），(1..4) 是一个Range类型的实例，左闭右开。这里迭代变量num是不用预先声明的
for num in 1..4 {

}

// 反向遍历
for num in (1..4).rev() {
    
}
```

for循环可以用来在一个集合结构上迭代，这种迭代比较快速而安全：

```
let a = [1,2,3];
for ele in a.iter() {
	// ...
}
```

match语句类似C的switch，将表达式的结果和每个分支的pattern比较。（表达式的括号并不是必要的）

```
match expression {
	pattern => instructions,
	pattern => {
		instructions;
	}
}
```

关于match的介绍详见 OOP - match，pattern & if let.

### Math

#### 随机数

```
use rand::Rng;

let number = rand::thread_rng().gen_range(1,101);
// 参数代表区间，左闭右开
```

#### 比较

```
use std::cmp::Ordering;

match num1.cmp(&num2) {
	Ordering::Less => [some instructions],
    Ordering::Greater => [],
    Ordering::Equal => [],
}
```

###
