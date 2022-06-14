#Работа со строками
print("РАБОТА СО СТРОКАМИ\n")

print("Объявите  две  строковые  переменные:")
string1 = "This is a string."
string2 = "  This is another string."
string3=string1+string2
print(string3,'\n')

#Функции для строк
print("Примените к cтроке функции:")
print("len():",len(string1))
print("title():",string3.title())
print("lower():",string2.lower())
print("upper():",string2.upper())
print("rstrip():",string1.rstrip())
print("lstrip():",string2.lstrip())
print("strip():",string3.strip())
print("strip('.'):",string3.strip('.'),'\n')


#индексирование
print("С помощью индексирования ([]) извлеките требуемый символ:")
word= "Announcement"
symbol= word[2] 
print("Слово=",word,",  3-й символ =", symbol)

pattern = word[2:5]
print("Срез [2:5]= ", pattern)

pattern = word[1:8:2]
print("Срез [1:8:2] = ", pattern,'\n')

#word[5]= 'o'