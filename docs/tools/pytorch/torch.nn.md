# torch.nn

## torch.nn 方法

```text
# 如何产生常用的层

# 2维卷积层，带个卷积核
nn.Conv2d(in_channel,out_channel,(kernel_width,kernel_length))
# in_channel代表输入的channel数（比如RGB图像输入就是3个channel）
# out_channel代表输出的channel数（应该就是卷积核的个数，每个核扫一遍出一个channel）
# kernel_size = (width,length)就是每个卷积核的大小了

# 线性层，或者说全连接层，参数为输入数据维度和输出数据维度，都是整型
nn.Linear(in_dim,out_dim) 

# drop out
nn.Dropout(dropout)

train(mode = True)
使模型进入训练模式。据称只对部分模型有影响。返回self.

nn.Parameter
是 Tensor 的子类，把 Tensor 封装为一个被认为是模型参数的对象。

Container:

ModuleList(modules = None)
把子模块放在一个列表里面，可以像列表一样访问。


```

