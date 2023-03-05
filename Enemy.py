class Enemy():
    def create(self, name, attak, hp):
        self.__attak = attak
        self.__hp = hp
        self.__name = name

    def get_info_enemy(self):
        return self.__name + ' ' + str(self.__attak) + ' ' + str(self.__hp)

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_attak(self):
        return self.__attak
