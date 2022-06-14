from random import randint
import time

igrok1 = input('Введите имя 1-го играющего ')
igrok2 = input('Введите имя 2-го играющего ')

x=0
y=0
for i in range(5):
#Ввод имен играющих
   
#Моделирование бросания кубика первым играющим
    print('Кубик бросает', igrok1)
    time.sleep(2)
    n1 = randint(1, 6)
    print('Выпало:', n1)

#Моделирование бросания кубика вторым играющим
    print('Кубик бросает', igrok2)
    time.sleep(2)
    n2 = randint(1, 6)
    print('Выпало:', n2)

#Определение победителя
    if n1<n2:
        y+=1
        print("Победил ",igrok2, "кол-во побед:", y)
    elif n1==n2:
        print("Ничья!")
    else:
        x+=1
        print("Победил ",igrok1, "кол-во побед:", x)
 
if x>y:
    print("Чемпион",igrok1)
elif x<y:
    print("Чемпион",igrok2)
else:
    print("Победителей нет")
