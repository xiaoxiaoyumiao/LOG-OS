# Collections

## Collections

`collections.defaultdict(function_factory)`，创建一个`dict`对象，所有value都是function的实例，并且对不存在的key，d\[key\]也有一个该function实例的默认值。例如，`defaultdict(int)`创建一个key到int类型的映射，并且每个不存在的key都有一个默认值value：0.

内建转换函数都是工厂函数。例如，`int(),long(),float(),complex(),str(), unicode(), basestring(),list(), tuple(), type(), dict(), bool(),set(), frozenset(),object() ,classmethod(),staticmethod(), super(), property(), file()`

拓展知识可参考 [Iterables](../iterables.md).

