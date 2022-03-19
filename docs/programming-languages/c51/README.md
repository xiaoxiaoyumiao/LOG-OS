# C51

C51 是一种用于开发 8051 架构上的应用程序的编程语言，其语法是 C 的扩展。可使用的 IDE 有 Keil μvision、Simplicity Studio 等，Keil 提供了完整的 C51 编译链接工具链以及配套的说明文档。

## 使用 Keil 开发

（本节建议细化后移动到 Keil 介绍中）

```c
// AT89C51/52 上的一个空转程序
# include "reg52.h" //reg51 for C51
void main(){
    while (1){
        // do something
    }
}
```

build\(F7\) target options - output - create HEX file

生成的 HEX 文件就可以通过 programmer 烧录到目标设备中。

关于 HEX 文件的格式（待补完）

[https://en.wikipedia.org/wiki/Intel\_HEX](https://en.wikipedia.org/wiki/Intel\_HEX)

## 命令行编译

**所有编译链接工具的使用文档可以在 keil 的 help 中查到。** C51.EXE 编译 c 文件，BL51.EXE 链接 OBJ， OH51.EXE 转换文件成 HEX。

如：有文件 test.c：

```bash
C51 test.c
BL51 test.obj TO test # 链接多文件时用逗号分隔文件名
OH51 test
```

这样就能编译出HEX文件。

\`\`

