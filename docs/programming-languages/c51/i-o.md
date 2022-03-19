# I/O

* `printf` \(ref: [https://www.keil.com/support/man/docs/c51/c51\_printf.htm](https://www.keil.com/support/man/docs/c51/c51_printf.htm)\)
  * This function is implementation-specific and is based on the operation of the `_getkey` and `putchar` functions. These functions, as provided in the standard library, read and write characters using the microcontroller's serial port. Custom functions may use other I/O devices.
    * C51 中的 low-level stream I/O routines 由 `putchar` 和 `_getkey` 定义和实现。
    * 这两个函数的缺省实现可以在 keil 安装目录下的 LIB 文件夹中找到（PUTCHAR.C 和 GETKEY.C）。可以把它们复制到自己的项目中并修改实现来让 `printf` 适应当前项目的 IO 设备。
    * 默认的 `getchar` 实现会把 \n 扩展为 \r\n。
  * A maximum of 15 bytes may be passed in SMALL or COMPACT model. A maximum of 40 bytes may be passed in LARGE model.
    * 也就是说一次传输的数据长度是有限制的。拓展：[https://www.keil.com/support/docs/867.htm](https://www.keil.com/support/docs/867.htm)

