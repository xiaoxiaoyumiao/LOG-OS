# DLL

在 Windows 10 平台使用 Visual Studio 2017 编写和生成 dll。

## Create a Project

创建一个 Visual C++ 的 Dynamic-Link Library \(DLL\) 项目。这里我们把项目命名为 SampleDll。项目创建时包含必要的头文件和一个 dllmain 文件。dllmain 文件包含类似如下代码：

```cpp
// dllmain.cpp : Defines the entry point for the DLL application.
#include "pch.h"

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}
```

DllMain 是一个实现可选的入口函数，使得用户可以处理 dll 的加载和卸载等事件。如果不实现，链接器会链接一个 dummy DllMain。\(ref: \[3\]\)

## Define Exported Functions

大体来说，要使得一个函数能够被 dll 的使用者调用，也就是要把一个函数导出到 dll，只需要在这个函数前加上特定的修饰符：

```cpp
extern "C" __declspec( dllexport ) int add(int a, int b);
```

这里 extern "C" 的作用是告诉编译器使用 C 的规范来编译这个函数，使得函数可以被其他类 C 的语言调用。\(ref: \[2\]\)

使用 dll 时，需要先声明将使用的 dll 中的函数，这些函数声明常常一起放在一个头文件里。为了方便使用，在使用 Visual Studio 生成 dll 时可以利用预处理指令，把所有需要导出的函数声明放在一个头文件里：

```cpp
#pragma once

#ifdef SAMPLEDLL_EXPORTS
#define SAMPLEDLL_API __declspec(dllexport)
#else
#define SAMPLEDLL_API __declspec(dllexport)
#endif

extern "C" SAMPLEDLL_API int add(int a, int b);
```

注意到 SAMPLEDLL 是我们的项目名称（转大写）。${PROJECTNAME}\_EXPORTS 是一个 Visual Studio 在编译项目时会定义的符号，以此可以区分这个头文件是正在被编译为 dll 还是被 dll 的使用者使用，进而决定函数的修饰符。

函数的实现等就和普通的函数一样。完成后构建解决方案即可得到输出的 dll 文件。

## Reference

\[1\] [https://docs.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-dynamic-link-library-cpp?view=msvc-160](https://docs.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-dynamic-link-library-cpp?view=msvc-160)

\[2\] [https://stackoverflow.com/questions/1041866/what-is-the-effect-of-extern-c-in-c](https://stackoverflow.com/questions/1041866/what-is-the-effect-of-extern-c-in-c)

\[3\] [https://forums.codeguru.com/showthread.php?540463-what-does-dllmain-entry-point-do](https://forums.codeguru.com/showthread.php?540463-what-does-dllmain-entry-point-do)

