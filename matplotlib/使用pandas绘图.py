import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 4).cumsum(0),
    columns=['A', 'B', 'C', 'D'],
    index=np.arange(0, 100, 10)
)

df.plot()

plt.show()