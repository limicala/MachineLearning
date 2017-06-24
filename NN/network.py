import numpy as np
import random

class Network(object):


    def __init__(self, sizes):
        """
        :param sizes: list 每层的神经元个数
        """
        self.num_layers = len(sizes)
        self.sizes = sizes
        # randn产生的是标准正态分布的数
        self._b = [np.random.randn(y, 1) for y in sizes[1:]]
        self._w = [np.random.randn(y, x)
                   for x, y in zip(sizes[:-1], sizes[1:])]

    # 批梯度下降法
    # 当数据量大的时候
    # 每次分成许多个小样本分别来算梯度
    def SGD(self, train_data, epochs, min_batch_size, learn_rate,
            test_data=None):
        """

        :param train_data: list
        :param epochs: 迭代次数
        :param min_batch_size: 最小批大小
        :param learn_rate: 学习率
        :param test_data: 测试数据集
        :return:
        """
        train_data = list(train_data)
        n = len(train_data)

        if test_data:
            test_data = list(test_data)
            n_test = len(test_data)

        for j in range(epochs):
            # 将数据集打乱
            random.shuffle(train_data)
            # 数据集分批
            mini_batches = [
                train_data[k : k + min_batch_size]
                for k in range(0, n, min_batch_size)
            ]
            # 分别处理，计算梯度
            for batch in mini_batches:
                self.update_mini_batch(batch, learn_rate)
            # if test_data:
            #     print("")
            if test_data:
                print("Epoch {} : {} / {}".format(j,self.evaluate(test_data),n_test));
            else:
                print("Epoch {} complete".format(j))

    def update_mini_batch(self, batch, rate):
        # 初始化
        ndelta_b = [np.zeros(b.shape) for b in self._b]
        ndelta_w = [np.zeros(w.shape) for w in self._w]
        for x, y in batch:
            # 返回该点求得的整个神经网络的梯度
            delta_nb , delta_nw = self.backprop(x, y)
            ndelta_b = [nb+dnb for nb, dnb in zip(ndelta_b, delta_nb)]
            ndelta_w = [nw+dnw for nw, dnw in zip(ndelta_w, delta_nw)]
        # 将该批的每一个点的梯度相加求平均值
        self._w = [w-(rate/len(batch))*nw
                   for w, nw in zip(self._w, ndelta_w)]
        self._b = [b-(rate/len(batch))*nb
                   for b, nb in zip(self._b, ndelta_b)]

    # 返回该点求得的整个神经网络的梯度
    def backprop(self, x, y):
        # 初始化
        ndelta_b = [np.zeros(b.shape) for b in self._b]
        ndelta_w = [np.zeros(w.shape) for w in self._w]
        # 前向传导
        # 第0层，输入层
        activation = x
        # 存储所有层的输出向量
        activations = [x]
        # 存储所有的z向量，这里理解为是上一层输出的向量乘以权值作为的输入的向量
        zs = []
        for b, w in zip(self._b, self._w):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        # 反向传播
        # 先计算倒数第一层的梯度
        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])

        ndelta_b[-1] = delta
        ndelta_w[-1] = np.dot(delta, activations[-2].T)

        # 计算其他层的梯度
        # 相邻两层的梯度有关系
        for back_index in range(2, self.num_layers):
            z = zs[-back_index]
            sp = sigmoid_prime(z)
            error = np.dot(self._w[-back_index + 1].T, delta)
            delta = error * sp
            ndelta_b[-back_index] = delta
            ndelta_w[-back_index] = np.dot(delta, activations[-back_index - 1].T)
        return (ndelta_b, ndelta_w)

    def evaluate(self, test_data):
        """Return the number of test inputs for which the neural
        network outputs the correct result. Note that the neural
        network's output is assumed to be the index of whichever
        neuron in the final layer has the highest activation."""
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        return (output_activations-y)

    def feedforward(self, a):
        """Return the output of the network if ``a`` is input."""
        for b, w in zip(self._b, self._w):
            a = sigmoid(np.dot(w, a)+b)
        return a
#### Miscellaneous functions
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))

if __name__ == '__main__':
    pass