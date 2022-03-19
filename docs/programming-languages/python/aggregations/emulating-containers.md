# Emulating Containers

```python
# Called to implement the built-in function len(). 
# Should return the length of the object, an integer >= 0. 

# Also, an object that doesn’t define a __bool__() method and 
# whose __len__() method returns zero is considered 
# to be false in a Boolean context.
object.__len__(self)

# Called to implement evaluation of self[key]. 
# For sequence types, the accepted keys should be integers and slice objects. 
# Note that the special interpretation of negative indexes 
# (if the class wishes to emulate a sequence type) 
# is up to the __getitem__() method. 

# If key is of an inappropriate type, TypeError may be raised; 

# if of a value outside the set of indexes for the sequence 
# (after any special interpretation of negative values), 
# IndexError should be raised. 

# For mapping types, if key is missing (not in the container), 
# KeyError should be raised.
object.__getitem__(self, key)

# Called to implement assignment to self[key]. 
# Same note as for __getitem__(). 

# This should only be implemented for mappings 
# if the objects support changes to the values for keys, 
# or if new keys can be added, 
# or for sequences if elements can be replaced. 

# The same exceptions should be raised for improper key values 
# as for the __getitem__() method.
object.__setitem__(self, key, value)

# This method is called when an iterator is required for a container. 
# This method should return a new iterator object 
# that can iterate over all the objects in the container. 
# For mappings, it should iterate over the keys of the container.
object.__iter__(self)
```

## Reference

\[1\] [https://docs.python.org/3/reference/datamodel.html\#object.\_\_getitem\_\_](https://docs.python.org/3/reference/datamodel.html#object.__getitem__)

