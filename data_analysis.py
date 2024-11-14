import pandas as pd
import numpy as numpy
import seaborn as sns
import matploatlib.pyplot as plt
#Import file from source path
df = pd.read_csv('C:/Users/shubham_kumar/Downloads/Expanded_data_with_more_features.csv/student_data.csv')
#Check some values present in column.
print(df.head())
# Check the statatics numerical values column.
df.describe()
# Information of all the column and its data type
df.info()
