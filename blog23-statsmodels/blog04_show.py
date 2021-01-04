# -*- coding: cp936 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
a = np.random.standard_normal((9,4))
df = pd.DataFrame(a)
df.columns = ["No1", "No2", "No3", "No4"]
dates = pd.date_range('2015-1-1',periods=9,freq='M')
df.index = dates
print(df['No1'])
 
import matplotlib.pyplot as plt
df['No1'].cumsum().plot(style="r",lw=2.)
plt.xlabel('date')
plt.ylabel('value')
plt.show()
