# Miscellaneous

## Basics

spaCy 有几个用于自然语言处理的基本类。首先看一段典型的使用代码：

```python
import spacy

texts = [
    "Net income was $9.4 million compared to the prior year of $2.7 million.",
    "Revenue exceeded twelve billion dollars, with a loss of $1b.",
]

nlp = spacy.load("en_core_web_sm")
for doc in nlp.pipe(texts, disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"]):
    # Do something with the doc here
    print([(ent.text, ent.label_) for ent in doc.ents])
```

* 通过 `load` 方法得到的 `nlp` 对象是一个 `Language` 实例。它可以加载指定的语言模型，例如此处的 `en_core_web_sm` 。模型需要另外下载，请参考官方的 Installation 指导。
* 通过 `pipe` 方法得到的 `doc` 是 `Doc` 实例，它也可以通过将 `Language` 实例直接作用于文本字符串得到：`doc = nlp("Some text")` 。此处的参数是一个文本字符串的 iterable（在这段代码中使用了列表），这使得模型可以批量处理数据，在使用 CUDA 时就可以提升效率。
* `pipe` 中的 `disable` 参数实现对部分模块的禁用。`Language` 加载的模型事实上包含了多个与语言处理相关的模块（例如此处列出的 tagger，parser 等），每个模块（文档称 component）与特定的处理任务相关联。在处理文本时，模型默认将包含的所有模块都作用于文本，如果你只需要某类特定的处理结果（例如 POS 标注信息），可以通过多种方式只加载或使用部分模块，提高处理效率。
  * 关于处理效率问题可参考 ref: \[4\]\[5\]
* `Span` 是 `Doc` 的一个子序列。`Token` 则代表了 `Doc` 的单个元素。它们都是 doc 的 view 对象，也就是说它不存储额外数据。模型的处理结果常使用 `Span` 和 `Token` 表示（如 noun\_chunks 是一个 Span 的列表）。
  * `Span` 具有 `start` 和 `end` 属性，可以方便地获取其在原文中的起止位置。此外它也可以像一般 sequence 一样操作。

## Pipelining

使用 `as_tuples` 参数可以允许输入的文本附带一个 context 以存储附加的元数据，这样在打包为 batch 后也可以方便地访问这些数据。

```text
TODO
```

## Common Tasks

```python
# noun phrase chunk
>>> from spacy.en import English
>>> nlp = English()
>>> doc = nlp(u'The cat and the dog sleep in the basket near the door.')
>>> for np in doc.noun_chunks:
>>>     np.text
u'The cat'
u'the dog'
u'the basket'
u'the door'
```

## Reference

\[1\] about disabling components:  [https://spacy.io/usage/processing-pipelines\#disabling](https://spacy.io/usage/processing-pipelines#disabling)

\[2\] [https://spacy.io/api/doc](https://spacy.io/api/doc)

\[3\] language models: [https://spacy.io/models/en](https://spacy.io/models/en)

\[4\] [https://stackoverflow.com/questions/49702372/speed-up-spacy-named-entity-recognition](https://stackoverflow.com/questions/49702372/speed-up-spacy-named-entity-recognition)

\[5\] [https://github.com/explosion/spaCy/issues/1508](https://github.com/explosion/spaCy/issues/1508)

\[6\] [https://spacy.io/api/span](https://spacy.io/api/span)

\[7\] noun chunks: [https://stackoverflow.com/questions/33289820/noun-phrases-with-spacy](https://stackoverflow.com/questions/33289820/noun-phrases-with-spacy)

