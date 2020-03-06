import pandas
import numpy
import matplotlib.pyplot as plt
import sys
print(sys.path)
plt.figure(figsize=(10,10))
dataset = pandas.read_csv("/home/varsha/Desktop/Edureka_Practice/AllCountries.csv")
selected_data = dataset.loc[:,['Country','GDP','BirthRate']]
x = numpy.array(selected_data['GDP'])
y = numpy.array(selected_data['BirthRate'])
print(x,y)
plt.scatter(x,y)
plt.xlim(0,20000)
plt.show()