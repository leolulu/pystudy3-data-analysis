import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.arange(12).reshape(3, 4),
                   columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20).reshape(4, 5),
                   columns=list('abcde'))


print(
    df1
)