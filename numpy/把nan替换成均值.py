import numpy as np

t = np.arange(30).reshape((6,5)).astype('float')
t[3,3] = np.nan
print(t)
print('\n')

t_temp = t
t_temp[np.isnan(t_temp)] = 0

print(
    t
)
