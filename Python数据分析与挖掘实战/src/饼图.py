from matplotlib import pyplot as plt
import numpy as np

labels = ['Shit', 'Sss', 'Fuck', 'Sex']
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)

plt.pie(
    sizes,
    colors=colors,
    labels=labels,
    explode=explode,
    startangle=90,
    shadow=True,
    autopct='%1.1f%%'
)
plt.axis('equal')
plt.show()
