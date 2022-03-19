# Dataset & DataLoader

```text
from torch.utils.data import Dataset, DataLoader
```

## Dataset

torch 中的 Dataset 把数据集封装为一个可迭代的对象（也就是 python 中的 iterable），从而可以方便地使用 for 循环遍历获得数据实例。当然只是需要可迭代的话并不一定要用 Dataset，它的主要优点在于可以配合 DataLoader 类完成诸如 batching 等神经网络训练中的常用操作。

严格来说 Dataset 分为两种。`data.Dataset` 是 map-style 的，即拥有 `__len__` 和 `__getitem__` 方法（python 中的 sequence 接口）；`data.IterableDataset` 是 iterable-style 的，即拥有 `__iter__` 方法（python 中的 iterable 接口）。关于这些方法的细节可以参阅 python 的相关文档。如果想要自定义 Dataset，只需要定义一个继承`Dataset` 或 `IterableDataset` 的类，然后重写上面提到的相应的方法即可。

以下代码实现了一个简单的自定义 map-style dataset：

```python
class MyDataset(Dataset):
    def __init__(self):
        # self.data = ["To be or not to be, this is the question.".split(),] * 12
        # self.data = [[1,2,3,4],] * 12
        self.data = [torch.tensor([1,2,3,4]),] * 12
    def __len__(self):
        return len(self.data)
    def __getitem__(self, index):
        return self.data[index]

dataset = MyDataset()
for sample in dataset:
    print(sample) # will print tensor([1,2,3,4]) for 12 times
```

## DataLoader

DataLoader 是用于加载 dataset 的类。其基本功能从构造参数就可以大致看出。常用的参数有 `batch_size` 、`num_workers` 、`shuffle` 等。

关于 `num_workers` 的选择：ref \[4\]

```python
DataLoader(dataset, batch_size=1, shuffle=False, sampler=None,
           batch_sampler=None, num_workers=0, collate_fn=None,
           pin_memory=False, drop_last=False, timeout=0,
           worker_init_fn=None, *, prefetch_factor=2,
           persistent_workers=False)
```

以下代码实现了一种对 DataLoader 的简单使用。数据集采用上文定义的 `MyDataset` 。

```python
def test_dataloader():
    dataset = MyDataset()
    dataloader = DataLoader(dataset, batch_size = 4)
    for sample in dataloader:
        print(sample)
        break

test_dataloader() 
# output:
tensor([[1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]])
```

## Reference

\[1\] [https://pytorch.org/docs/stable/data.html\#module-torch.utils.data](https://pytorch.org/docs/stable/data.html#module-torch.utils.data)

\[2\] [https://docs.python.org/3/glossary.html](https://docs.python.org/3/glossary.html)

\[3\] tutorial: writing custom datasets, dataloaders and transforms: [https://pytorch.org/tutorials/beginner/data\_loading\_tutorial.html](https://pytorch.org/tutorials/beginner/data_loading_tutorial.html)

\[4\] guidelines for assigning num\_workers to DataLoader: [https://discuss.pytorch.org/t/guidelines-for-assigning-num-workers-to-dataloader/813](https://discuss.pytorch.org/t/guidelines-for-assigning-num-workers-to-dataloader/813)

