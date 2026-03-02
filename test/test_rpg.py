from src.RPG import Character

def test_player_initialization():
    #ETANT DONNE UN PERSONNAGE, doit avec hp==100
    p = Character("Guerrier", 20)

    assert p.hp == 100

def test_attack_reduces_hp():
    # ETANT DONNE deux personnages un monstre et un hero avec 100 PV
    hero = Character("Hero", 20)
    monster = Character("Gobelin", 5)
    
    #QUAND LE HERO ATTAQUE LE MONSTRE
    hero.attack(monster)
    
    #LE MONSTRE doit avoir 100-20=80 hp
    assert monster.hp == 80

def test_player_death():
    #ETANT DONNE UN PERSONNAGE
    monster = Character("Gobelin", 5)

    #QUAND IL PREND DES DOMMAGES > A ses HP
    monster.take_damage(110) 
    
    #IL DOIT avoir 0 hp et ne pas être en vie 
    assert monster.hp == 0
    assert monster.is_alive() is False