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
# Analyze the score destribution
sns.boxplot(data=df, y ='MathScore')
plt.show()
sns.boxplot(data=df, y ='ReadingScore')
plt.show()
sns.boxplot(data=df, y ='WritingScore')
plt.show()
# Student Practice impact the student score

gb3= df.groupby('PracticeSport').agg({'MathScore':'mean','ReadingScore':'mean','WritingScore':'mean'})
print(gb3)
#line chat analysis
sns.lineplot(data=gb3,x='PracticeSport',y='MathScore')
sns.lineplot(data=gb3,x='PracticeSport',y='ReadingScore')
sns.lineplot(data=gb3,x='PracticeSport',y='WritingScore')

#Bar chat analysis

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
sns.barplot(data=gb3,x='PracticeSport',y='MathScore',ax=axes[0])
axes[0].set_title("MathScore")
sns.barplot(data=gb3,x='PracticeSport',y='ReadingScore',ax=axes[1])
axes[1].set_title("ReadingScore")
sns.barplot(data=gb3,x='PracticeSport',y='WritingScore',ax=axes[2])
axes[2].set_title("WritingScore")
plt.show()
