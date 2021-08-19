#修正的relu函数
import matplotlib.pyplot as plt
import numpy as np
y = []
x = np.arange(-9,9.1,0.1)
for i in x:
    j = max(0.1*i,i)
    y.append(j)
plt.plot(x,y)
plt.show()