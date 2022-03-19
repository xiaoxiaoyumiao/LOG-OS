# Chapter 2 Entropy, Relative Entropy & Mutual Information

* **DEF** **Entropy** $$H(x)$$ of a discrete random variable X is defined by $$H(X) = - \sum p(x) \log p(x)$$ 
  * **PROP** $$H(X)\geq 0$$ 
* **DEF** **Joint Entropy** $$H(X,Y)$$ of a pair of discrete random variables $$(X, Y)$$with a joint distribution $$p(x,y)$$is defined as $$H(X,Y) = -\sum_{x,y} p(x,y)\log p(x,y)$$.
* **DEF** **Conditional Entropy** $$H(Y|X)$$is defined as: $$H(Y|X) = \sum p(x)H(Y|X=x) = -\sum p(x) \sum p(y|x) \log p(y|x) = - \sum_{x,y} p(x,y) \log p(y|x)$$
* **THEOREM** $$H(X,Y) = H(X)+H(Y|X)$$.
  * **COR** $$H(X,Y|Z) = H(X|Z)+H(Y|X,Z)$$
  * **PROOF** $$H(X,Y,Z) = H(X,Y|Z)+H(Z)=H(Y|X,Z)+H(X,Z) =H(Y|X,Z)+H(X|Z)+H(Z)$$
* **DEF** **Kullback-Leibler Distance / Relative Entropy** $$D(p||q)=\sum p(x) \log \frac{p(x)}{q(x)}$$.
  * **PROP** $$0\log\frac{0}{0} = 0, 0\log \frac{0}{q} = 0, p\log \frac{p}{0} = +\infty$$.
* **DEF** **Mutual Information** $$I(X;Y)$$is the relative entropy between the joint distribution and the product distribution $$p(x)p(y)$$:$$I(X;Y) = D(p(x,y)||p(x)p(y))$$.
  * **PROP** $$I(X;Y) = \sum_{x,y} p(x,y) \log \frac{p(x,y)}{p(x)} = H(X) - H(X|Y)$$.
  * **PROP** $$I(X;X) = H(X)$$.
  * **PROP** $$I(X;Y) = H(X)+H(Y)-H(X,Y)$$
  * It's easy to see that relations between entropy, joint entropy, conditional entropy and mutual information can be represented by a Venn graph.

