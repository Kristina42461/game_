from random import randint, uniform
from time import sleep
from data import *


def train():
    # можно свою логику
        choice_train = input('\t1. Тренировать атаку\n\t2. Тренировать броню\n')
        for i in range(0,101, 20):
            print(f'Тренировка завершена на {i}%')
            sleep(1)
        if  choice_train == '1': 
            # == тренируем атаку
            temp_rand = randint(1,5)
            player['attack'] +=  temp_rand
            print(f'Теперь твоя атака равна: {player["attack"]}\n')
        elif choice_train == '2':
            # == тренируем броню
            if player['armor'] >= 0.8: 
                temp_rand = uniform(0.05, 0.2)
                player['armor'] -= temp_rand
                print(f'Теперь твоя броня равна: {player["armor"]}\n')
            else:
                print(f'Вы достигли максимума в прокачке брони! Броня = {player["armor"]}')

def fight():
        # выпадает число либо 1, либо 2 (для определения того, кто первый начнет)
        round = randint(1, 2)
        # выбор рандомного врага из списка "enemies"
        current_enemy = randint(0,2)

        # выпадает число либо 1, либо 2 (для определения того, кто первый начнет)
        round = randint(1, 2)

        # переменная "enemy", в которую из списка выбирается враг по рандомной переменной "current_enemy"
        enemy = enemies[current_enemy]

        # "enemy_hp" переменная для хп врага
        enemy_hp = enemies[current_enemy]['hp']

        # выводим сообщение с именем и фразой врага
        print(f'Противник - {enemy["name"]}: {enemy["script"]}')
        luck_boost = 0
        choice = input('Будешь ли пить зелье путник? \n\t1 - Да \n\t2 - Нет\n')
        if choice == '1':
            if not player['inventory']:
                print('У тебя ничего нет!')
            else:
                number = 1
                for item in player['inventory']:
                    print(f'Предмет № {number} {item}\n')
                    number += 1
                inv_choice = input('Что выберешь?(Напиши)')
                if inv_choice == 'Зелье атаки':
                    player['attack'] += 10
                    print(f'Теперь твоя атака равна {player["attack"]}')
                elif inv_choice == 'Зелье удачи':
                    luck_boost = 4
                    print('Теперь твоя удача увеличилась на 4')
                elif inv_choice == 'Зелье восстановления':
                    player['hp'] += 40
                    print(f'Теперь твое здоровье увеличилось на 40 и равно {player["hp"]}')
                player['inventory'].remove(inv_choice)
        else:
            input('Enter чтобы продолжить')
        print()

     # цикл пока у кого-то из игроков не закончится хп  
        while player['hp'] > 0 and enemy_hp > 0:
            # если нечетеное число аттакует игрок  
            if round %2 == 1:
                print(f'Ход игрока')
                print(f'{player["name"]} атакует {enemy["name"]}.')
                # из жизни врага отнимаем силу нашей аттаки
                enemy_hp -= player['attack']
                sleep(1)
                # пишем сколько осталось хп у игрока и врага
                print(f"\n\t{player['name']} - {player['hp']}\n\t{enemy['name']} - {enemy_hp}")
                print()
                sleep(1)
            # если нечетеное число аттакует враг 
            else:
                print(f'Ход {enemy["name"]}')
                print(f'{enemy["name"]} атакует {player["name"]}.')
                # из жизни игрока отнимаем силу аттаки врага
                temp_rand = randint(5,15-luck_boost)
                if player["luck"] == temp_rand: # ==== выпала удача, в 2 раза меньше урон врага и не кончается броня!
                    print('___________Удача_________')
                    print('В этом раунде урон врага в 2 раза меньше!')
                    player['hp'] -= enemy['attack']/2 * player['armor'] # ===== добавили броню
                else:
                    player['hp'] -= enemy['attack'] * player['armor'] # ===== добавили броню
                    if player['armor'] < 0.99:
                        player['armor'] += 0.2 # ===== кончается броня
                    sleep(1)
                # пишем сколько осталось хп у игрока и врага
                print(f"\n\t{player['name']} - {player['hp']}\n\t{enemy['name']} - {enemy_hp}")
                print()
                sleep(1)
            round += 1

        # пишем кто выиграл
        # если хп игрока больше 0 - он выиграл / иначе - враг победил
        if player['hp'] > 0:
            print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        else:
            print(f'Противник - {enemy["name"]}: {enemy["loss"]}')

def info_about_player():
     for info, stat in player.items():
          print(f'{info} : {stat}') 

def info_about_enemy():
     for enemy_list in enemies:
        for info, stat in enemy_list.items():
            print(f'{info} : {stat}') 
        print('\n')

def shop():
     print(f'Приветствую {player["name"]} в ларьке тролля!')
     number = 1
     print(f'У тебя есть {player["money"]} монет.')
     for key, value in shop_items.items():
        print(f'____________________Товар № {number}____________________')
        print(f'{value["Название"]}: {value["Цена"]}: {value["Эффект"]}')
        print('\n')
        number+=1
     choice = input('Готов ли ты что-то купить? \n\t1 - Да \n\t2 - Нет\n')
     while choice != '2':
        if choice == '1':
            item = input("Введите номер товара")
            # # провряем нет ли уже этого предмета в интентаре 
            # if item in player['inventory']:
            #     print(f'У тебя уже есть {shop_items[item]["name"]}')
            # # иначе если хватает денег, то добавляем в инвентарь  
            if player['money'] >= shop_items[item]['Цена']:
                print(f'Ты успешно приобрёл {shop_items[item]["Название"]}')
                # добавляем товар в инвентарь  
                player['inventory'].append(shop_items[item]["Название"])
                # вычитаем деньги у игрока
                player['money'] -= shop_items[item]['Цена']
            else:
                print('Не хватает монет :(')  
        choice = input('Хочешь ли ты еще что-то купить? \n\t1 - Да \n\t2 - Нет\n')
     else:
         print('Приходи еще!')

def earn():
    print('Добро пожаловать на завод! У тебя есть 66.66% шанс заработать 500 монет. Соответственно, 33.33% чтобы их потерять')
    result = randint(1, 100)
    sleep(1.5)
    print('Результат....')
    sleep(1.5)
    print('Страшно?!')
    if result < 67:
        print('Вы выиграли 500 монет!')
        player['money'] += 500
    else:
        print('Вы проиграли 500 монет :(')
        player['money'] -= 500
    print()
    print(f'Осталось монет: {player["money"]}')
    print()
