import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(10,30,30)

plt.plot(data,'g--',label='Defualt')
plt.plot(data,'y-',drawstyle='steps-post',label='steps-post')

print(
    plt.xlim(0,29)
)


plt.legend()
plt.show()