# Introduction

## Installation

### 环境变量配置

变量名JAVA\_HOME 变量值为jdk路径（...\jdk-xxx）

Path中添加%JAVA\_HOME%\bin

cmd中运行java -version和javac测试即可

### JAVA包管理gradle安装

binary-only安装包解压到预定安装路径，

变量名GRADLE\_HOME 变量值gradle路径（...\gradle-xxx）

Path中添加%GRADLE\_HOME%\bin

cmd中运行gradle -v

## Hello World

### Comments

```java
//单行注释
​
/*
多行注释
多行注释
不可嵌套
*/
​
/**
用于Javadoc的注释方法
*/
​
```

### Main Process

```java
//主函数定义，公共类名需要和本文件名相同
public class ClassName{
    public class void main(String[] args){
        //function body
    }
}
```

## Usage

```bash
javac ClassName.java # compile
java ClassName # run
```

### trivial

java12中switch表达式需要--enable-preview编译选项支持

