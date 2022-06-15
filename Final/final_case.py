#Вариант 7
n=0
arr=[]

while True:
	x=input("Создаем последовательность, для выхода напииши 'Finish': ")
	n+=1
	arr.append(n)
	if (x=="Finish"):
		break
	else:
		print(arr)