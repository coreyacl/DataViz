import pandas as pd
import matplotlib as plt
import numpy as np

data = pd.read_csv("files/tabula-timework.csv")
df = pd.DataFrame(data)
df = df.T

print(df[0])
datatotal = df[0]
x = np.arange(25)
xTicks = df[0][0]
#pd.DataFrame.plot(datatotal)
#plt.figure()
datatotal.plot()
