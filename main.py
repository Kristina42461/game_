from random import randint, uniform
from time import sleep
from data import *
from actions import *

name = input('Введи своё имя, путник: ')

# добавляем имя в словарь "player" с игроком (ты игрок!!)
player['name'] = name

# ====
while True:
    print('Выбери действие:')
    actiont = input('\n\t1. Тренировка\n\t2. В бой\n\t3. Твои показатели\n\t4. Список врагов\n \t5. Магазин\n \t6. Пойти на завод\n') 
    if actiont == '1': 
        train()
    elif actiont == '2':
        fight()
    elif actiont == '3':
        info_about_player()
    elif actiont == '4':
        info_about_enemy()   
    elif actiont == '5':
        shop() 
    elif actiont == '6':
        earn() 