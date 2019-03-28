
import pandas
import numpy
titanic = pandas .read_csv ('train.csv')
print(titanic .head() )

# 自定义函数apply
def hundredth(column):
    hundredth_item=column .loc[99]
    return hundredth_item
hundredth_row = titanic .apply(hundredth)
print(hundredth_row )

# 每个列缺失值的个数
def not_null_count(column):
    column_null = pandas.isnull  (column )
    null=column [column_null ] # 空值
    return len(null)
column_null_count = titanic .apply(not_null_count)
print(column_null_count )

# 数据离散化
def witch_class(row):
    pclass = row["Pclass"]
    if pandas .isnull (pclass):
        return "Unknow"
    elif pclass == 1:
        return "First class"
    elif pclass == 2:
        return "second"
    elif pclass == 3:
        return "Third"
classes= titanic .apply(witch_class,axis= 1)
print(classes )

def age_(row):
    age=row['Age']
    if pandas.isnull (age):
        return "unknow"
    elif age<18:
        return "minor"
    else:
        return "adult"
res= titanic .apply(age_,axis=1)
print(res)

# 每个年龄段的生还率
titanic['age_labels'] = res # 加一个列名
age_group = titanic .pivot_table (index='age_labels',values= "Survived")
print(age_group )






















