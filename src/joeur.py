from joeur import Player

def joeur_100():
    joeur = Player()
    assert joeur.hp == 100

def attack():
    attacker = Player()
    defender = Player()

    attacker.attack(defender)

     for _ in range(15):
        attacker.attack(defender)

    assert defender.hp == 0
