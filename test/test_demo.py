from src.RPG import Character

def test_demo_arme():
    # étant donné un personnage
    perso_arme = Character()
    
    # Lorsqu'on lui ajoute une arme
    perso_arme.ajouter_arme(1.2)
    
    # Alors il est bien armé 
    assert perso_arme.arme_multiplicator > 0
    
def test_demo_arme_attaque_hausse():
    # Étant donné un personnage ayant une arme et un ennemi
    perso_arme = Character(1.2)
    perso_sans_arme = Character()
    ennemi = Character()
    ennemi2 = Character()

    # Lorsque le personnage armé attaque l'ennemi
    perso_arme.attack(ennemi)
    perso_sans_arme.attack(ennemi2)
    
    # Alors l'ennemi subit plus de dégâts que lors d'une attaque sans arme
    assert ennemi.hp <= 10 and ennemi.hp >= 4
    assert ennemi2.hp <= 10 and ennemi2.hp >= 5

    
def test_demo_arme_attaque_baisse():
    # Étant donné un personnage ayant une arme et un ennemi
    perso_arme = Character(0.5)
    perso_sans_arme = Character()
    ennemi = Character()
    ennemi2 = Character()
        
    # Lorsque le personnage armé attaque l'ennemi
    perso_arme.attack(ennemi)
    perso_sans_arme.attack(ennemi2)

    # Alors l'ennemi subit moins de dégâts que lors d'une attaque sans arme
    assert ennemi.hp <= 10 and ennemi.hp >= 2.5
    assert ennemi2.hp <= 10 and ennemi2.hp >= 5
