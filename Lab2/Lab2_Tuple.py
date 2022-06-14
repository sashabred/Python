print("КОРТЕЖИ")

print("Методы:",dir(tuple),'\n')

tup = (2,8,23,97,92,44,17,39,11,12)
print(help(tup.index))
print(help(tup.count))

print("Count - возвращает количество искомого значение, например число 17 встречается -",tup.count(17))
print("Index - возвращает индекс искомого значения, например индекс числа 44=",tup.index(44),'\n')

#Преобразование кортежа к типу список
tolist = list(tup)
print("Тип, после преобразования = ",type(tolist))