# Miscellaneous

特殊关键字：

```c
// bit 声明一个位标量，值是一个二进制位，取0或1，不能创建位的指针或数组
bit flag = 0; 
// sbit 定义可位寻址对象，一般用来给引脚起个别名
sbit variable_name = address_value; 
// 如：
sbit led = P2^0;
// sfr 定义8位SFR（特殊功能寄存器），给寄存器地址起个别名。如
sfr P0 = 0x80;
// sfr16 定义16位SFR，意义和用法同上
sfr16 T2 = 0xCC;
​
​
循环位移
_crol_(a,b) //返回a左移b位（循环）
_crol_(a,b) //返回a右移b位（循环）
```

* **C51 getchar\(\)函数会调用putchar\(\)把结果echo回去。**
  * [http://www.keil.com/support/man/docs/c51/c51\_getchar.htm](http://www.keil.com/support/man/docs/c51/c51_getchar.htm)

## 汇编指令集

A为累加器，C为累加器的carry flag（最高位的高一位），Rn为寄存器

```text
XCH A, Rn ;swap value of A and Rn
RRC A ;rotate right 1 bit
RLC A ;rotate left 1 bit
DJNZ Rn, LABEL ; Rn--; if (Rn!=0) jump to LABEL
```



