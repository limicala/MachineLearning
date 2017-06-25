# 单词纠错

贝叶斯模型 P(A|B) = ( P(A) * P(B|A) ) / P(B)

事件A为打字员打出正确单词A的概率

事件B为打字员打出错误单词B的概率

P(A|B)为在打字员误写成B的前提下，原本想写的是A的概率

P(B|A)为在打字员想打A的前提下，却打出B的概率

故我们现在需要求的是P(A|B))

P(A|B) = ( P(A) * P(B|A) ) / P(B)

P(B) B的集合是无限大的，即是错误单词是无限多的，所以可以假设打出任意一个错误单词的概率是一样的

所以
P(A|B) = ( P(A) * P(B|A) )

而P(B|A) 是需要大量的输入错误的数据集，这种数据集作者在文章也有提到[一些](http://aspell.net/test/)

不过链接里面的数据集还是太小了，数据集过小会导致没考虑到许多错误单词和概率的设定

所以把P(B|A)忽略

现在的话

P(A|B) 约等于 P(A)

P(A)的概率可以看作是一篇文章里面单词A出现的概率

具体实现看作者[博客链接](http://norvig.com/spell-correct.html)

# 相关链接
[How to Write a Spelling Corrector](http://norvig.com/spell-correct.html)

[[译]如何编写一个拼写纠错器](https://segmentfault.com/a/1190000009826061)