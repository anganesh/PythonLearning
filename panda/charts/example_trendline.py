# import the library
import matplotlib.pyplot as plt
  
  
# Creation of Data
x1 = ['July 1-7', 'July 8-15', 'July 16-23', 'July 24-Aug 1', 'Aug 1-8']
y1 = [900, 940, 1000, 1100, 1200]
y2 = [40, 80, 300, 350, 450]
y3 = [840, 860, 700, 750, 750]

  
# Plotting the Data
plt.plot(x1, y1, label='Total Issues')
plt.plot(x1, y2, label='Closed')
plt.plot(x1, y3, label='Open')

  
plt.xlabel('Date')
plt.ylabel('Ratings')
plt.title("Rating Trend")
  
plt.plot(y1, 'o:b', linestyle='-', linewidth='8')
plt.plot(y2, 'o:g', linestyle='-', linewidth='8')
plt.plot(y3, 'o:r', linestyle='-', linewidth='8')

  
plt.legend()
plt.show()
