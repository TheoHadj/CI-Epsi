from RPG import Character
import pytest

def test_player_initialization():
    #ETANT DONNE UN PERSONNAGE
    p = Character()

    #doit avoir hp==10 + endurance
    assert p.hp == 10 + p.endurance

def test_attack_reduces_hp():
    # ETANT DONNE deux personnages un perso et un perso1 avec 10 PV
    perso1 = Character()
    perso2 = Character()
    hp0 = perso2.hp

    #QUAND LE perso1 ATTAQUE LE perso
    perso1.attack(perso2)

    #LE perso doit perdre entre 0 et 1 hp + la force du perso1
    assert hp0 - perso2.hp >= 0
    assert perso1.force >= 0 and perso1.force <= 2 * perso1.lvl

def test_player_death():
    #ETANT DONNE UN PERSONNAGE
    perso2 = Character()

    #QUAND IL PREND ASSEZ DE COUPS
    while(perso2.hp>0) :
        perso2.take_damage(1)
    
    #IL DOIT avoir 0 hp et ne plus être en vie
    assert perso2.hp == 0
    assert perso2.is_alive() is False

def test_player_kill():
    #ETANT DONNE DEUX PERSONNAGES perso et perso1
    perso1 = Character()
    perso2 = Character()

    #QUAND perso TAPE perso1 JUSQU'A 0 HP
    while(perso1.hp>0) :
        perso2.attack(perso1)
    
    #perso1 doit mourir et avoir 0 hp
    assert perso1.hp == 0
    assert perso1.is_alive() is False

def test_player_over_damage():
    #ETANT DONNE DEUX PERSONNAGES perso et perso1
    perso1 = Character()
    perso2 = Character()

    #QUAND perso TAPE ASSEZ LE perso1 POUR QU'IL MEURT, PUIS TAPE DEUX FOIS DE PLUS 
    while(perso1.hp>0):
        perso2.attack(perso1)
    
    for i in range (2):
        perso2.attack(perso1)
        
    #perso1 doit mourir et ne pas perdre plus d'hp que 0
    assert perso1.hp == 0
    assert perso1.is_alive() is False
 
def test_dead_player_cant_attack():
    #ETANT DONNE DEUX PERSONNAGES perso et perso1 
    perso1 = Character()
    heroHp0=perso1.hp
    perso2 = Character()

    #QUAND perso EST MORT ET QU'IL ATTAQUE
    while(perso2.hp>0):
        perso1.attack(perso2)

    #ALORS perso NE FAIT PAS DE DEGAT A perso1.
    assert perso1.hp==heroHp0

def test_valid_take_damage_argument():
    # Etant donné un personnage
    perso1 = Character()
    hero_base_hp = perso1.hp
    
    # Lorsqu'un personnage subit des dégats, et que la valeur des dégats subits n'est pas un nombre supérieur à 0
    perso1.take_damage(-1)
    
    # Alors le perso ne doit pas perdre points de vie
    assert perso1.hp == hero_base_hp

    perso1.take_damage("1")
    assert perso1.hp == hero_base_hp
    
    perso1.take_damage(perso1)
    assert perso1.hp == hero_base_hp

def test_has_endu():
    #Etant donné un personnage
    perso1 = Character()
    
    baseEnd= perso1.endurance
    #Quand il vient d'être créé
    #Alors il a 0 d'endurance
    assert perso1.endurance == 0


    #Quand il gagne un niveau
    perso1.levelUp()
    #Alors il gagne 2 d'endurance
    assert perso1.endurance == 2
    assert (baseEnd + 2) == 2

def test_end_impact_hp():
    #Etant donné un personnage
    perso1 = Character()

    #Alors ces hp sont égaux à baseHp + son endurance
    assert perso1.hp == perso1.baseHp + perso1.endurance 
    
def test_levelUp():
    #Etant donné un personnage
    perso1 = Character()
    
    damage0= perso1.force
    hp0= perso1.hp

    #Quand il gagne un niveau
    perso1.levelUp()

    #Alors ses dégats et ses hp augmente de deux
    assert perso1.force == damage0+2
    assert perso1.hp == hp0+2

    #Quand il gagne un autre niveau
    perso1.levelUp()

    #Alors ses dégats et ses hp augmente de quatre (2*lvl)
    assert perso1.force == damage0+4
    assert perso1.hp == hp0+4
     


def test_caracteristique_force():
    # Étant donné un personnage
    perso = Character()
    perso_2 = Character()

    perso_force = perso.force
    perso_base_hp = perso.hp
    
    # Il possède une caractéristique Force qui augmente ses dégats
    assert perso_force >= 0
    perso_2.attack(perso)
    assert perso.hp <= perso_base_hp

def test_armor_is_over_powered():
    #Etant donné un perso1 possédant une armure de 102 
    perso1 = Character(102)
    
    #Le héro ne peut pas être créer.
    assert perso1 == False 

def test_armor_is_over_powered():
    #Etant donné un perso1 possédant une armure de 102 
    with pytest.raises(ValueError):
        Character(102)
    
    #Le héro ne peut pas être créer.
def test_armor_is_negative():
    #Etant donné un perso1 possédant une armure de -2 
    with pytest.raises(ValueError):
        Character(-2)
    
    #Le héro ne peut pas être créer.
     

def test_is_armor_reducing_damage_taken():
    #Etant donné un perso1 possédant une armure de 50 
    perso1 = Character(50)
    hp0= perso1.hp

    #Quand heros reçoit des dommages égale à 2 de dégats
    perso1.take_damage(2)
    
    #Le héro doit perdre 1 hp.
    assert (hp0 - 1)== perso1.hp 
    
def test_is_max_armor_protect_damage_taken():
    #Etant donné un perso1 possédant une armure de 1 
    perso1 = Character(100)
    hp0= perso1.hp

    #Quand heros reçoit des dommages égale à 1 de dégats
    perso1.take_damage(1)
    
    #Le héro la vie de perso1 ne doit pas changer.
    assert hp0 == perso1.hp 
    
def test_is_armor_reducing_attack_receive():
    #Etant donné deux personnages, perso1 possédant une armure de 1 et perso 
    perso1 = Character(50)
    h0=perso1.hp
    perso = Character()

    #Quand heros reçoit une attaque de perso qui a 0 de force et qui fera entre 0 et 1 de dégats
    perso.attack(perso1)
    
    #La vie du perso1 ne doit pas changer.

    assert perso1.hp == h0 
    
def test_armor_is_reducing_more_than_received():
    #Etant donné un perso1 possédant une armure de 3 
    perso1 = Character(100)
    hp0= perso1.hp

    #Quand heros reçoit des dommages égale à 1 de dégats
    perso1.take_damage(0)
    
    #La vie du perso1 ne doit pas changer.
    assert hp0 == perso1.hp 