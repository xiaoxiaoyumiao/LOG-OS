# Start Up Files

* 标准的 STARTUP 代码中最后一行跳转到了 ?C\_START，它在无需要初始化的变量时跳转到 main，在有变量需要初始化时则跳转到 INIT 代码。INIT 是位于 LIB 文件夹下，keil 默认不拷贝到项目文件夹，也不推荐修改，但有时候确实可能需要修改（例如看门狗相关）的一个 A51 文件，它定义了  `?C_INITSEG` 段，负责初始化变量。
  * [https://www.silabs.com/community/mcu/8-bit/knowledge-base.entry.html/2015/09/14/c\_start\_symbol\_inke-QD72](https://www.silabs.com/community/mcu/8-bit/knowledge-base.entry.html/2015/09/14/c_start_symbol_inke-QD72)
  * [https://developer.arm.com/documentation/ka003500/latest](https://developer.arm.com/documentation/ka003500/latest)
  * [https://developer.arm.com/documentation/ka003268/latest](https://developer.arm.com/documentation/ka003268/latest)
  * 关于 INIT.A51 的介绍：
    * [https://www.keil.com/support/man/docs/c51/c51\_ap\_init.htm](https://www.keil.com/support/man/docs/c51/c51_ap_init.htm)

