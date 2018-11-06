import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

for j in range(2):
    for k in range(2):
        axes[j][k].hist(
            np.random.randn(500),
            bins=50,
            color='k',
            alpha=0.5
        )
plt.subplots_adjust(wspace=0, hspace=0)

plt.show()
