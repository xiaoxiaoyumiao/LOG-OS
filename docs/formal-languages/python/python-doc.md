# Python Doc

## 注释风格

```text
#!D:/Code/python
# -*- coding: utf-8 -*-
# @Time : 2019/8/24 17:58
# @Author : Johnye
# @Site :
# @File : python_practise.py
# @Software: PyCharm
​
​
def day_learn_python(day, plan, state="finished", *learn_time, **learn_content):
    """
    计算学习时间。
    :param day: 固定参数，定义当天日期
    :param plan: 固定参数，表示当天是否学习python
    :param state:默认参数,学习计划是否完成 对应默认的参数为”finished“，如果输入参数”unfinished“，
    :param learn_time: 不定长参数，每天学习的时间 learn_time 离散的数字 每一个数字对应学习的内容
    :param learn_content: 关键字参数，每天学习的内容不定
    :return:返回当天日志，以及完成的情况
    """
    datetime = 0
    for time in learn_time:
        datetime = int(time) + datetime
    # ...
```

