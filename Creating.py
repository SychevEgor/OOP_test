from Charizard import Charizard
from Charmander import Charmander
from Charmelion import Charmelion
from Enemy import Enemy
from Dialogs import Dialog


class Creating():
    char = Charmander()
    char.create()
    charmel = Charmelion()
    charmel.create()
    charizard = Charizard()
    charizard.create()
    bad_1 = Enemy()
    bad_1.create('Bad', 30, 70)
    hello = Dialog()
    hello.hello(char, charmel, charizard, bad_1)
