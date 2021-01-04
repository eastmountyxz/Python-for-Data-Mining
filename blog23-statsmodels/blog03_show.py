# -*- coding: cp936 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
a = np.random.standard_normal((9,4))
df = pd.DataFrame(a)
df.columns = ["No1", "No2", "No3", "No4"]
dates = pd.date_range('2015-1-1',periods=9,freq='M')
df.index = dates
 
print(df.cumsum())
df.plot(lw=2.0)
plt.show()
