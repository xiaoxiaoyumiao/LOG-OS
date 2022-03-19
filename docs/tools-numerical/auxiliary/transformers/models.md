# Models

## PyTorch Models

其本质就是一个 torch module，如果需要嵌入其他模型，正常地像其他 module 一样使用即可。

```python
from transformers import BertTokenizer, BertForMaskedLM
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')

inputs = tokenizer("The capital of France is [MASK].", return_tensors="pt")
labels = tokenizer("The capital of France is Paris.", return_tensors="pt")["input_ids"]

outputs = model(**inputs, labels=labels)
loss = outputs.loss
logits = outputs.logits
```

## Reference

\[1\] [https://huggingface.co/transformers/model\_doc/bert.html\#](https://huggingface.co/transformers/model_doc/bert.html#)

\[2\] [https://huggingface.co/transformers/main\_classes/output.html\#transformers.modeling\_outputs.MaskedLMOutput](https://huggingface.co/transformers/main_classes/output.html#transformers.modeling_outputs.MaskedLMOutput)

