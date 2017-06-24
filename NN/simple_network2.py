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

loop = 10000
# 输入数据集
X = np.asarray([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])
# 输出数据集
y = np.asarray([[0, 1, 1, 0]]).T

np.random.seed(1)
# 构造一个神经网络，3层，分别有[3,4,1]个神经元
w0 = 2 * np.random.random((3, 4)) - 1
w1 = 2 * np.random.random((4, 1)) - 1

for index in range(loop):

    # 前向传导
    layer0 = X
    layer1 = nonlin(np.dot(layer0, w0))
    layer2 = nonlin(np.dot(layer1, w1))

    # 从后面开始求损失函数
    # Layer2的损失函数
    layer2_error = y - layer2

    if index % (loop // 10) == 0:
        print("Error" + str(np.mean(np.abs(layer2_error))))

    # 求梯度
    layer2_delta = layer2_error * nonlin(layer2, deriv=True)
    # Layer1的损失函数
    # 相邻两层的损失函数是有关系的，看林轩田的机器学习技法可知
    layer1_error = layer2_delta.dot(w1.T)
    # 求梯度
    layer1_delta = layer1_error * nonlin(layer1, deriv=True)

    # 更新
    w1 += np.dot(layer1.T, layer2_delta)
    w0 += np.dot(layer0.T, layer1_delta)

