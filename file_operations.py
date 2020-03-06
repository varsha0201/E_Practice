import pandas
import numpy
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
dataset= pandas.read_csv("/home/varsha/Desktop/Edureka_Practice/AllCountries.csv")
selected_data= dataset.loc[:['Country','GDP','BirthRate']]
x = numpy.array(selected_data["GDP"])
y = numpy.array(selected_data["BirthRate"])
print(x,y)
plt.scatter(x,y)
plt.xlim(0,20000)
plt.show()
# import os
# newfile = open("Edureka_py.txt","w+")

# for i in range(1,10):
#     newfile.write("\n Hello, welcome to python")

# newfile.close()
# newfile = open("Edureka_py.txt","r")

# for i in range(1,10):
#     print(newfile.read())

# newfile.seek(5)
# print(newfile.tell())
# os.rename("Edureka_py.txt","python1.txt")
# os.remove("python1.txt")

# newfile.close()

# import os
# os.getcwd()

#os.curdir
# os.listdir(os.getcwd())

#os.mkdir('new')

# fb = open("USArrests.csv","r")
# for line in fb:
#     print(line)
# # print(fb.read())
# fb.close()

# import codecs
# fb = codecs.open('worldcities.csv','r')
# cnt = 0
# for line in fb:
#     if cnt <= 10:
#         print(line)
#     else:
#         break
#     cnt +=1
# fb.close()
