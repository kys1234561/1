#tanh激活函数
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-9,9.1,0.1)
y = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

plt.plot(x, y)
plt.show()