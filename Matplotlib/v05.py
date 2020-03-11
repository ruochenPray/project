'''
numpy.histogram() 函数是数据的频率分布的图形表示。
水平尺寸相等的矩形对应于类间隔，称为bin，变量 height 对应于频率

numpy.histogram() 函数将输入数组和 bin 作为两个参数。bin 数组中的连续元素用作每个 bin 的边界

Matplotlib 可以将直方图的数字表示转换为图形
'''
import numpy as np
import matplotlib.pyplot as plt

a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
# np.histogram(a, bins=[0,20,40,60,80,100])
# hist,bins = np.histogram(a, bins=[0,20,40,60,80,100])
# print(hist)
# print(bins)

plt.hist(a, bins=[0,20,40,60,80,100])
plt.title('histogram')
plt.show()