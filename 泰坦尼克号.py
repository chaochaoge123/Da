import pandas
import numpy
titanic = pandas .read_csv ('train.csv')
print(titanic .head() )

age = titanic ['Age']
print(age.loc[0:10])

# 判断缺失值
age_is = pandas .isnull (age)
# print(age_is)  # 结果是True就是缺失值,False不是缺失值

# 找到缺失值
age_null = age[age_is ]
print(age_null )
print(len(age_null))

# 有缺失值在,无法求平均数
mean_age = sum(titanic ['Age'])/len(titanic ['Age'])
print(mean_age )

# 将没有缺失的值求平均数
good_ages=titanic ['Age'][age_is==False ]
correct = sum(good_ages)/len(good_ages)
print(correct)
# 内置求平均数的方法
co =titanic ['Age'].mean()
print(co)

# 不同级别船仓的平均价格
passenger_class = [1,2,3]
fares_by_class = {}
for i in passenger_class :
    # 查出每个级别船仓的数据(行数)
    pclass_rows = titanic [titanic ["Pclass"]==i]
    # 每个级别船仓的价格
    pclass_fares = pclass_rows ['Fare']
    # 平均价格
    fare_for = pclass_fares .mean()
    fares_by_class [i]=  fare_for
print(fares_by_class )
#{1: 84.1546875, 2: 20.662183152173913, 3: 13.675550101832993}

# 每个级别的船仓平均获救的人数(每个船仓的生还率)
passenger_sur = titanic .pivot_table (index="Pclass",values= "Survived",aggfunc= numpy .mean)
'''
index  统计的数据的基准
values 关联的字段
aggfunc 列之间的运算,不指定默认求平均值
'''
print(passenger_sur )


# 每种船仓乘客的平均年龄
pass_age = titanic .pivot_table (index="Pclass",values = "Age")
print(pass_age )

# 不同登船地点,船票价格总和,生还人数总和
port_start = titanic .pivot_table (index="Embarked",values=["Fare","Survived"],aggfunc= numpy .sum)
print(port_start )

# 去掉列名的缺失值
drop_na = titanic .dropna(axis=1)
new_drop = titanic .dropna(axis= 0,subset=["Age","Sex"])
print(new_drop  )

# 指定行数查看列值
row_indx = titanic .loc[2,"Age"]
print(row_indx )

























