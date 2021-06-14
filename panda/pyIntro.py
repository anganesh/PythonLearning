import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
from pandas import DataFrame, read_csv
import os
# matplotlib inline
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names,births))
print (BabyDataSet)
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print (df)
df.to_csv('births1880.csv',index=False,header=False)
print("reading csv file")
print()
Location0 = r'E:\PythonMaterials\workouts\panda\births1880.csv'

Location = r'E:\PythonMaterials\workouts\panda\births1881.csv'
df = pd.read_csv(Location, header=None,names=['Names','Births'])
print(df)

# command to remove the os file.

os.remove(Location0)

# To check data types of data frames

print(df.dtypes)
print()
print(df['Births'].max())
print()

Sorted = df.sort_values(['Births'], ascending=False)
print(Sorted)
print()
print(Sorted.head(1))


# Name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values


print(MaxName)

print()

print("The most popular name")

print(df[df['Births'] == df['Births'].max()])

print()

