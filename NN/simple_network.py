import numpy as np
# 参考代码：https://iamtrask.github.io/2015/07/12/basic-python-network/
# sigmoid函数
def nonlin(x, deriv=False):
    """
    :param x:
    :param deriv:是否是求导
    :return:
    """
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

loop = 1000
# 输入数据集
X = np.asarray([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])
# 输出数据集
y = np.asarray([[0, 0, 1, 1]]).T

np.random.seed(1)

# 初始化layer0到layer1的权重矩阵w
w = 2 * np.random.random((3, 1)) - 1
for _ in range(loop):

    # 前向传导
    layer0 = X

    layer1 = nonlin(np.dot(layer0, w))

    # 计算损失
    layer1_error = y - layer1

    # 计算梯度
    # 求导公式看：http://blog.csdn.net/pennyliang/article/details/6695355
    layer1_delta = layer1_error * nonlin(layer1, True)

    # 更新权重
    # 将每个店对应纬度上的点乘以更新值并求其和作为最后的权值增量
    w += np.dot(layer0.T, layer1_delta)
    # print(w)
    # break

print("Done")
print(layer1)
