#sigmoid激活函数
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-9,100,0.1)
y = 1/(1+np.exp(-x))

plt.plot(x,y)
plt.show()
