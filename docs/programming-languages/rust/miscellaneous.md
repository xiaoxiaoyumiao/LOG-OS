# Miscellaneous

### 操作系统相关

如何在程序中移除对OS的依赖？

* 核心库`core`是一个和操作系统无关的crate。
* 堆栈展开：`eh_personality`，当程序出错时沿堆栈回溯回收所有局部变量，包括RAII（资源获取即是初始化，最初构造，最后析构）和drop
* 在toml中可以设置panic时是否采用堆栈展开策略：
  * ```
    [profile.dev]
    panic = "abort"

    [profile.release]
    panic = "abort"
    ```
* > 对于大多数语言，他们都使用了 **运行时系统(runtime system)** ，这导致 main 并不是他们执行的第一个函数。
  >
  > 以 Rust 语言为例：一个典型的链接了标准库的 Rust 程序会首先跳转到 C runtime library 中的 **crt0(C runtime zero)** 进入 C runtime 设置 C 程序运行所需要的环境(比如：创建堆栈，设置寄存器参数等)。
  >
  > 然后 C runtime 会跳转到 Rust runtime 的 **入口点(entry point)** 进入 Rust runtime 继续设置 Rust 运行环境，而这个入口点就是被 `start` 语义项标记的。Rust runtime 结束之后才会调用 main 进入主程序。
  >
  > C runtime 和 Rust runtime 都需要标准库支持，我们的程序无法访问。如果覆盖了 `start` 语义项，仍然需要 `crt0`，并不能解决问题。
* ```
  // src/main.rs

  #![no_std] // don't link the Rust standard library
  #![no_main] // disable all Rust-level entry points 不使用常规入口点

  use core::panic::PanicInfo;
  // This function is called on panic.
  #[panic_handler]
  fn panic(_info: &PanicInfo) -> ! {
      loop {}
  } // 返回值为!表示不允许返回

  #[no_mangle] // don't mangle the name of this function 确保函数名不被程序（为了保证唯一性而）更改
  pub extern "C" fn _start() -> ! {
      // this function is the entry point, since the linker looks for a function named `_start` by default
      loop {}
  } // extern "C" 标识这是一个C函数
  ```

\
