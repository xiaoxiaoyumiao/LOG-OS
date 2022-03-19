# Miscellaneous

```python
# tokenize: cut text into tokens
from nltk.tokenize import sent_tokenize, word_tokenize
# sentence as token
sentences = sent_tokenize(document)
# word as token
sentences = [word_tokenize(sent) for sent in sentences]

# POS tagging
from nltk.tag import pos_tag
sentences = [pos_tag(sent) for sent in sentences]

# noun phrase chunking
# the sentence fed as input should be POS-tagged
sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),
 ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]
# a regex-like expression for matching noun phrases
# you can design more delicate regex rules
grammar = "NP: {<DT>?<JJ>*<NN>}" 
cp = nltk.RegexpParser(grammar) 
# parse the sentence to get a nltk.tree.Tree object as result
result = cp.parse(sentence) 
# output:
(S
  (NP the/DT little/JJ yellow/JJ dog/NN)
  barked/VBD
  at/IN
  (NP the/DT cat/NN))
  
# The tree nodes are trees and tuples.
# A tree is a sequence of leaves and subtrees,
# so you can iterate over it and index on it.
# You can access POS of a tree by its label method.
print(result[0].label())
# You can write a DFS to get absolute starting index of every tree node!

from nltk.tree import Tree
def dfs(tree):
    state_stack = []
    word_list = []
    np_list = []
    # node is a nltk tree
    def create_state(node):
        state = {
            "node": node,
            "index": 0
        }
        state["is_np"] = node.label() == "NP"
        state["start"] = len(word_list)
        return state
    def parse_tuple(node):
        word_list.append({
            "token": node[0],
            "type": node[1]
        })
    def finish_state(state):
        state["end"] = len(word_list)
        if state["is_np"]:
            np_list.append((state["start"], state["end"]))
        
    state_stack.append(create_state(tree))
    while len(state_stack) != 0:
        curr_state = state_stack[-1]
        node = curr_state["node"]
        index = curr_state["index"]
        if len(node) <= index: # end of node
            finish_state(state_stack.pop())
            continue
        
        if type(node[index]) == Tree:
            state_stack.append(create_state(node[index]))
        elif type(node[index]) == tuple:
            parse_tuple(node[index])
        curr_state["index"] += 1
        
    print(word_list, np_list)    
```

## Reference

\[1\] [http://www.nltk.org/api/nltk.html?highlight=tree\#nltk.tree.Tree](http://www.nltk.org/api/nltk.html?highlight=tree#nltk.tree.Tree)

\[2\] [https://www.nltk.org/book/ch07.html](https://www.nltk.org/book/ch07.html)

\[3\] [https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da](https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da)

