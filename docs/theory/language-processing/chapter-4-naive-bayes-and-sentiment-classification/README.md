# Chapter 4 Naive Bayes and Sentiment Classification

**DEF** **text categorization** is the task of assigning a label to an entire text.

**TASK** **sentiment analysis** is the extraction of sentiment.

Use handwritten rules can be fragile. Most are done via **supervised machine learning**, where we have a data set of input observations, each associated with some correct output\(a "**supervision signal**"\). The goal is to learn how to map an observation to a correct output.

**DEF** a **probabilistic classifier** gives the probability of the observation being in a class, in other words, a distribution.

**DEF**

* A **generative classifier** models how a class could generate some input data.
  * **EX** naive Bayes
* A **discriminative classifier** learn what features from the input are most useful to discriminate between possible classes.
  * **EX** logistic regression

