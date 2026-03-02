from joeur import Joeur

def joeur_100():
    joeur = Joeur()
    assert joeur.hp == 100

def attack():
    attacker = Joeur()
    defender = Joeur()

    attacker.attack(defender)

     for _ in range(15):
        attacker.attack(defender)

    assert defender.hp == 0
