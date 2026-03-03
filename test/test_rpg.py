from src.RPG import Character

def test_player_initialization():
    #ETANT DONNE UN PERSONNAGE
    p = Character()

    #doit avec hp==10
    assert p.hp == 10

def test_attack_reduces_hp():
    # ETANT DONNE deux personnages un monstre et un hero avec 10 PV
    hero = Character()
    monster = Character()
    hp0 = monster.hp

    #QUAND LE HERO ATTAQUE LE MONSTRE
    hero.attack(monster)

    #LE MONSTRE doit perdre 1 hp
    assert hp0 - monster.hp == 1

def test_player_death():
    #ETANT DONNE UN PERSONNAGE
    monster = Character()

    #QUAND IL PREND DES ASSEZ DE COUPS
    while(monster.hp>0) :
        monster.take_damage(1)
    
    #IL DOIT avoir 0 hp et ne plus être en vie
    assert monster.hp == 0
    assert monster.is_alive() is False

def test_player_kill():
    #ETANT DONNE DEUX PERSONNAGES monstre et hero
    hero = Character()
    monster = Character()

    #QUAND MONSTRE TAPE HERO 10 FOIS
    while(hero.hp>0) :
        monster.attack(hero)
    
    #Hero doit mourir et avoir 0 hp
    assert hero.hp == 0
    assert hero.is_alive() is False

def test_player_over_damage():
    #ETANT DONNE DEUX PERSONNAGES monstre et hero
    hero = Character()
    monster = Character()

    #QUAND MONSTRE TAPE ASSEZ LE HERO POUR QU'IL MEURT, PUIS TAPE DEUX FOIS DE PLUS 
    while(hero.hp>0):
        monster.attack(hero)
    
    for i in range (2):
        monster.attack(hero)
        
    #Hero doit mourir et ne pas perdre plus d'hp que 0
    assert hero.hp == 0
    assert hero.is_alive() is False
 
def test_dead_player_cant_attack():
    #ETANT DONNE DEUX PERSONNAGES monstre et hero 
    hero = Character()
    monster = Character()

