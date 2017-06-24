from util import gen_two_clusters, visualize2d
from perceptron import Perceptron
import numpy as np
data, labels = gen_two_clusters(size=20000)

perceptron = Perceptron()
perceptron.fit(data, labels)

result = (perceptron.predict(data) == labels).mean()

print(result)

visualize2d(perceptron, data, labels)