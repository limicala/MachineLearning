# coding:utf-8
import re
from collections import Counter

def words(text):
    # 匹配能组成单词的字符
    return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open("big.txt").read()))

print(WORDS.values())

def P(word, ncount=sum(WORDS.values())):
    # P(A)
    return float(WORDS[word] / ncount)



def correction(word):
    return max(candidates(word), P)

def candidates(word):
    # 候选集合
    return None

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
    pass

def edits2(word):
    pass

