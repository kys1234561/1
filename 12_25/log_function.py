#对数
import matplotlib.pyplot as plt
import  numpy as np

x = np.arange(0.01,10,0.01)
y1 = np.log(x)#python以e为底
y2 = np.log(x)/np.log(0.5)
plt.plot(x,y1,c='red')
plt.plot(x,y2,c='yellow')
plt.show()
