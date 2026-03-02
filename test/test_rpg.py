from src.RPG import Character

def test_player_initialization():
    #ETANT DONNE UN PERSONNAGE
    p = Character("Guerrier")

    #doit avec hp==10
    assert p.hp == 10

def test_attack_reduces_hp():
    # ETANT DONNE deux personnages un monstre et un hero avec 10 PV
    hero = Character("Hero")
    monster = Character("Gobelin")
    
    #QUAND LE HERO ATTAQUE LE MONSTRE
    hero.attack(monster)
    
    #LE MONSTRE doit avoir 9 hp
    assert monster.hp == 9

def test_player_death():
    #ETANT DONNE UN PERSONNAGE
    monster = Character("Gobelin")

    #QUAND IL PREND DES 10 COUPS
    for i in range(10) :
        monster.take_damage(1)
    
    #IL DOIT avoir 0 hp et ne plus être en vie
    assert monster.hp == 0
    assert monster.is_alive() is False