from matplotlib import pyplot as plt
import numpy as np

# x = np.random.randint(20,50,(1,200),'int32')
x = [1,2,3,4,5,6,6,7,8,9,10,7,5,5,3]


plt.hist(x,15)
plt.show()