# tokenizer

tokenizer 的主要功能可以用 tokenize 和 encode 来描述。tokenize 将文本切分为 token，encode 则将（已切分或未切分的） token 按照词表转换为（或者说映射到）数值 id。tokenizer 的`tokenize` 和 `encode` 分别实现上述功能， `__call__` 方法基本上是 encode，并返回包含更多的控制信息的 `BatchEncoding` 对象。

当 `__call__` 接收一个 `List[str]` 作为参数时，它默认会把参数理解为一个文本 batch，所以如果传入的是已切分的 token 序列，就需要设置 `is_split_into_words` 参数为真。但 `encode` 方法并不需要，它默认把 `List[str]` 理解为已切分的 token 序列。

`encode` 有一个反向的方法 `decode` ，可以把已编码的 id 序列还原为文本字符串。但注意 tokenize 本身不是可逆的，tokenize 包含大小写归一化、OOV 单词处理等过程。对于 BERT tokenizer 等会做 subword 切分的 tokenizer，`decode` 可以帮助省去 subword 拼接的过程；`decode` 也会对标点进行合适的处理。

由于 token 既可以抽象地指代文本处理中的最小对象（对于 tokenizer 来说，一般就是 word 或 subword），也可以指代具体的字符串形式的（采用字符编码的） 最小对象，本文可能会在这两种意义上模糊地使用 token 这个词，但请留意这一概念上的分歧。

`BatchEncoding` 对象继承自 python dict。

tokenizer 是支持对一个 batch 的文本做 tokenize 和 encode 的。

`attention_mask` 是一个对文本做 batching 时会用到的参数。假设有若干长度不同的序列要放入同一个 batch，并且不做截断，那么只能对短的序列做 padding。但对于 BERT 这样的基于 attention 的非自回归的模型而言，输入连同 padding 会一起被 attention 机制作用，而我们不期望 padding 信息造成干扰。通过 attention mask 可以告诉模型，输入数据的哪些部分不需要参与 attention 计算（例如 padding 的部分）。直接调用 tokenizer 得到的 `BatchEncoding` 里默认包含 `attention_mask` 。它是一个和产生的 id 序列长度相同的 01 序列，1 代表对应位置的 token 将参与 attention 运算，0 代表相反。

如果希望把序列 padding 到一个统一的长度，可以考虑 `padding` 参数。它不仅支持把一个 batch 内的 sequence 补齐到 batch 内最长 sequence 的长度，也支持补齐到一个给定的任意长度。通过 `truncation` 参数则可以执行截断到给定长度。这个给定长度由参数 `max_length` 控制。

直接调用 tokenizer 返回的 id 序列默认是一个 python list。通过 `return_tensors` 参数可以要求 tokenizer 返回特定数值框架中的数值类型。`pt` 代表 PyTorch 的 `Tensor`，`tf` 代表 TensorFlow 的 `Tensor`，`np` 代表 NumPy 的 `ndarray`。

```python
# load a tokenizer
global_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
hamlet = "To be or not to be, that is the question."

# tokenize, encode and decode
result = global_tokenizer.tokenize(hamlet)
print(result)
['to', 'be', 'or', 'not', 'to', 'be', ',', 'that', 'is', 'the', 'question', '.']
result = global_tokenizer.encode(result)
print(result)
[101, 2000, 2022, 2030, 2025, 2000, 2022, 1010, 2008, 2003, 
1996, 3160, 1012, 102]
result = global_tokenizer.decode(result)
print(repr(result))
'[CLS] to be or not to be, that is the question. [SEP]'

# subword example
hysteria = "a psychoneurosis marked by emotional excitability and disturbances " \
    "of the psychogenic, sensory, vasomotor, and visceral functions"
result = global_tokenizer.tokenize(hysteria)
print(result)
['a', 'psycho', '##ne', '##uro', '##sis', 'marked', 'by', 'emotional', 
'ex', '##cit', '##ability', 'and', 'disturbances', 'of', 'the', 'psycho', 
'##genic', ',', 'sensory', ',', 'va', '##som', '##oto', '##r', ',', 'and', 
'vis', '##cera', '##l', 'functions']

# directly encoding is supported
result = global_tokenizer.encode(hamlet)
print(result)
[101, 2000, 2022, 2030, 2025, 2000, 2022, 1010, 2008, 2003, 
1996, 3160, 1012, 102]

result = global_tokenizer(hamlet)
print(result)
{'input_ids': [101, 2000, 2022, 2030, 2025, 2000, 2022, 1010, 2008, 2003, 
1996, 3160, 1012, 102], 
'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}

# Tokenized text is not properly encoded.
# Every token is treated as an individual sentence.
result = global_tokenizer.tokenize(hamlet)
result = global_tokenizer(result)
print(result)
{'input_ids': [[101, 2000, 102], [101, 2022, 102], [101, 2030, 102], ...
result = global_tokenizer.tokenize(hamlet)
# use of is_split_into_words
result = global_tokenizer(result, is_split_into_words=True)
print(result)
{'input_ids': [101, 2000, 2022, 2030, 2025, 2000, 2022, 1010, 2008, 2003, 
1996, 3160, 1012, 102], 
'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}

# use of padding, truncation and max_length
result = global_tokenizer(hamlet,padding='max_length', max_length=20)
print(result)
{'input_ids': [101, 2000, 2022, 2030, 2025, 2000, 2022, 1010, 2008, 2003, 
1996, 3160, 1012, 102, 0, 0, 0, 0, 0, 0], 
'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]}

result = global_tokenizer(hamlet, truncation=True, max_length=10)
print(result)
{'input_ids': [101, 2000, 2022, 2030, 2025, 2000, 2022, 1010, 2008, 102], 
'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}

# use of return_tensors
result = global_tokenizer(hamlet, return_tensors="pt")
print(result)
{'input_ids': tensor([[ 101, 2000, 2022, 2030, 2025, 2000, 2022, 1010, 
2008, 2003, 1996, 3160, 1012,  102]]), 
'token_type_ids': tensor([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), 
'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}

# additional flags to control returned value
result = global_tokenizer(hamlet, 
    return_token_type_ids=False, 
    return_attention_mask=False)
print(result)
{'input_ids': [101, 2000, 2022, 2030, 2025, 2000, 2022, 1010, 2008, 2003, 
1996, 3160, 1012, 102]}
​
```

## Reference

\[1\] [https://huggingface.co/transformers/main\_classes/tokenizer.html](https://huggingface.co/transformers/main_classes/tokenizer.html)

