# IO & String

### IO

```
use std::io;

// read_line会读入整行字符串，并保留行末的换行符
io::stdin()
	.read_line(&mut str)
	.expect("");
```

### 字符串

注意hardcoded的string literal和String类型是不一样的。

```
String::from("something") // 构造String
string.trim() // 去除字符串首尾空白字符，类似python的strip()
string.parse() // 字符串转数字
string.push_str("something") // string后接新的串
println!("{}", string) // 可以格式化打印
string.as_bytes() // 返回一个可迭代的字符数组
```

#### Slice切片

可以从字符串中取一段索引，它实际上是一种指向一个字符串的immutable reference.

上文提到的string literal实际上就相当于指向内存中一段文本的slice(`&str`)，所以相当于是immutable reference。

```
str[0..2]
str[..2]
str[..]
```

```
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

调用clear方法时，需要字符串提供一个可变引用，因此会出错。

```
fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s[..]);

    s.clear(); // error!

    println!("the first word is: {}", word);
}
```

###
