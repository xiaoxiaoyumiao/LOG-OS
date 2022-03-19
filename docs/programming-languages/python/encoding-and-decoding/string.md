# String

## **Format**

格式化：%和format

```python
#%格式化：
 1 >>> print('%f' % 1.11)  # 默认保留6位小数
 2 1.110000
 3 >>> print('%.1f' % 1.11)  # 取1位小数
 4 1.1
 5 >>> print('%e' % 1.11)  # 默认6位小数，用科学计数法
 6 1.110000e+00

#format格式化，'something'.format(someData)
 1 >>> print('{} {}'.format('hello','world'))  # 不带字段
 2 hello world
 3 >>> print('{0} {1}'.format('hello','world'))  # 带数字编号
 4 hello world
 5 >>> print('{0} {1} {0}'.format('hello','world'))  # 打乱顺序
 6 hello world hello
 7 >>> print('{1} {1} {0}'.format('hello','world'))
 8 world world hello
 9 >>> print('{a} {tom} {a}'.format(tom='hello',a='world'))  # 带关键字
10 world hello world
```

| 数字 | 格式 | 输出 | 描述 |
| :--- | :--- | :--- | :--- |
| 3.1415926 | {:.2f} | 3.14 | 保留小数点后两位 |
| 3.1415926 | {:+.2f} | +3.14 | 带符号保留小数点后两位 |
| -1 | {:+.2f} | -1.00 | 带符号保留小数点后两位 |
| 2.71828 | {:.0f} | 3 | 不带小数 |
| 5 | {:0&gt;2d} | 05 | 数字补零 \(填充左边, 宽度为2\) |
| 5 | {:x&lt;4d} | 5xxx | 数字补x \(填充右边, 宽度为4\) |
| 10 | {:x&lt;4d} | 10xx | 数字补x \(填充右边, 宽度为4\) |
| 1000000 | {:,} | 1,000,000 | 以逗号分隔的数字格式 |
| 0.25 | {:.2%} | 25.00% | 百分比格式 |
| 1000000000 | {:.2e} | 1.00e+09 | 指数记法 |
| 13 | {:&gt;10d} | 13 | 右对齐 \(默认, 宽度为10\) |
| 13 | {:&lt;10d} | 13 | 左对齐 \(宽度为10\) |
| 13 | {:^10d} | 13 | 中间对齐 \(宽度为10\) |

## Pattern Matching

TODO

ref: \[1\]

## Reference

\[1\] [https://docs.python.org/2/library/re.html](https://docs.python.org/2/library/re.html)

\[2\] [https://www.cnblogs.com/fat39/p/7159881.html](https://www.cnblogs.com/fat39/p/7159881.html)

