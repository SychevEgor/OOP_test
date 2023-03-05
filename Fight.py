import random as r
import time
from tqdm import tqdm


class Fight():

    def fights(self, poke, enemy):
        count = 0
        enemy_hp = enemy.get_hp()
        pokemon_hp = poke.get_hp()

        print('Бой проходит между: ' + str(poke.get_kind()) + ' и ' + enemy.get_name())
        list = [str(poke.get_kind()), str(enemy.get_name())]
        if list[r.randint(0, 1)] == str(poke.get_kind()):
            print('Первым атакует: ' + f" \033[33m{poke.get_kind()}" + '\033[0;0m')

        else:
            print('Первым атакует: ' + f'\033[31m{enemy.get_name()}' + '\033[0;0m')
        while pokemon_hp or enemy_hp > 0:
            time_list = [1, 2, 3]

            if pokemon_hp < 0:
                print('О нет! Враг оказался сильнее')
                break
            if enemy_hp < 0:
                print('Победа!')
                break
            print(f'Ходит \033[32m{list[count % 2]}' + '\033[0;0m')
            if list[count % 2] == str(poke.get_kind()):
                damage = r.randint(10, poke.get_attak())
                damage_1 = r.randint(10, poke.get_attak())
                enemy_hp = damage - enemy_hp
                enemy_hp = -enemy_hp
                for i in tqdm(time_list):
                    time.sleep(1)
                print()

                print(
                    f'\033[33m{str(poke.get_kind())}' + '\033[0;0m' + ' Наносит ' + f' {damage}' + ' урона по ' + f'\033[31m{enemy.get_name()}' + '\033[0;0m')
                print('У ' + enemy.get_name() + ' осталось ' + f'{enemy_hp}' + ' жизней!')
            else:
                pokemon_hp = damage_1 - pokemon_hp
                pokemon_hp = -pokemon_hp
                for i in tqdm(time_list):
                    time.sleep(1)
                print()

                print(
                    f'\033[31m{enemy.get_name()}' + '\033[0;0m' + ' Наносит ' + f' {damage_1}' + ' урона по ' + f'\033[33m{poke.get_kind()}' + '\033[0;0m')
                print('У ' + str(poke.get_kind() + ' осталось ' + f'{pokemon_hp}' + ' жизней!'))
            count += 1
