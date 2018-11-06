import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 4,sharey=True)
for k in range(4):
    rand_array = np.random.randint(-1,2)
    axes[0][k].plot(rand_array, 'ko--')
    axes[1][k].plot(rand_array.cumsum(), 'go--')

plt.subplots_adjust(wspace=0)
plt.show()
