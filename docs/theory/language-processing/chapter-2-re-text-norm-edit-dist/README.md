# Chapter 2 RE, Text Norm, Edit dist.

## **Introduction**

**DEF** **text normalization** tasks involving converting text to a more convenient, standard form

* 大意就是所谓文本规范化或者结构化。

**EX** text normalization:

* **DEF** **tokenization of / tokenizing** words from _running text \(main text of a document, as distinguished from captions, titles, lists, etc. - Merriam Webster\)_ means to chopping up the text into pieces called **tokens**. A token is an instance of a sequence of characters in some particular document that are grouped together as a useful semantic unit for processing. 
  * reference: [Tokenization](https://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html)
  * 也就是说，将文本切分为某种语义单位的序列，切分所得序列的元素，也就是这些语义单位，叫做 token。token 并不一定是 word，例如一些惯用短语在特定语境下也可以成为单个 token。
  * 甚至 emoticons 和 hashtags 也可以成为 token。
* **DEF** **lemmatization** is the task of determining that two words are derived from the same _lemma \(a form of a word that appears as an entry in a dictionary and is used to represent all the other possible forms - Cambridge\)_. a **lemmatizer** maps a word to its lemma.
  * lemma 应该就是原型或者词典型。lemmatization 对于一些小语种很有必要。
* **DEF** **stemming** means stripping suffixes from the word.
* **DEF** **sentence segmentation** means breaking up texts into individual sentences.

### Regular Expressions

Please refer to [Regular Expressions](../../formal-languages/regular-expressions.md).

