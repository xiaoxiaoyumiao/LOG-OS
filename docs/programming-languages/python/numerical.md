# Numerical

## Random

```python
# Shuffle the sequence x in place.
# The optional argument random is a 0-argument function 
# returning a random float in [0.0, 1.0); 
# by default, this is the function random().
# (This argument is deprecated since 3.9 and to be removed in 3.11)
random.shuffle(x[, random])
```

## Emulating Numbers

```python
object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__matmul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)
# These methods are called to implement the binary arithmetic operations 
# (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |).
```

## Reference

\[1\] [https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)

\[2\] [https://docs.python.org/3/reference/datamodel.html\#emulating-numeric-types](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)

