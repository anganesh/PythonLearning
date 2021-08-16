# import the library
import matplotlib.pyplot as plt
import pandas as pd
Location = r'E:\github_anganesh\PythonLearning\panda\charts\trendline.csv'
csv = pd.read_csv(Location)
data = csv[['WDate', 'Total','Closed','Open']]
print(data.dtypes)

x1 = data['WDate']
y1 = data['Total']
y2 = data['Closed']
y3 = data['Open']
print('Total')
print(y1)
print('closed')
print(y2)
print('open')
print(y3)
  
# Creation of Data
#x1 = ['July 1-7', 'July 8-15', 'July 16-23', 'July 24-Aug 1', 'Aug 1-8']
#y1 = [900, 940, 1000, 1100, 1200]
#y2 = [40, 80, 300, 350, 450]
#y3 = [840, 860, 700, 750, 750]

  
# Plotting the Data
plt.plot(x1, y1, label='Total')
plt.plot(x1, y2, label='Closed')
plt.plot(x1, y3, label='Open')

  
plt.xlabel('Date')
plt.ylabel('Ratings')
plt.title("Rating Trend")
  


  
plt.legend()
plt.show()
