import pandas
food_info = pandas.read_csv('2018-04-08_15-28-14.csv',sep=';') # 以sep切分列名
# print(food_info .loc[0]) # 第一行数据 下标取值

# 指定列名取数据
# columns = ['TimeStemp','grDataTime']
# info = food_info [columns ]
# print(info )

# 将数据的列名放在列表里,取出列名以p结尾的前3行数据
# col = food_info .columns.tolist()
# col = col[0] .split(';')
# print(col)
# gram= []
# for i in col:
#     if i.endswith('p'):
#         gram.append(i)
# gram_df = food_info [gram ]
# print(gram_df .head(3))

# 根据列名进行运算 将列中的值加100
# div_ = food_info ['W_GD']+100
# print(div_ )

# 新增一个列
# obj_= food_info ['Bl1_S2_25M1']+food_info ['Bl1_S1_46M1']
# print(food_info .shape )
# food_info ['new_']=obj_ # 将两个列的值和赋值给新的列new_
# print(obj_)
# print(food_info .shape ) # 列的个数已增加

# 求列中的最大值,最小值,平均值
# print(food_info ['Bl1_S2_25M1'].max())
#平均值mean()

# 列中值排序
# food_info .sort_values('Bl1_S2_25M1',inplace= True  ) # 从小到大
# food_info .sort_values('Bl1_S2_25M1',inplace= True ,ascending= False  ) # 大到小
# print(food_info['Bl1_S2_25M1'])
















