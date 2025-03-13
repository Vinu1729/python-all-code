import pandas as pd
import numpy as np

ser = pd.Series()
print("pandas series ",ser)
#array
data = np.array(['V','I','N','U'])
ser = pd.Series(data)
print("pandas series \n",ser)