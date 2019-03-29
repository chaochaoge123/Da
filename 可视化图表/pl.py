import pandas
import numpy
import matplotlib.pyplot as plt

# fig = plt.figure()
# ax1 = fig.add_subplot(4,3,1)  # 四行三列矩阵中的第一个位置
# ax2 = fig.add_subplot(4,3,2)
# ax3 = fig.add_subplot(4,3,6)
# res = plt.show()
# print(res)

fig = plt.figure(figsize=(6,3))  # figsize 指定长度和高度
s1 = fig.add_subplot(2,1,1)
s2 = fig.add_subplot (2,1,2)

s1.plot(numpy.random.randint(1,5,5) ,numpy .arange(5))
s2 .plot(numpy .arange(10)*3,numpy.arange(10)  )
res=plt.show()
print(res)





































