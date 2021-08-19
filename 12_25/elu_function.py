#elu激活函数
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3.1, 0.1)
len1 = len(x)
y = np.zeros(shape=(len1,1))#shape固定大小
for i in range(0,len1):
    if x[i] < 0:
        y[i] = 0.5 * (np.exp(x[i])-1)
    else:
        y[i] = x[i]

plt.plot(x,y)
plt.show()