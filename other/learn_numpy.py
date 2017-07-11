import pdb
import numpy as np
# asarray 把数组转成矩阵
a = [1,2,3,4,5]
x = np.asarray(a)
b = [1,-1,1,-1,1]
y = np.asarray(b)

# eye 生成n维的单位矩阵
aa = np.eye(2)
print(aa)
# x * n ：矩阵的每个元素乘以n
z = x * 3
print(z)  # z = [ 3  6  9 12 15]
# 矩阵x和矩阵y对应的元素相乘
z = x * y
print(z)
# 矩阵的乘法
z = x.dot(y)
print(z)
pdb.set_trace()
# np.zeros(shape) 生成一个长宽为shape的零矩阵, shape[0]为行,shape[1]为列
# zeros = np.zeros(x.shape[0])
# print(zeros)

y_ = x.dot(4) + 5
print(y, y_)
# maximum(x1, x2) x1和x2每个元素比较大小，输出大的值
m = np.maximum(0, y_ * y)
print(m)
# argmax(x)  找出最大值的下标或者索引
idx = np.argmax(y_)

print(idx)
# sign    sign函数判定
print(np.sign([-34,0,9,-1.1]))