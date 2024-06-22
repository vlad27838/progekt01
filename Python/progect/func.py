from data import *


def training(training_type0):
    if training_type0 == '1':
        #качаем атаку
        pass
    else:
        #качаем защиту
        pass




def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}. Шанс критического урона ({player["attack"] * 3}ед.) равен {player["luck"]}%')
    print(f'Броня поглощает {(1 - player["armor"]) * 100}% урона')
    print()

def fight(current_enemy0):
#Подготовка к бою
    enemy = enemies[current_enemy0]
    #script - то что говорит противник
    input('Enter чтобы продолжить')

#Бой
    while player['hp'] > 0 and enemy['hp']> 0:
        pass
        #Битва


#End
    if player['hp'] > 0:
        pass
        #print -> win
        current_enemy0 += 1

    else:
        pass
        #print -> loss 
        return current_enemy0
    
def display_enemy(c_enemy):
    enemy = enemies[c_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Здоровье - {enemy["hp"]}')
    print(f'Атака - {enemy["attack"]}')

