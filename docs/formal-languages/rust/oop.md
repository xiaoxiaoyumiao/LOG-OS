# OOP

#### 结构体

```
struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}
```

定义一个结构体实例（rust只允许整体可变或不可变）：

```
let user1 = User {
    email: String::from("someone@example.com"),
    username: String::from("someusername123"),
    active: true,
    sign_in_count: 1,
}; // immutable
let mut user1 = User {
    email: String::from("someone@example.com"),
    username: String::from("someusername123"),
    active: true,
    sign_in_count: 1,
}; // mutable
```

当使用某个变量初始化结构体的某个域，且这个变量的名字和这个域的名字一样时，初始化可以省略域的名字：

```
User {
    email,
    username,
    active: true,
    sign_in_count: 1,
}
```

从已有的一个结构体创建新结构体，可以使用如下的update语法：

```
let user2 = User {
    email: String::from("another@example.com"),
    username: String::from("anotherusername567"),
    ..user1
};
```

可以创建域操作类似于tuple的tuple struct（相当于一个定义了类名的tuple）：

```
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

let black = Color(0, 0, 0);
let origin = Point(0, 0, 0);
```

结构体允许被定义为不含任何域。

结构体可以包含类型为引用的域，但需要借助lifetime机制。

可以使用`println!`打印结构体，但需要使用`{:?}`或者`{:#?}`格式化，并在结构体定义前面添加一行`#[derive(Debug)]`.

```
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 is {:?}", rect1);
}
```

#### 方法

关键字为`impl`：

```
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}
```

方法的第一个参数一定是self，它可以让出所有权、给出可变引用或不可变引用（`self`,`&self`,`&mut self`）

如果不带上self参数就是关联函数（associated function），类似于C的静态函数：

```
impl Rectangle {
    fn square(size: u32) -> Rectangle {
        Rectangle {
            width: size,
            height: size,
        }
    }
}
```

调用时用双冒号，如`Rectangle::square(3)`.

同一个类的方法可以定义在多个`impl`块里。

#### enum枚举

最简单的形式：

```
enum IpAddrKind {
    V4,
    V6,
}
```

使用`IpAddrKind::V4`取值。

枚举变量可以被定义为和某类数据具有绑定关系：

```
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

enum IpAddr {
    V4(String),
    V6(String),
}

let home = IpAddr::V4(String::from("127.0.0.1"));
```

甚至枚举类型也可以定义方法，如对上面的Message：

```
impl Message {
	fn call(&self) {
		// method body would be defined here
	}
}
```

#### Option

特殊且常用的模板类：

```
enum Option<T> {
    Some(T),
    None,
}
```

编译器不会把Option类型自动转换为T类型。

枚举类需要使用match语法来处理。

#### match，pattern & if let

```
match expression {
	pattern => instructions,
	pattern => {
		instructions;
	}
}
```

一个match表达式实例：

```
match coin {
    Coin::Penny => {
        println!("Lucky penny!");
        1
    }
    Coin::Nickel => 5,
    Coin::Dime => 10,
    Coin::Quarter => 25,
}
```

为了提取枚举表达式中的数据，需要用到pattern语法：

```
#[derive(Debug)] // so we can inspect the state in a minute
enum UsState {
    Alabama,
    Alaska,
    // --snip--
}
enum Coin {
    Penny,
    Quarter(UsState),
}
match coin {
    Coin::Penny => 1,
    Coin::Quarter(state) => {
        println!("State quarter from {:?}!", state);
        25
    }
}
```

利用match和pattern可以完成对Option的处理：

```
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(i) => Some(i + 1),
    }
}

let five = Some(5);
let six = plus_one(five);
let none = plus_one(None);
```

match语句中可以使用`_`作为一个default分支：

```
let some_u8_value = Some(0u8);
match some_u8_value {
    Some(3) => println!("three"),
    _ => (), // ()表示什么都不做
}
```

上面的语句也可以用如下的`if let`代替：

```
if let Some(3) = some_u8_value {
    println!("three");
}
```

`if let`有一个备选的`else`分支：

```
let mut count = 0;
if let Coin::Quarter(state) = coin {
    println!("State quarter from {:?}!", state);
} else {
    count += 1;
}
```

#### modules封装

* **Packages:** A Cargo feature that lets you build, test, and share crates
* **Crates:** A tree of modules that produces a library or executable
* **Modules** and **use:** Let you control the organization, scope, and privacy of paths
* **Paths:** A way of naming an item, such as a struct, function, or module

#### 容器

**Vector**

```
let data =Vec::new();
let data:Vec<i32> =Vec::new();
let vec = vec![1,2,3];
let vec:Vec<i32> =vec![1,2,3];
let v = vec![0; 10]; // 10个0
v.push(3);
let val = v.pop();
let num = v[2]; // Supported by implementing Index & IndexMut traits
```

### 异常处理

#### expect

```
result.expect("error info");

match result {
    Ok(num) => num,
    Err(_) => continue, // _算是一个哑变量，可以捕捉任何值
}
```

#### assert断言

```
assert_eq!()
assert!()
```

