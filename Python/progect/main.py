

from func import *


name = input('Введи своё имя, путник: ')
player['name'] = name

current_enemy = 0

while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка
3 - получить валюту
4 - Показать инвентарь
5 - Информация об игроке
6 - Информация о текущем противнике
''')
    
    if action == '2':
        training_type = input('1 - тренировать атаку, 2 - тренировать оборону')
        training(training_type)
    
    if action == '6':
        display_player

    if action == '1':
        current_enemy = fight(current_enemy)






