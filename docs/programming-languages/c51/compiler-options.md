# Compiler Options

* OT / OPTIMIZE
  * default: OT\(8, SPEED\)
  * OT 包含两个参数，第一个参数为优化等级，第二个参数可取值 SIZE 或 SPEED，用来设定优化大小还是速度。
  * 使用 \#pragma 语句可以针对程序的特定部分做特定优化。
* DB / DEBUG
  * default: -
  * 在编译得到的 object file 中插入调试信息，这些信息可被 IDE 等用于运行时调试。
* OE / OBJECTEXTEND
  * default: -
  * 在编译得到的 object file 中插入变量定义信息，使得来自不同作用域的同名变量能够被仿真器等识别。
* BR / BROWSE
  * default: -
  * 在编译得到的 object file 中插入 browser 信息，包括变量的标识符、存储类型等。
* INTVECTOR
  * 设置中断向量表的起始地址。默认为0.
* INTERVAL
  * 设置中断向量表每两项之间的间隔。默认为 8.

