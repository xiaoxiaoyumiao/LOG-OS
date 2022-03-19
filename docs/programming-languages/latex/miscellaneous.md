# Miscellaneous

```text
数字枚举：
\begin{enumerate}
\item 第一项
\item 第二项
\end{enumerate}

公式：
大体和markdown公式语法一致
方程：独立成块，居中分布
带星号的equation环境不会有序号计数
\begin{equation*}
\end{equation*}
不带星号的则会有序号
增量符号：\increment
积分 \int 微分 \dif
逻辑与 \land
\text 嵌入文本


引用：
每个bibtex格式的参考文献会带有一个可引用的唯一标识符，用作cite的参数
仅带序号的引用：
（逗号分隔引用多篇文献）
\cite{b1, b2, b3} 
带人名的引用：
\citet

表格：
一个比较复杂的表格长这样：
\begin{tabular}{l|l|l|l|l|l|l|l}
\hline
 & \multirow{2}{*}{Method2} & \multicolumn{3}{|l}{Data1} & \multicolumn{3}{|l}{Data2} \\
\cline{3-8}
~ & ~ & P & R & F & P & R & F \\
\hline
Method11 & Method21 & 6.60 & 6.25 & 6.92 & 6.11 & 5.49 & 5.80 \\
\hline
\end{tabular}

{l|l|l...}是用来描述整个表格的布局的，1个l代表一个内容左对齐的列，|代表一个竖直分隔线。
类似地c可以代表一个内容居中的列。不写|就不会有分隔线。
表格元素都用&分隔，行之间用\\用分隔，\hline用来添加一个水平的分隔线。
```

## References

\[1\] [https://www.caam.rice.edu/~heinken/latex/symbols.pdf](https://www.caam.rice.edu/~heinken/latex/symbols.pdf)

\[2\] [https://oeis.org/wiki/List\_of\_LaTeX\_mathematical\_symbols](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)

\[3\] [https://zhuanlan.zhihu.com/p/191641301](https://zhuanlan.zhihu.com/p/191641301)

