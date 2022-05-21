# Basics

## Basic Usage

* 特殊变量和常量
  * `ans`：最近的回答
  * `eps` ：浮点精度
  * `i` or`j`：虚数单位
  * `Inf`：无穷大
  * `NaN`：未定义
  * `pi`：圆周率
* 所有变量都是数组或矩阵
* 若表达式返回值未被指定分配给任何变量，默认分配给`ans`

```text
a = 2; b = 3; c = a + b # 变量赋值
who # 显示所有已使用的变量
whos # 显示变量细节
clear c # 删除一个变量
c = a + ...
 b # ...跨行指令
#format指令用于指定显示格式
global # 声明全局变量
```

* 其他交互指令：

```text
mkdir
chdir
cd
date
delete #删除文件
dir #列出当前目录下所有文件
```

## I/O

```text
save / load
save mymat # 保存所有变量到文件 mymat
load mymat # 从文件mymat中加载变量

%文件IO：
fscanf
fprintf
%字符串IO：
sprintf
input #屏幕输入
x = input(‘what’) %类似python
```

从文件读入纯数据：（仅含数字和空白符）

```text
A = dlmread(filepath);
```

## 控制流

```text
if [cond]
[stat]
elseif [cond]
[stat]
else
[stat]
end
​
while [cond]
[stat]
end
​
for index = [initval:endval | initval:step:endval | valArray]
end
% 区间尾会被包含进来
​
for a = 10:20
end
for a = 10:2:20
end
for a = [1,3,4,6,7]
end

function y=func(x)
end

% 断言函数
% error_cond逻辑表达式，为0时触发提示error_str
assert(error_cond, error_str)
```

## 基本运算

```text
​
#不等关系是~=

# 位运算
bitand(a,b)
bitor(a,b)
bitset(a,pos)
bitget(a,pos)
```

## 函数对象

```text
% 函数句柄/函数对象/function_handle
函数句柄的创建：
方式①：直接加@
　　　　语法：@函数名fun1 = @sin;
​
方式②：str2func函数
　　　　语法：str2fun('函数名')
　　　　fun2 = str2func('cos');
​
方式③：str2func函数
　　　　语法：@(参数列表)单行表达式
　　　　fun3 = @(x, y)x.^2 + y.^2;
```

