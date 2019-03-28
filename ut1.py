import pandas 
food_info = pandas.read_csv('2018-04-08_15-28-14.csv',sep=';')
print(type(food_info))  #<class 'pandas.core.frame.DataFrame'>
# print(help(pandas .read_csv ))
print(food_info.head())  # 显示前5行，可指定
print(food_info.shape)  #

# print(food_info .tail(3))  # 尾部几行
print(food_info .columns) # 列名















