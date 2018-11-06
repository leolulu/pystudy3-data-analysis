import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# x = np.random.randn(10)
D = pd.DataFrame([1,2,3,4,5]).T

D.plot(kind='box')


print(D)
plt.show()
