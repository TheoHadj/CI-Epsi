from src.RPG import Character
import pytest

def test_player_initialization():
    #ETANT DONNE UN PERSONNAGE
    p = Character()

    #doit avoir hp==10 + endurance
    assert p.hp == 10 + p.endurance

def test_attack_reduces_hp():
    # ETANT DONNE deux personnages un perso et un hero avec 10 PV
    hero = Character()
    monster = Character()
    hp0 = monster.hp

    #QUAND LE HERO ATTAQUE LE perso
    hero.attack(monster)

    #LE perso doit perdre entre 0 et 1 hp + la force du hero
    assert hp0 - monster.hp >= 0
    assert hero.force >= 0 and hero.force <= 2 * hero.lvl

def test_player_death():
    #ETANT DONNE UN PERSONNAGE
    monster = Character()

    #QUAND IL PREND ASSEZ DE COUPS
    while(monster.hp>0) :
        monster.take_damage(1)
    
    #IL DOIT avoir 0 hp et ne plus être en vie
    assert monster.hp == 0
    assert monster.is_alive() is False

def test_player_kill():
    #ETANT DONNE DEUX PERSONNAGES perso et hero
    hero = Character()
    monster = Character()

    #QUAND perso TAPE HERO JUSQU'A 0 HP
    while(hero.hp>0) :
        monster.attack(hero)
    
    #Hero doit mourir et avoir 0 hp
    assert hero.hp == 0
    assert hero.is_alive() is False

def test_player_over_damage():
    #ETANT DONNE DEUX PERSONNAGES perso et hero
    hero = Character()
    monster = Character()

    #QUAND perso TAPE ASSEZ LE HERO POUR QU'IL MEURT, PUIS TAPE DEUX FOIS DE PLUS 
    while(hero.hp>0):
        monster.attack(hero)
    
    for i in range (2):
        monster.attack(hero)
        
    #Hero doit mourir et ne pas perdre plus d'hp que 0
    assert hero.hp == 0
    assert hero.is_alive() is False
 
def test_dead_player_cant_attack():
    #ETANT DONNE DEUX PERSONNAGES perso et hero 
    hero = Character()
    heroHp0=hero.hp
    monster = Character()

    #QUAND perso EST MORT ET QU'IL ATTAQUE
    while(monster.hp>0):
        hero.attack(monster)

    #ALORS perso NE FAIT PAS DE DEGAT A HERO.
    assert hero.hp==heroHp0

def test_valid_take_damage_argument():
    # Etant donné un personnage
    hero = Character()
    hero_base_hp = hero.hp
    
    # Lorsqu'un personnage subit des dégats, et que la valeur des dégats subits n'est pas un nombre supérieur à 0
    hero.take_damage(-1)
    
    # Alors le perso ne doit pas perdre points de vie
    assert hero.hp == hero_base_hp

    hero.take_damage("1")
    assert hero.hp == hero_base_hp
    
    hero.take_damage(hero)
    assert hero.hp == hero_base_hp

def test_has_endu():
    #Etant donné un personnage
    hero = Character()
    
    baseEnd= hero.endurance
    #Quand il vient d'être créé
    #Alors il a 0 d'endurance
    assert hero.endurance == 0


    #Quand il gagne un niveau
    hero.levelUp()
    #Alors il gagne 2 d'endurance
    assert hero.endurance == 2
    assert (baseEnd + 2) == 2

def test_end_impact_hp():
    #Etant donné un personnage
    hero = Character()

    #Alors ces hp sont égaux à baseHp + son endurance
    assert hero.hp == hero.baseHp + hero.endurance 
    
def test_levelUp():
    #Etant donné un personnage
    hero = Character()
    
    damage0= hero.force
    hp0= hero.hp

    #Quand il gagne un niveau
    hero.levelUp()

    #Alors ses dégats et ses hp augmente de deux
    assert hero.force == damage0+2
    assert hero.hp == hp0+2

    #Quand il gagne un autre niveau
    hero.levelUp()

    #Alors ses dégats et ses hp augmente de quatre (2*lvl)
    assert hero.force == damage0+4
    assert hero.hp == hp0+4
     


def test_caracteristique_force():
    # Étant donné un personnage
    perso = Character()
    ennemi = Character()

    perso_force = perso.force
    perso_base_hp = perso.hp
    
    # Il possède une caractéristique Force qui augmente ses dégats
    assert perso_force >= 0
    ennemi.attack(perso)
    assert perso.hp <= perso_base_hp

def test_armor_is_over_powered():
    #Etant donné un hero possédant une armure de 102 
    hero = Character(102)
    
    #Le héro ne peut pas être créer.
    assert hero == False 

def test_armor_is_over_powered():
    #Etant donné un hero possédant une armure de 102 
    with pytest.raises(ValueError):
        Character(102)
    
    #Le héro ne peut pas être créer.
def test_armor_is_negative():
    #Etant donné un hero possédant une armure de -2 
    with pytest.raises(ValueError):
        Character(-2)
    
    #Le héro ne peut pas être créer.
     

def test_is_armor_reducing_damage_taken():
    #Etant donné un hero possédant une armure de 50 
    hero = Character(50)
    hp0= hero.hp

    #Quand heros reçoit des dommages égale à 2 de dégats
    hero.take_damage(2)
    
    #Le héro doit perdre 1 hp.
    assert (hp0 - 1)== hero.hp 
    
def test_is_max_armor_protect_damage_taken():
    #Etant donné un hero possédant une armure de 1 
    hero = Character(100)
    hp0= hero.hp

    #Quand heros reçoit des dommages égale à 1 de dégats
    hero.take_damage(1)
    
    #Le héro la vie de hero ne doit pas changer.
    assert hp0 == hero.hp 
    
def test_is_armor_reducing_attack_receive():
    #Etant donné deux personnages, hero possédant une armure de 1 et perso 
    hero = Character(50)
    h0=hero.hp
    perso = Character()

    #Quand heros reçoit une attaque de perso qui a 0 de force et qui fera entre 0 et 1 de dégats
    perso.attack(hero)
    
    #La vie du hero ne doit pas changer.

    assert hero.hp == h0 
    
def test_armor_is_reducing_more_than_received():
    #Etant donné un hero possédant une armure de 3 
    hero = Character(100)
    hp0= hero.hp

    #Quand heros reçoit des dommages égale à 1 de dégats
    hero.take_damage(0)
    
    #La vie du hero ne doit pas changer.
    assert hp0 == hero.hp 