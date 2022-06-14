
from random import randint
from math import fsum
from statistics import median, stdev, mean


print("Генерируем случайный список из 10 чисел от 1 до 100:")
list_ten = [randint(1, 100) for x in range(0, 10)]
for i in list_ten:
    print(i)

print()
print("Сумма  чисел  списка:",fsum(list_ten))
print("Cреднее  значение: {}".format(mean(list_ten)))
print("Медиана: {}".format(median(list_ten)))
print("Cтандартное  отклонение: {:7.2f}".format(stdev(list_ten)))