#- * - coding: utf - 8 - * -

import pandas
from pandas import Series

fan = pandas .read_csv('train.csv')
series_file = fan['Age'] # 指定列值
print(type(series_file ))
print(series_file [0:5])

film_name = series_file .values
print(type(film_name ))






























































