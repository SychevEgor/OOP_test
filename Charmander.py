from Pokemon import Pokemon


class Charmander(Pokemon):
    def create(self):
        super().first_crate('Charmander', 8, 'fire', 30, 70)
