# coding:utf-8
import re
from collections import Counter

def words(text):
    # 匹配能组成单词的字符
    return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open("big.txt").read()))

# print(WORDS)

def P(word, ncount=sum(WORDS.values())):
    # P(A)
    return float(WORDS[word] / ncount)



def correction(word):
    return max(candidates(word), key=P)

def candidates(word):
    # 候选集合
    # 如果word是正确的单词，则返回该单词
    if known([word]):
        return word
    if known(edits1(word)):
        return known(edits1(word))
    elif known(edits2(word)):
        return known(edits2(word))
    # 上面这几行的作用等于下面这句，作者写的比较简洁
    # return known([word]) or known(edits1(word)) or known(edits2())

def known(words):
    # 过滤words集合中不是单词的元素
    return set(w for w in words if w in WORDS)

def edits1(word):
    """
    返回与word编辑距离为1的所有结果
    编辑距离为1是指 对word增删改以及两个字符互换，这种操作每次只能有一次
    每次操作而成的新单词组成一个集合
    :param word:
    :return:
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    # 删除一个字符
    deletes = [L + R[1:] for L, R in splits if R]
    # 置换字符
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    # 修改
    replaces = [L + letter + R[1:] for L, R in splits if R for letter in letters]
    # 增加
    inserts = [L + letter + R for L, R in splits for letter in letters]

    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    """
    返回与word编辑距离为1的所有结果
    :param word:
    :return:
    """
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

print(correction("finsh"))
print(correction("finiish"))