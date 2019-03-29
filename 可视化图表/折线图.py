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







































