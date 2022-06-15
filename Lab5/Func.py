from random import randint
import time

#Ввод имени игрока
def player_name():
    return input('Введите имя игрока ')


#Бросок кубика
def throw(name):
    print('Кубик бросает ', name)
    time.sleep(2)
    point = randint(1, 6)
    print('Выпало:', point)
    return point
    

#Ядро игры
def play():
    playerList=[]
    allResult=[]
    currentResult=[]

    print("Для выхода наберите exit")
    while True:
        name=player_name()
        if name == "exit":
            break
        else:
            playerList.append(name)

    i=0

    while i < len(playerList):
        allResult.append(0)
        i+=1

    print("Начинаем игру!")

    while True:
        for i in playerList:
            currentResult.append(throw(i))
        
        winner_id=0

        while winner_id <len(currentResult):
            if currentResult[winner_id] == max(currentResult):
                allResult[winner_id]= allResult[winner_id] + 1
                print("Победил ", playerList[winner_id], " кол-во побед:",allResult[winner_id])
            winner_id = winner_id+1
    
        currentResult.clear()

        end=input("Для выхода наберите exit")
        if end=="exit":
            break




