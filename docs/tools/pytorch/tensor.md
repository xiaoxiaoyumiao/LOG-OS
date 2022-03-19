# Tensor

```python
# use torch.tensor(data) to create a torch tensor from python list
data = [[1,2],[3,4]]
x_data = torch.tensor(data)

# use torch.from_numpy(data) to create a torch tensor from numpy array
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

# construct special tensors from a shape
shape = (2,3,)
rand_tensor = torch.rand(shape) # random float in (0,1)
ones_tensor = torch.ones(shape) # all ones
zeros_tensor = torch.zeros(shape) # all zeros

# construct special tensors like a given tensor
x_ones = torch.ones_like(x_data) # all ones
x_rand = torch.rand_like(x_data, dtype=torch.float) # all random and of float type

# get shape, data type and device the tensor is stored on
tensor = torch.rand(3,4)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")
```

## Frequently Used Ops

### Normal Math

```python
import torch.nn.functional as F

# softmax
F.softmax(data,dim=0)

# log softmax: log(softmax(tensor)), faster and safer than softmax
data = torch.tensor([1,1,1],dtype=float)
F.log_softmax(data,dim=0)
# tensor([-1.0986, -1.0986, -1.0986], dtype=torch.float64)
# log(1/3) = -1.0986

# real cross entropy implementation
def cross_entropy(pred, soft_targets):
    return torch.mean(torch.sum(- soft_targets * F.log_softmax(pred), 1))

```

### Shape Manipulation

```python
# squeeze: remove all dimensions of length 1
data = torch.tensor([[[1],[2],[3]]])
torch.squeeze(data) # tensor([1,2,3])

# torch.unsqueeze()
    
# flatten: reshape tensor to 1d tensor
torch.flatten(input, start_dim=0, end_dim=-1)
# If start_dim or end_dim are passed, 
# only dimensions starting with start_dim and ending with end_dim
# are flattened. The order of elements in input is unchanged.
t = torch.tensor([[[1, 2],
                   [3, 4]],
                  [[5, 6],
                   [7, 8]]])
torch.flatten(t, start_dim=1)
# tensor([[1, 2, 3, 4],
#         [5, 6, 7, 8]])
```

### Reduction Ops

```python
# argmax
data = torch.tensor([1,2,100,3])
torch.argmax(data) # tensor(2)
```

### Conditional Ops

```python
# masked_select: construct a new tensor with selected elements by a mask
>>> x = torch.randn(3, 4)
>>> x
tensor([[ 0.3552, -2.3825, -0.8297,  0.3477],
        [-1.2035,  1.2252,  0.5002,  0.6248],
        [ 0.1307, -2.0608,  0.1244,  2.0139]])
>>> mask = x.ge(0.5)
>>> mask
tensor([[False, False, False, False],
        [False, True, True, True],
        [False, False, False, True]])
>>> torch.masked_select(x, mask)
tensor([ 1.2252,  0.5002,  0.6248,  2.0139])

# a list of indices of which elements in inpus are non-zero
torch.nonzero(input, *, out=None, as_tuple=False)s
```

## Reference

\[1\] [https://discuss.pytorch.org/t/how-should-i-implement-cross-entropy-loss-with-continuous-target-outputs/10720/18](https://discuss.pytorch.org/t/how-should-i-implement-cross-entropy-loss-with-continuous-target-outputs/10720/18)

\[2\] [https://pytorch.org/docs/stable/torch.html](https://pytorch.org/docs/stable/torch.html)

\[3\] [https://pytorch.org/tutorials/beginner/basics/tensorqs\_tutorial.html](https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)

