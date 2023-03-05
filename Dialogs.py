from Fight import Fight


class Dialog():
    def hello(self, char, charmel, charizard, bad_1):
        fight_2 = Fight()
        user_pokemon = int(input('Привет, тебе нужно выбрать покемона!\n1-Charmander\n2-Charmelion\n3-Charizard\n'))
        if user_pokemon == 1:
            print('Ты выбрал \033[33mЧармандера!' + '\033[0;0m')
            fight_2.fights(char, bad_1)

        elif user_pokemon == 2:
            print('Ты выбрал Чармелиона!')
            fight_2.fights(charmel, bad_1)
        else:
            print('Ты выбрал Чаризарда!')
            fight_2.fights(charizard, bad_1)
