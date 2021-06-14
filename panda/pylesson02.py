# https://nbviewer.jupyter.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/02%20-%20Lesson.ipynb
import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
# matplotlib inline

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)


names = ['Bob','Jessica','Mary','John','Mel']


#  Be low to print 10 random numbers

randintarray = random.randint(10, size=6)
print(randintarray)

# len function returns the length of array 
print(len(randintarray))


random.seed(500)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(100)]

# Print first 10 records
print (random_names)

births = [random.randint(low=0,high=1000) for i in range(100)]
print(births[:10])
print(births)

BabyDataSet = list(zip(random_names,births))
print(BabyDataSet[:10])
print(BabyDataSet)

df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print(df)

df.to_csv('births100.csv',index=False,header=False)

Location = r'E:\PythonMaterials\workouts\panda\births100.csv'
df1 = pd.read_csv(Location)

print("Information about data in csv file")

df1.info()


df1 = pd.read_csv(Location, header = None)

print("Information about data in csv file with header = None parameter ")

df1.info()

#  To print last 5 records

print(df1.tail())

#  To print top 5 records
df = pd.read_csv(Location, names=['Names','Births'])
print(df.head(5))


#  To remove the file

import os
os.remove(Location)


print(df['Names'].unique())

for x in df['Names'].unique():
    print(x)



print(df['Names'].describe())

name = df.groupby('Names')

print("After group by")
print()

df = name.sum()
print(df)

print("after sorting")


Sorted = df.sort_values(['Births'], ascending=False)
print(Sorted)


print(df['Births'].max())














