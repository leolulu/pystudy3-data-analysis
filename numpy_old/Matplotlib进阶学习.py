import numpy as np
import matplotlib.pyplot as plt

plt.figure()

x = np.linspace(-100, 100, 200)
y = (np.random.randn(200) * 1000).astype('int64')
print(y)
y1 = x ** 2

plt.plot(x, y1, 'r')
plt.plot(x, y, 'b')
plt.show()
