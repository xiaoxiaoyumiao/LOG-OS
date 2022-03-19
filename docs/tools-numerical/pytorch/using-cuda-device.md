# Using CUDA Device

## CUDA Semantics

在有 CUDA 资源的时候，我们可能会希望 torch 使用 CUDA 进行计算以提高效率。大体来说，torch 通过 torch 对象（tensor 、module 等）所在的设备（cpu、cuda device 等）来决定使用什么设备完成计算。因此，需要在创建 tensor 和 module 对象时将其移动到所需的设备上。

虽然 torch 提供了多样的 CUDA 使用的接口，但利用 `torch.device` 可能是最灵活而简洁的办法。一个`torch.device` 对象表示一个设备，例如：

```python
cpu = torch.device('cpu')        # CPU
cuda = torch.device('cuda')      # Default CUDA device (usually 0)
# get specific CUDA device by index
cuda0 = torch.device('cuda:0')   # GPU 0
cuda2 = torch.device('cuda:2')   # GPU 2 (these are 0-indexed)
```

使用这些设备对象作为创建 tensor 的 `device` 参数，创建的 tensor 就会被分配在相应设备上。打印 tensor 可以看到 tensor 的设备信息；也可以通过 tensor 的 `device` 属性获取其所在设备：

```python
a = torch.tensor([1,2,3], device=cpu)
b = torch.tensor([1,2,3], device=cuda)
print(a,b)
print(a.device,b.device)

# output:
tensor([1, 2, 3]) tensor([1, 2, 3], device='cuda:0')
cpu cuda:0
```

如果已经拥有一个 tensor 对象（例如是通过第三方接口获得的），希望把它移动到特定的设备上，则可以使用 tensor 的 `to` 方法。它是用来完成 tensor 类型转换的，但同时也可以转换 tensor 所在的设备：

```python
c = a.to(cuda)
print(c)

# output:
tensor([1, 2, 3], device='cuda:0')
```

如果希望基于 `nn.Module` 的 torch 模型在特定的设备上运行，那么除了移动作为输入的 tensor 以外还需要移动 module 对象（因为它也包含了同为 tensor 的参数等等）。模型同样拥有 `to` 方法，参数是 device 时使用方法和 `torch.Tensor.to()` 类似。

```python
input = torch.tensor([1,2,3], dtype=torch.float32, device=cuda)
model = torch.nn.Linear(3, 3).to(cuda)
output = model(input)
print(output.device)

# output
cuda:0
```

请确保自己使用的所有 tensor 和 module 对象都在希望分配的同一设备上。跨设备的计算原则上是不允许的，如果计算时发现参与运算的 tensor（或者 tensor 和 module）不在同一设备就会报错。报错在一定程度上也可以帮助检查是否所有参与运算的对象都移动到了相应设备。

采用 device 对象控制所有 tensor 和 module 的所在设备后，就可以用类似如下的逻辑让代码适应多种计算环境。`torch.cuda.is_available` 方法可以判断当前是否有可用的 CUDA 资源：

```python
global_device = torch.device('cpu')
# suppose args is some parsed command line arguments
if args.device == "gpu" and torch.cuda.is_available() == True:
    global_device = torch.device('cuda')
    
# then use global_device to create tensors and modules
```

## Data Paralleling

使用 `nn.DataParallel` 可以便捷地实现在batch 维度上的多设备并行。一个 batch 会被均匀分配到多个设备上，当 batch 大小不足够时则只会分配到部分设备上。

```python
model = Model(input_size, output_size)
if torch.cuda.device_count() > 1:
  print("Let's use", torch.cuda.device_count(), "GPUs!")
  # dim = 0 [30, xxx] -> [10, ...], [10, ...], [10, ...] on 3 GPUs
  model = nn.DataParallel(model)

model.to(device)
```

## Reference

\[1\] [https://pytorch.org/docs/master/notes/cuda.html](https://pytorch.org/docs/master/notes/cuda.html)

\[2\] [https://pytorch.org/docs/master/tensor\_attributes.html\#torch.torch.device](https://pytorch.org/docs/master/tensor_attributes.html#torch.torch.device)

\[3\] [https://pytorch.org/docs/master/generated/torch.Tensor.to.html\#torch.Tensor.to](https://pytorch.org/docs/master/generated/torch.Tensor.to.html#torch.Tensor.to)

\[4\] [https://pytorch.org/docs/master/generated/torch.nn.Module.html\#torch.nn.Module.to](https://pytorch.org/docs/master/generated/torch.nn.Module.html#torch.nn.Module.to)

\[5\] [https://discuss.pytorch.org/t/solved-make-sure-that-pytorch-using-gpu-to-compute/4870/14](https://discuss.pytorch.org/t/solved-make-sure-that-pytorch-using-gpu-to-compute/4870/14)

\[6\] [https://discuss.pytorch.org/t/nn-dataparallel-and-batch-size-is-1/36789](https://discuss.pytorch.org/t/nn-dataparallel-and-batch-size-is-1/36789)

\[7\] [https://pytorch.org/tutorials/beginner/blitz/data\_parallel\_tutorial.html](https://pytorch.org/tutorials/beginner/blitz/data_parallel_tutorial.html)

\[8\] [https://pytorch.org/docs/stable/generated/torch.nn.DataParallel.html](https://pytorch.org/docs/stable/generated/torch.nn.DataParallel.html)

