import numpy as np
import pandas as pd
num_dataframe=pd.read_excel('numbers.xlsx',sheet_name='numbers',usecols=['n1','n2'])
arr1=num_dataframe[['n1']].to_numpy()
arr2=num_dataframe[['n2']].to_numpy()
output=np.intersect1d(arr1,arr2)
print(output)