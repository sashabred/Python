#Списки
print("СПИСКИ")
list1 = [82,8,23,97,92,44,17,39,11,12]

#Примените  команду dir для  просмотра  методов  работы  со  списками (dir(list)).
print("Методы работы со списками:")
print(dir(list),'\n')

#Вызовите справку (с помощью команды help) для методов insert, append, sort, remove, reverse.
help(list1.insert)
help(list1.append)
help(list1.sort)
help(list1.remove)
help(list1.reverse)

print("Изначальный список:")
print(list1, sep='\n')
print()

#Измените значения элементов списка (по вашему усмотрению) с помощью операции индексирования.
list1[0]=55
print("Меняем первый элемент:")
print(list1, sep='\n')
print()

#Добавьте новый элемент в конец списка.
list1.append(135)
print("Добавляем элемент в конец списка:")
print(list1, sep='\n')
print()

#Добавьте новый элемент в произвольную(на ваше усмотрение)позицию списка
list1.insert(3, 77)
print("Добавляем элемент на позицию (индекс=3) списка:")
print(list1, sep='\n')
print()

#Удалите элемент из списка по известной позиции.
list1.pop(3)
print("Удаляем элемент из списка (индекс=3):")
print(list1, sep='\n')
print()

#Удалите последний элемент из списка
list1.pop(-1)
print("Удаляем последний элемент из списка:")
print(list1, sep='\n')

print()
print("Сортировка элементов списка")
list1.sort(reverse=True)
print("Отсортированный список:")
print(list1, sep='\n')
print()
print("Новый объект отсортированного списка")
list2 = [3,5,6,2,33,6,11]
lis = sorted(list2)
print(lis, sep='\n')
print()