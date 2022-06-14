##Словари

#dict = {
#  "food": "Apple",
#  "quantity": 4,
#  "color": "Red"
#}
#print("Проверяем возможность доступа к элементам словаря")
#print("Ключ food: ",dict["food"])
#dict["quantity"]+=10
#print("Меняем значение для quantity на +10 =",dict["quantity"])

##Создаем пустой словарь
#print()
#print("Заполняем словарь значениями")
#dp = {}

#length = int(input("Введите длину словаря:"))
#for element in range(0,length):
#   name = str(input('введите Имя: '))
#   age = int(input('введите Возраст: '))

#   dp[name] =age

#print("Вывод словаря:")
#for k, v in dp.items():
#    print(k, v)


#Вложенность хранения данных
rec = {
 'name': {'firstname': 'Bob', 'lastname': 'Smith'},
 'job': ['dev', 'mgr'],
 'age': 25
}

# вывод  значения  полного  имени,  отдельно  имени firstname, список должностей.
print("ФИО:", rec['name']['firstname']+' '+rec['name']['lastname'],'\n')
print("Имя:", rec['name']['firstname'],'\n')
print("Список должностей: ", rec['job'][0] +', '+rec['job'][1],'\n')
rec['job'].append('engineer')
print("Добавили новую должность:")
for k in rec['job']:
    print(k)
print()    
print("Полная информация о персоне:")
print(rec)
