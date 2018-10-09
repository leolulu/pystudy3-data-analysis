import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)

x = np.linspace(-10, 10, 200)
y1 = sp.stats.norm.pdf(x=x, loc=0, scale=2)

plt.plot(x,y1)
plt.hist(sp.stats.norm.rvs(loc=5, scale=2, size=200), bins=50, normed=True, color='red', alpha=0.5)

plt.show()
