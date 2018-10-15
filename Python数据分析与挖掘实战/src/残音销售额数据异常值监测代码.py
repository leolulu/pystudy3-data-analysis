import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_excel('./data/data.xlsx')
print(data)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
p = data.boxplot()
print(

)
