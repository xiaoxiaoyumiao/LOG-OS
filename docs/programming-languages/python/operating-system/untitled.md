# Time

## **epoch / 时间基准点**

在Unix系统中，这个基准点就是1970年1月1日0点整那个时间点。

## **time**

time.time()返回一个从epoch开始计算的浮点数（单位：秒）

```python
import time

start = time.time()
print("hello")
end = time.time()
print(end - start)

time.sleep(1) # block for 1 second
```

## **datetime**

TODO

## Reference

\[1] [https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python](https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python)
