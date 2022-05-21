# LLVM

## Dependency

### Robot

* basic shell for Linux \[EASY\]
* tar \[EASY\]

## Introduction

## Installation

OS：Windows 10 WSL Linux version: Ubuntu 18.04.5 LTS

以下操作的效果：获取 LLVM 工程源码，编译并安装。

执行以下命令时，如果提示 Permission Denied，就尝试在命令前加上 `sudo` 。

从 LLVM 下载页 \[1\] 获取所需版本的 llvm-project monorepo source code，下载到本地。

使用解压缩工具将源码解压到合适的目录下。

在解压出的项目的根目录中可以看到 README.md，按照 README.md 的指示操作，在项目的根目录执行以下命令，并选择合适的参数，参数的意义可以参考 \[2\]：

```bash
 cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -DLLVM_TARGETS_TO_BUILD="X86" ../llvm
 make # compile and build
 sudo make install # install
```

测试安装是否成功：

```bash
make check-all
```

更直观的使用 clang 的测试方法可以参考 \[3\] 。

## Reference

[\[1\] LLVM Download Page](https://releases.llvm.org/)

[\[2\] Building LLVM with CMake](https://llvm.org/docs/CMake.html#building-llvm-with-cmake)

[\[3\] Getting Started with the LLVM System - An Example Using the LLVM Tool Chain](https://llvm.org/docs/GettingStarted.html#an-example-using-the-llvm-tool-chain)

