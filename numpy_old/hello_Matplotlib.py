import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
print(fig)

# ax1 = fig.add_subplot(2, 2, 1)

dir_array = np.random.randn(100)
print(dir_array)

plt.plot(dir_array)
plt.show()
