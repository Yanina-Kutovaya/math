import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
k = [1, 1.5]

plt.plot(x, np.cos(k[0] * x), label='y=cos(x)')
plt.plot(x, np.cos(k[1] * x), label='y=cos(1.5x)')
plt.legend(loc='best')
plt.show()
