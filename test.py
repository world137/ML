from IPython.display import display
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
display(df.describe)

display('isnull' , df.isnull)
display('is nan' , df.isna)
df.columns()