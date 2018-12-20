import pandas as pd
import numpy as np 
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

data = pd.read_excel('./datasets/主动暂停有欠费用户明细20181129.xlsx')



myfont=FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf',size=14)
sns.set(font=myfont.get_name(),style='whitegrid')


sns.countplot(data=data,x='分公司',hue='主副卡')

plt.show()