#Преобразование данных
print("Реализуйте конкатенацию – число преобразуйте к строке")
param = "string" + str(15)
print(param,'\n')

print("Составьте  программу,  запрашивающую  у  пользователя  два  числа  и реализующую их сложение")
n1 = input("Enter the first number:  ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)


#Форматирование строк
print()
a = 1/3
print("Форматирование строк:","{:7.3f}".format(a))

a = 2/3
b = 2/9
print()
print("форматный вывод для нескольких значений сразу:")
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b),"\n")

print("В программe  измените  способ  вывода  результата –примените функцию format().")
n1 = input("enter the first number:  ")
n2 = input("enter the second number: ")
n3 = float(n1) + float(n2)
print("{0:6.2f} plus {1:6.2f}={2:6.2f}".format(float(n1),float(n2),n3),'\n')