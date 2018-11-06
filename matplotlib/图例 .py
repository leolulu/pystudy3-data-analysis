import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.random.randn(1000000).cumsum(),'r-.',label='one')
plt.plot(np.random.randn(1000000).cumsum(),'g--',label='two')
plt.plot(np.random.randn(1000000).cumsum(),'b.',label='three')

plt.legend()

plt.show()