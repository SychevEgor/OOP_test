from Pokemon import Pokemon


class Charizard(Pokemon):
    def create(self):
        super().first_crate('Charizard', 90, 'fire', 90, 300)
