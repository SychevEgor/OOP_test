class Pokemon:
    def first_crate(self, kind, weight, element, attak, hp):
        self.__kind = kind
        self.__weight = weight
        self.__element = element
        self.__attak = attak
        self.__hp = hp

    def get_info(self):
        print('Kind: ' + self.__kind + '\nWeight: ' + str(
            self.__weight) + '\nElement: ' + self.__element + '\nAttak: ' + str(self.__attak) + '\nHP: ' + str(
            self.__hp) + '\n')

    def get_kind(self):
        return self.__kind

    def get_attak(self):
        return self.__attak

    def get_hp(self):
        return self.__hp
