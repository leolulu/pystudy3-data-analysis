import matplotlib.pyplot as plt
from pandas_datareader import data

gafataDict = {'谷歌': 'GOOG', '亚马逊': 'AMZN', 'Facebook': 'FB',
              '苹果': 'AAPL', '阿里巴巴': 'BABA', '腾讯': '0700.hk'}

start_date = '2017-01-01'
end_date = '2018-01-01'

a = data.get_data_yahoo(gafataDict['阿里巴巴'], start_date, end_date)

a['change'] = (a['Close']-a['Close'][0])/a['Close'][0]

plt.plot(a['Close'])
plt.plot(a['change']*200)

plt.title('BAKA')
plt.grid(True)
plt.legend(loc='best')

print(
    a.index
)

plt.show()