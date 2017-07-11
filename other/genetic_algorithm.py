import random
import math
"""
思路：
初始化一个Population，设定好适应函数（Fitness Function）

依据适应度淘汰部分染色体，随机从被淘汰的群体随机挑出一些染色体保留到下一代

剩下的随机杂交，变异，保持Population的染色体数量不变

到达n代之后，选出适应度最高的染色体作为答案

"""
# 具体问题
# 求解函数 f(x) = x + 10*sin(5*x) + 7*cos(4*x) 在区间[0,9]的最大值。

# 自然选择适应度排在20%前面的染色体
select_rate = 0.2
# 随机从适应度不高的80%里挑
random_select_rate = 0.5
# 变异概率
mutation_rate = 0.01
# 人口规模
population_size = 300
# 染色体长度，即问题的解集的大小转换成二进制的长度
chromosome_length = 17
def random_chromosome(length):
    """
    随机生成长度为length的染色体
    :param length: 
    :return: int  
    """
    chromosome = 0
    for i in range(length):
        chromosome |= (1 << i) * random.randint(0, 1)
    return chromosome
def random_population(length = chromosome_length, count = population_size):
    """
    随机生成初代人口
    :param length: 染色体长度
    :param count: 染色体数目
    :return: list element->(chromosome)
    """
    return [random_chromosome(length) for _ in range(count)]

def fitness(chromosome):
    """
    计算适应度
    :param chromosome:  
    :return: float
    """
    x = decode(chromosome)
    # f(x) = x + 10 * sin(5 * x) + 7 * cos(4 * x)
    return x + 10 * math.sin(5 * x) + 7 * math.cos(4 * x)

def decode(chromosome):
    """
    解码，将二进制数转换成属于[0,9]的实数
    :param chromosome: 
    :return:  Phenotype real value
    """
    return chromosome * 9.0 / (2 ** chromosome_length - 1)

def crossover(parents : list):
    """
    杂交
    :param parents: 
    :return: next population
    """
    children = []
    parents_size = len(parents)
    # 需要繁殖的孩子数量
    target_count = population_size - parents_size
    for _ in range(target_count):
        # 选定两个不同的染色体
        male, female = random.sample(range(0, parents_size), 2)
        # 随机选取交叉点
        cross_pos = random.randint(0, chromosome_length)
        # 生成掩码，方便位操作
        mask = 0
        for i in range(cross_pos):
            mask |= (1 << i)
        male = parents[male]
        female = parents[female]

        # 孩子将获得父亲在交叉点前的基因和母亲在交叉点后（包括交叉点）的基因
        child = ((male & mask) | (female & ~mask)) & ((1 << chromosome_length) - 1)
        children.append(child)

    return parents + children

def selection(population : list):
    """
    自然选择
    :param population:
    return the rest of the current population
    :return: list element->(chromosome) 
    """
    # 根据适应度从大到小排序
    graded = sorted(population, key=fitness, reverse=True)
    threshold_index = math.floor(len(graded) * select_rate)
    # 根据自然选择率找出适应度阈值
    threshold = graded[threshold_index]
    def select(chromosome):
        # 适应度大于或等于阈值，则存活
        if chromosome >= threshold:
            return True
        # 随机选择概率
        elif random.random() < random_select_rate:
            return True
        else:
            return False

    return list(filter(select, graded))

def mutation(chromosome):
    """
    变异
    随机改变个体中的某个基因
    :param chromosome: 
    :return: 
    """
    if random.random() < mutation_rate:
        i = random.randint(0, chromosome_length - 1)
        chromosome ^= 1 << i
    return chromosome

def evovle(population):
    parents = selection(population)
    new_population = crossover(parents)
    new_population = list(map(mutation, new_population))
    return new_population

# 初代
population = random_population()

for _ in range(300):
    population = evovle(population)

graded = sorted(population, key=fitness, reverse=True)

print(decode(graded[0]))