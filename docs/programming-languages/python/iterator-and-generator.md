# Iterator & Generator

## Iterator

> The iterator objects themselves are required to support the following two methods, which together form the _iterator protocol_:
>
> `iterator.__iter__`\(\)
>
> Return the iterator object itself. This is required to allow both containers and iterators to be used with the [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)and [`in`](https://docs.python.org/3/reference/expressions.html#in) statements. This method corresponds to the [`tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter) slot of the type structure for Python objects in the Python/C API.
>
> `iterator.__next__`\(\)
>
> Return the next item from the container. If there are no further items, raise the [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration) exception. This method corresponds to the [`tp_iternext`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iternext) slot of the type structure for Python objects in the Python/C API.

## Generator

Generator 是一种特殊的 iterator。

### Generator Expressions

```python
a = [1,2,3]
gen = (x for x in a)
```

### Yield Expressions

yield 表达式可以拥有值。

> `generator.__next__()`
>
> Starts the execution of a generator function or resumes it at the last executed yield expression.
>
> `generator.send(value)`
>
> Resumes the execution and “sends” a value into the generator function. The _value_ argument becomes the result of the current yield expression. The [`send()`](https://docs.python.org/3/reference/expressions.html#generator.send) method returns the next value yielded by the generator, or raises [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration) if the generator exits without yielding another value.

```python
# This function returns a generator object.
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```

> If a container object’s [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__) method is implemented as a generator, it will automatically return an iterator object \(technically, a generator object\) supplying the [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__) and [`__next__()`](https://docs.python.org/3/reference/expressions.html#generator.__next__) methods.
>
> When `yield from <expr>` is used, the supplied expression must be an iterable. The values produced by iterating that iterable are passed directly to the caller of the current generator’s methods.

```python
>>> def genfrom():
...     a = [1,2,3]
...     yield from a
...
>>> b = genfrom()
>>> b.__next__()
1
>>> b.__next__()
2
```

## Reference

\[1\] [https://docs.python.org/3/library/stdtypes.html\#iterator-types](https://docs.python.org/3/library/stdtypes.html#iterator-types)

\[2\] [https://docs.python.org/3/reference/expressions.html\#generator-expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions)

