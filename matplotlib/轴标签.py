import matplotlib.pyplot as plt
import numpy as np

plt.plot(
    np.random.randn(1000).cumsum()
)

plt.xticks([0,300,600,900,1200],['begin','shit','sas','you','end'],rotation=45)
plt.yticks([0,300,600,900,1200],['begin','shit','sas','you','end'],rotation=45)

plt.show()