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

#Check the null values and its count of all the column
df.isnull().sum()

# Bar grap of the Male and Female count
df=df.drop('Unnamed: 0',axis=1)
plt.figure(figsize=(8,5))
ax=sns.countplot(data=df,x='Gender')
ax.bar_label(ax.containers[0])
plt.show()

# From the above chat we have analysis that female count is more then male count.

# Analyze the impact of student scores based on parental education.

gb = df.groupby('ParentEduc').agg({'MathScore':'mean','ReadingScore':'mean','WritingScore':'mean'})
sns.heatmap(gb,annot=True)
plt.show()
# Analyze the impact of student scores based on parental Maritalstatus.
gb1=df.groupby('ParentMaritalStatus').agg({'MathScore':'mean','ReadingScore':'mean','WritingScore':'mean'})
print(gb1)
sns.heatmap(gb1,annot=True)
