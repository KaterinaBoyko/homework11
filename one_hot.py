import pandas as pd
import random
Создаем исходный DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
Преобразуем DataFrame в one-hot вид
one_hot = pd.DataFrame()
one_hot['robot'] = (data['whoAmI'] == 'robot').astype(int)
one_hot['human'] = (data['whoAmI'] == 'human').astype(int)
Проверяем результат
print(one_hot.head())
