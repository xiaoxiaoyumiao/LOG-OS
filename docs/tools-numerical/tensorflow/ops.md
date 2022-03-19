# Ops

```python
tf.zeros_like(tensor, dtype)
tf.math.maximum(t1, t2) # map(zip(t1, t2), lambda t1, t2: max(t1, t2))
tf.where(cond, x, y) # map(zip(cond, x, y), lambda cond, x, y: x if cond else y)
tf.greater_equal(t1, t2) # map(zip(t1, t2), lambda t1, t2: t1 >= t2)
tf.cast(tensor, dtype)
tf.boolean_mask(tensor, mask) # [ x for x, m in zip(tensor, mask) if m ]
tf.reduce_sum(tensor) # sum(tensor)
tf.reduce_sum(tensor, axis, keepdims) # sum along axis, keep len(axis)=1 if keepdims
	# axis can be a list of axes
tf.reshape(tensor, shape) # if shape has one -1, corresp dim is inferred
	# In particular, shape == [-1] will flatten the tensor
tf.expand_dims(tensor, axis) # add a axis with dim=1 for tensor
tf.tile(tensor, multiples) # replicate tensor multiple[i] times along axis i
tf.nn.top_k
tf.matmul
tf.nn.bias_add
tf.tensordot(tensor1, tensor2, axes) # generalized matrix multiplication
	# axes has a form of (axes1, axes2), in which axes1 and axes2 can be 
    # axis or tuple of axes respectively.
	# tensor1 should have same dimensions along axes1 as those of tensor2 along axes2
    # for example: t1.shape = (2, 3, 4) t2.shape= (3, 2, 5) axes=((0,1),(1,0))
    # sum-reduction is performed on slices along axes from two tensors
    # for example: res[1][2] = reduced_sum(t1[:][:][1], t2[:][:][2])
    # = sum([(t1[i][j][1]*t2[j][i][2]) for i in [0~2) for j in [0~3)])
    # ref: https://stackoverflow.com/questions/41870228/understanding-tensordot
tf.logical_and(t1, t2)
tf.clip_by_value(
    t, clip_value_min, clip_value_max, name=None
)
tf.math.reduce_any(
    input_tensor, axis=None, keepdims=None, name=None, reduction_indices=None,
    keep_dims=None
) # do logical or along axis and reduce
```

