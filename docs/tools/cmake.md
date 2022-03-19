# CMake

## Dependency

### Robot

* basic shell for Linux \[EASY\]

### Human

* make & makefile \[EASY\]
* apt \[EASY\]
* wget \[EASY\]
* tar \[EASY\]
* libssl-dev \[EASY\]
* build-essential \[EASY\]

## Introduction

CMake 可以为项目生成一个与项目所在环境适配的 makefile 文件，交给 make 去 make。

## Installation

OS：Windows 10 WSL Linux version: Ubuntu 18.04.5 LTS

以下命令的效果为：将所需的某一版本 CMake 源码下载到本地，编译并安装。

执行以下命令时，如果提示 Permission Denied，就尝试在命令前加上 `sudo` 。

如果已安装旧版本 CMake，先移除旧版本：

```bash
apt remove cmake
```

安装编译必要的库：

```bash
apt install libssl-dev build-essential
```

·选择一个合适的目录，获取所需的 CMake 版本（以 3.16.0 为例）：

```bash
cd /usr/src # choose a proper directory
wget https://github.com/Kitware/CMake/releases/download/v3.16.0/cmake-3.16.0.tar.gz # download CMake file
tar -zxvf cmake-3.16.0.tar.gz # unzip file
cd cmake-3.16.0 # enter root of CMake project
```

在源码根目录下编译和安装：

```bash
./bootstrap # run the build script provided by project
make # compile
sudo make install # install
```

完成后重启 shell。

测试安装是否成功：

如果 CMake 安装成功，以下命令将打印已安装的 CMake 的版本号。

```bash
cmake --version
```

输出：

```bash
cmake version 3.16.0

CMake suite maintained and supported by Kitware (kitware.com/cmake).
```

## Reference

[\[1\] ubuntu 中 cmake 版本升级](https://www.cnblogs.com/passedbylove/p/11982777.html)

[\[2\] How to Install build-essential on Ubuntu 16.04/18.04 Linux ](https://www.osetc.com/en/how-to-install-build-essential-on-ubuntu-16-04-18-04-linux.html)

[\[3\] Installing CMake](https://cmake.org/install/)

