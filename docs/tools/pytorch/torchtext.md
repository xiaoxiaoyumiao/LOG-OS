# torchtext

```python
import torchtext
torchtext.data # 包含数据加载器，abstractions, iterators for text
torchtext.datasets # 包含常用的NLP数据集加载器
```

```python
Dataset(examples,fields,filter_pred=None)
variables: sort_key,examples, fields
examples: List of Examples
fields:List(Tuple(str,Field))
​
Dataset.split(split_ratio=0.7, stratified=False, strata_field='label', random_state=None)
'''
    split_ratio:取一个浮点数（此时表示训练集的占比，剩余用作验证）
    也可以取一个浮点数序列，此时表示训练-测试（-验证）的分割
    返回分割好的数据集(iter?)构成的元组
'''
Dataset.splits(path=None, root='.data', train=None, validation=None, test=None, **kwargs)
    train,validation,test取的都是三个数据集相对root的路径的值
    # 返回分割好的数据集构成的元组

class torchtext.data.TabularDataset(path, format, fields, skip_header=False,    csv_reader_params={}, **kwargs) 
    # format取{'CSV','TSV','JSON'}中的一个
```

## Iterator

```python
'''
dataset – The Dataset object to load Examples from.
batch_size – Batch size.
batch_size_fn – Function of three arguments (new example to add, current count of examples in the batch, and current effective batch size) that returns the new effective batch size resulting from adding that example to a batch. This is useful for dynamic batching, where this function would add to the current effective batch size the number of tokens in the new example.
sort_key – A key to use for sorting examples in order to batch together examples with similar lengths and minimize padding. The sort_key provided to the Iterator constructor overrides the sort_key attribute of the Dataset, or defers to it if None.
train – Whether the iterator represents a train set.
repeat – Whether to repeat the iterator for multiple epochs. Default: False.
shuffle – Whether to shuffle examples between epochs.
sort – Whether to sort examples according to self.sort_key. Note that shuffle and sort default to train and (not train).
sort_within_batch – Whether to sort (in descending order according to self.sort_key) within each batch. If None, defaults to self.sort. If self.sort is True and this is False, the batch is left in the original (ascending) sorted order.
device (str or torch.device) – A string or instance of torch.device specifying which device the Variables are going to be created on. If left as default, the tensors will be created on cpu. Default: None.
​'''
torchtext.data.Iterator(dataset, batch_size, sort_key=None, device=None, batch_size_fn=None, train=True, repeat=False, shuffle=None, sort=None, sort_within_batch=None)

'''
Create Iterator objects for multiple splits of a dataset.
​
Parameters: 
datasets – Tuple of Dataset objects corresponding to the splits. The first such object should be the train set.
batch_sizes – Tuple of batch sizes to use for the different splits, or None to use the same batch_size for all splits.
keyword arguments (Remaining) – Passed to the constructor of the iterator class being used.
​'''
splits(datasets, batch_sizes=None, **kwargs)
```

