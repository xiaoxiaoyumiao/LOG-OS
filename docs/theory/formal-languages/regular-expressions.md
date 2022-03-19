# Regular Expressions

**DEF** **Regular Expression, pattern, corpus**

* A regular expression search function will search through the corpus, returning all texts that match the pattern.

Basic patterns: \(note: `//` is used to mark its content as a RE pattern but is not part of the pattern\)

* sequence of digits and Latin letters \(and other special characters except for these listed below\): search for an identical substring
  * `/Buttercup/` search for a substring `Buttercup`
* `[]` specifies a disjunction of characters to match
  * `/[Bb]/` matches `B` or `b`
* `[-]` specifies a range of characters
  * `/[a-d]/` matches `a`, `b`, `c` or `d`.
  * `/[0-9]/` matches an arbitrary digit
  * `/[A-Z]/` matches an arbitrary upper case letter
* `[^]` specifies any character that does _not_ match expressions following `^` symbol
  * `^` must be the first symbol after `[`, otherwise it simply matches a `^`
  * 也就是说在中括号内部的开头放一个 `^` 就可以对要匹配的内容取反
  * `/[^A-Z]/` matches any character that is not an upper case letter
  * `/[e^]/` matches a letter `e` or `^`
* `?` specifies the preceding character to be optional.
  * `/colou?r/` matches `color` or `colour`.
* `*` \(Kleene star\) means "zero or more occurrences"
  * `/a/` matches null, `a`, `aa`, etc.
* `+` \(Kleene plus\) means "one or more occurrences"
  * `/a/` matches `a`, `aa`, etc.
* Anchors anchor RE to particular places in a string
  * 也就是定位用
  * `^` matches the start of a line.
    * `/^The/` matches a `The` at the start of a line
  * `$` matches the end of a line
    * `/.$/` matches a `.` at the end of a line
* `\b` matches a word boundary, while `\B` matches a non-boundary
  * a word is a sequence of digits, underscores or letters
* `|` is a **disjunction** operator matching with patterns at either side
  * `/cat|dog/` matches `cat` or `dog`

**DEF** **false positive** - incorrectly matched

**DEF** **false negative** - incorrectly missed

**DEF** increasing **precision** - minimizing false positives

**DEF** increasing **recall** - minimizing false negatives

* `s///` works as a **substitution** that replace a string with another
  * `s/colour/color` replaces `colour` with `color`
* If we need to refer to a particular subpart of a matching result we can use **number** operator:
  * `s/([0-9]+)/<\1>` encloses every number with a `<>`. `\1` refers to the number captured by `()`.
  * `/(.*) are \1/` will match `cats are cats` but not `cats are dogs`.
* `()` serves as a **capture group**. strings matching the RE inside are stored in numbered registers. Data in registers can be referred to through number operators like `\1`, `\2`, etc.
* sometimes we use `()` only to specify priority of operators. In that case we use a **non-capturing group** `(?:)`.
  * `/(?:some|a few) people/`

**DEF** **lookahead assertions** help to look ahead in the text without advancing the match cursor.

* （这似乎已经不是形式语言中的正则表达式语法了）
* `(?=pattern)` returns true if `pattern` occurs
  * 理解时应当有 match cursor 的概念。简单来说就是 `pattern` 匹配到的东西不会作为结果的一部分，而且因为是在 look ahead，它完成匹配后被匹配串的匹配状态还是和匹配 `pattern` 前一样。\`
* `(?!pattern)` returns true if `pattern` does not occur
  * `/^(?!Volcano)[A-Za-z]+/` 匹配所有不是 `Volcano` 的单词。

## reference

[\[1\] Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/)

