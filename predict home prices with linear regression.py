import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#list of properties 
#first element is house size
#second element is price
properties = [[793, 1300000], 
              [2477, 3700000], 
              [1263, 1480000], 
              [1291, 2380000], 
              [603, 955000], 
              [1655, 2130000], 
              [1071, 1300000], 
              [1877, 2700000],
              [1610, 2650000],
              [3058, 2850000],
              [1609, 2250000],
              [1630, 2950000],
              [1211, 1900000],
              [1219, 1820000],
              [1700, 2100000],
              [1629, 2480000],
              [740, 1270000],
              [740, 1260000],
              [1637, 2520000],
              [1637, 3450000],
              [1291, 2430000],
              [1211, 2250000],
              [400, 1],
              [800, 925000],
              [700, 950000],
              [1711, 2630000],
              [847, 975000],
              [1230, 1570000],
              [1291, 2010000],
              [2300, 3630000],
              [886, 1120000],
              [1700, 2020000],
              [389, 695974],
              [793, 1330000],
              [978, 1460000],
              [582, 685000],
              [793, 1340000],
              [1327, 2440000],
              [791, 925000],
              [793, 1400000],
              [1630, 2980000],
              [740, 1200000],
              [1244, 1650000],
              [1183, 1880000],
              [1327, 2440000],
              [1183, 1880000],
              [1643, 2790000],
              [2500, 3470000],
              [1085, 1160000],
              [740, 1230000],
              [1291, 2180000],
              [1291, 2060000],
              [740, 1270000],
              [1230, 1660000],
              [1219, 1870000],
              [1275, 1800000],
              [793, 1330000],
              [1259, 1650000],
              [1395, 1950000]]



properties_size = []
properties_price = []

for size in range(len(properties)):
    properties_size.append(properties[size][0])

for price in range(len(properties)):
    properties_price.append(properties[price][1])


size = np.array(properties_size)
price = np.array(properties_price)









#calculate linear regression line (y = mx + b)
#m
m = (len(properties_price) * sum(a * b for a, b in zip(properties_price, properties_size)) - sum(properties_size) * sum(properties_price))/(len(properties_price) * sum(i**2 for i in properties_size) - sum(properties_size) ** 2)

#b
b = (sum(properties_price) * sum(i**2 for i in properties_size) - sum(properties_size) * sum(a * b for a, b in zip(properties_price, properties_size)))/(len(properties_price) * sum(i**2 for i in properties_size) - sum(properties_size) ** 2)



#plot the linear regression line
line = m * size + b
plt.plot(size, line, color='orange', label='Line of Best Fit')



plt.scatter(size, price)
plt.title("House Prices vs. House Sizes")
plt.xlabel("House Size (sq.ft)")
plt.ylabel("House Price ($)")
plt.show()
