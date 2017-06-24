import numpy as np

class Perceptron:
    def __init__(self):
        self._w = None
        self._b = None

    def fit(self, x, y, lr=0.01, epoch=1000):
        """
        :param x 训练集的x
        :param y 训练集的y
        :param lr 学习率
        :param epoch 迭代次数
        """
        # 初始化
        x, y = np.asarray(x, np.float32), np.asarray(y, np.float32)
        self._w = np.zeros(x.shape[1])
        self._b = 0.


        for _ in range(epoch):
            # 此处的err可以看作所有点到直线的距离，只是不考虑乘以(-1/||w||)
            # 正确分类的err值是负数，错误分类的err为正数
            err = -y * self.predict(x, True)
            # 找出误差最大的err值
            idx = np.argmax(err)
            # 如果最大值小于0，则表示所有点对应的err值是负数，即全部被正确分类
            if err[idx] < 0:
                break
            # 计算梯度
            delta = lr * y[idx]
            self._w += delta * x[idx]
            self._b += delta

    # 当前w,b下的训练结果
    def predict(self, x, raw=False):
        """
        :param x:
        :param raw: Fasle则进行sign函数处理，True则返回原数据
        :return:
        """
        x = np.asarray(x, np.float32)
        y_pred = x.dot(self._w) + self._b
        if raw:
            return y_pred
        return np.sign(y_pred).astype(np.float32)