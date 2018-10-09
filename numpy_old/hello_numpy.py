import numpy as np

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print('list:', list1)
diy_array = np.array(list1)
print(diy_array)

print(diy_array.ndim)
print(diy_array.shape)
print(diy_array.dtype)

print(
    diy_array[(diy_array > 5) & (diy_array < 9)]
)

common_array = np.random.randn(3, 4, 5).astype('float16')

print(
    np.unique(diy_array > 0)
)
