# MAP file / M51

## Dependency

### Human

* 编译原理

## Introduction

* BL51 链接器在链接和定位时会产生后缀为 .M51 的文件，这个文件称为 listing\(MAP\) file，包含了对分析程序内存布局极有帮助的众多信息。
* applies to C51 Version 5.50a and later

## Sections

* Page Header - MAP file 的内容按页组织（虽然是单文件），每一页的第一行是一个 header，描述链接器的版本，生成的时间和页号。页的划分依据似乎只是行数。
* 下面按在 M51 文件中的出现顺序依次记录各个段的内容。
* Command Line - 链接器被调用时执行的命令行指令。例如
* ```text
  [some path]\BL51.EXE STARTUP.obj, config.obj, main.obj TO CHIPTESTER RAMSIZE (256)
  ```
* CPU Details - 指示项目使用的 memory model：
* ```text
  MEMORY MODEL: SMALL
  ```
* Input Modules - 列出链接时所有的输入文件，如各个 obj 和 lib 文件。
* Memory Map - 列出程序的物理存储使用情况。包含了 DATA，XDATA，CODE 三个小节。横向则有 TYPE，BASE，LENGTH，RELOCATION, SEGMENT NAME 几个字段。BASE 和 LENGTH 分别表示本行描述的  segment 的起始地址和长度，SEGMENT NAME 表示这个 segment 的名称。其他字段的意义则如下 \(ref: \[3\]\)：

> The TYPE column refers to the memory type, where BIT is bit addressable memory, DATA is internal directly addressable memory and IDATA is internal indirectly addressable memory. REG is a special case being the internal directly addressable memory that is reserved for the register banks. You will find out more all this in the Keil documentation and appropriate data sheets.
>
> Sections that are ABSOLUTE have a predetermined fixed place in memory and cannot be moved by the linker. Sections that are not ABSOULTE will be given a memory location by the linker/locator.
>
> A GAP will occur where the linker/locator cannot find anything to place in a range of memory locations. Your program has used a certain abount of bit addressable memory, but these bits must be fitted into a whole number of bytes ending in byte 0x27 of directly addressable RAM. This leaves a few unused bits left over. Your directly addressable RAM use starts are byte 0x28. \(by Graham Cole\)

* Overlay Map - 相当于程序的 call tree（函数调用图），展示程序的结构。
* Symbol Table - 符号表。NAME 为符号名称，VALUE 字段包含一个指示存储类型（如 data, xdata, code 之类）的前缀和一个值。TYPE 指示符号类型。对于多文件编译的情形，符号表会按文件组织为 module，每个文件对应一个同名的 module。一个 module 以一个类型为 MODULE 的同名符号开始，以一个类型为 ENDMOD 的同名符号结束。以下表格表示了一个名为 HELLO 的 module（其符号表的内容已省略）：
* ```text
  VALUE           TYPE          NAME
    ----------------------------------

    -------         MODULE        HELLO
  ...
    -------         ENDMOD        HELLO
  ```

  * 其他的 TYPE 取值意义还不清楚。
* Program Size - 输出链接后程序对各个存储空间的使用情况。
* ```text
  Program Size: data=59.0 xdata=512 code=1022
  ```
* Warnings & Errors - 输出链接过程中产生的警告和错误信息。
* ```text
  LINK/LOCATE RUN COMPLETE.  0 WARNING(S),  0 ERROR(S)
  ```

## Reference

\[1\] [https://www.keil.com/support/man/docs/bl51/bl51\_ln\_mapfile.htm](https://www.keil.com/support/man/docs/bl51/bl51_ln_mapfile.htm)

\[2\] [https://www.keil.com/support/docs/1676.htm](https://www.keil.com/support/docs/1676.htm)

\[3\] [https://community.arm.com/developer/tools-software/tools/f/keil-forum/42229/unknown-information-in-m51-file](https://community.arm.com/developer/tools-software/tools/f/keil-forum/42229/unknown-information-in-m51-file)

\[4\] [https://www.keil.com/support/docs/1201.htm](https://www.keil.com/support/docs/1201.htm)

