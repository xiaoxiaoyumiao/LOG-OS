# Heap

## heapq

```python
import heapq

# heapq 提供一组方法，用于实现堆操作
# 空列表被 heapq 方法作用后转化为堆
# 将列表 x 转化为堆
heapq.heapify(x)
# 将元素 item 压入堆 heap 中
heapq.heappush(heap, item)
# 从堆 heap 中获取最小元素
heapq.heappop(heap)
h = []
for value in iterable:
    heappush(h, value)
    
# 使用自定义的优先级时，将 heap 元素构造为 (priority, data) 的形式，
# 或为其元素重写 __lt__() 方法。(ref [2])
```

## Reference

\[1] [https://docs.python.org/3/library/heapq.html](https://docs.python.org/3/library/heapq.html)

\[2] [https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate/8875823](https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate/8875823)
