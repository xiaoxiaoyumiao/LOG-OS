# Miscellaneous

* restrict 关键字
* 关于 `do {} while(0)`：
  * 使用 `#define MACRO do { [statements] } while (0)`  来包含一个代码块 `[statements]`，就可以书写形如 `MACRO;` 的语句并安全地展开。
  * 被其包裹的代码也可以通过 `break` 语句实现跳转到代码块结尾的效果，而不必使用 `goto` 语句。
* 全局变量使用 static 关键字修饰
  * 该变量只能被位于同一文件中的函数使用

