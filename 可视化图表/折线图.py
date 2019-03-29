#- * - coding: utf - 8 - * -

import  pandas
from matplotlib import pyplot

unrate = pandas .read_csv ('shiyelu.csv')
unrate ['Date']= pandas .to_datetime(unrate ["Date"])
print(unrate .head())

first_t = unrate .head()
pyplot .plot (first_t ['Date'],first_t ['Value'])  # 两个参数，左边为X轴，右边是Y轴
pyplot .xticks(rotation=45)  # X轴数据45°显示
# X轴名
pyplot .xlabel ('Month')
# Y轴名
pyplot .ylabel ('Unemployment Rate')
# 标题
pyplot .title ('1945,Unemployment Rate ')

res=pyplot .show()
print(res)

# 画多条折线
# fit = pyplot .figure(figsize=(6,3))
# pyplot .plot(unrate [0:2]['Date'],unrate [0:2]['Value'],c = 'red')
# pyplot .plot(unrate [3:7]['Date'],unrate [3:7]['Value'],c = 'blue')
# b=pyplot .show()
# print(b)

# 每个年代的折线图
fg = pyplot .figure(figsize=(12,6))
colors = ['red','blue','green']
for i in range(3):
    start_index= i*12
    end_index = (i+1)*12
    subset = unrate [start_index :end_index ]
    label = str(1945 + i)
    pyplot.plot(subset['Date'],subset ['Value'],c = colors[i],label =label )

pyplot .legend (loc='best') # 每条线提示框的位置
# X轴名
pyplot .xlabel ('Month')
# Y轴名
pyplot .ylabel ('Unemployment Rate')
# 标题
pyplot .title ('1945-1947,Unemployment Rate ')
pyplot .show()





































