import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5,0.01)
y1 = 2 ** x
y2 = 1/2 ** x
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()