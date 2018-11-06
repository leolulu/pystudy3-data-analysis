import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure() #1.创建画布
ax1 = fig.add_subplot(2,2,1) #2.创建子图
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

x=np.arange(100)
ax1.plot(x,x) #3.用子图作画
ax2.plot(x,-x)
ax3.plot(x,x**2)

ax4.plot(np.random.randn(50).cumsum(), 'k--')

plt.show() #4.显示