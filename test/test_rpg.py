from src.RPG.RPG import Character, Equipe, Duel

import pytest

def create_default_char(armor=0, arme=1):
    return Character(level=1, end=0, force=0, agi=0, chn=0, armor=armor, arme=arme)

def test_player_initialization():
    #ETANT DONNE UN PERSONNAGE
    p = create_default_char()

    #doit avoir hp==10 + endurance
    assert p.hp == 12 + p.endurance

def test_attack_reduces_hp():
    # ETANT DONNE deux personnages un perso et un perso1 avec 10 PV
    perso1 = create_default_char()
    perso2 = create_default_char()
    hp0 = perso2.hp

    #QUAND LE perso1 ATTAQUE LE perso
    perso1.attack(perso2)

    #LE perso doit perdre entre 0 et 1 hp + la force du perso1
    assert hp0 - perso2.hp >= 0
    assert perso1.force >= 0 and perso1.force <= 2 * perso1.lvl

def test_player_death():
    #ETANT DONNE UN PERSONNAGE
    perso2 = create_default_char()

    #QUAND IL PREND ASSEZ DE COUPS
    while(perso2.hp>0) :
        perso2.take_damage(1)

    #IL DOIT avoir 0 hp et ne plus être en vie
    assert perso2.hp == 0
    assert perso2.is_alive() is False

def test_player_kill():
    #ETANT DONNE DEUX PERSONNAGES perso et perso1
    perso1 = create_default_char()
    perso2 = create_default_char()

    #QUAND perso TAPE perso1 JUSQU'A 0 HP
    while(perso1.hp>0) :
        perso2.attack(perso1)

    #perso1 doit mourir et avoir 0 hp
    assert perso1.hp == 0
    assert perso1.is_alive() is False

def test_player_over_damage():
    #ETANT DONNE DEUX PERSONNAGES perso et perso1
    perso1 = create_default_char()
    perso2 = create_default_char()

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
    perso1 = create_default_char()
    heroHp0=perso1.hp
    perso2 = create_default_char()

    #QUAND perso EST MORT ET QU'IL ATTAQUE
    while(perso2.hp>0):
        perso1.attack(perso2)

    #ALORS perso NE FAIT PAS DE DEGAT A perso1.
    assert perso1.hp==heroHp0

def test_valid_take_damage_argument():
    # Etant donné un personnage
    perso1 = create_default_char()
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
    perso1 = create_default_char()

    #Quand il vient d'être créé
    #Alors il a 0 d'endurance
    assert perso1.endurance == 0

    perso2 = Character(arme=1, armor=0, end=2, force=0, agi=0, chn=0, level=1)
    #Alors il gagne 2 d'endurance
    assert perso2.endurance == 2
    

def test_end_impact_hp():
    #Etant donné un personnage
    perso1 = create_default_char()

    #Alors ces hp sont égaux à baseHp + son endurance
    assert perso1.hp == 10 + perso1.lvl*2 + perso1.endurance

# def test_levelUp():
#     #Etant donné un personnage
#     perso1 = create_default_char()

#     damage0= perso1.force
#     hp0= perso1.hp

#     #Quand il gagne un niveau
#     perso1.levelUp()

#     #Alors ses dégats et ses hp augmente de deux
#     assert perso1.force == damage0+2
#     assert perso1.hp == hp0+2

#     #Quand il gagne un autre niveau
#     perso1.levelUp()

#     #Alors ses dégats et ses hp augmente de quatre (2*lvl)
#     assert perso1.force == damage0+4
#     assert perso1.hp == hp0+4



def test_caracteristique_force():
    # Étant donné un personnage
    perso = create_default_char()
    perso2 = create_default_char()

    perso_force = perso.force
    perso_base_hp = perso.hp

    # Il possède une caractéristique Force qui augmente ses dégats
    assert perso_force >= 0
    perso2.attack(perso)
    assert perso.hp <= perso_base_hp

def test_armor_is_over_powered():
    #Etant donné un perso1 possédant une armure de 102
    with pytest.raises(ValueError):
        create_default_char(101,1)
    #Le héro ne peut pas être créer.


def test_armor_is_negative():
    #Etant donné un perso1 possédant une armure de -2
    with pytest.raises(ValueError):
        create_default_char(-2,1)

    #Le héro ne peut pas être créer.


def test_is_armor_reducing_damage_taken():
    #Etant donné un perso1 possédant une armure de 50
    perso1 = create_default_char(50,1)

    hp0= perso1.hp

    #Quand heros reçoit des dommages égale à 2 de dégats
    perso1.take_damage(2)

    #Le héro doit perdre 1 hp.
    assert (hp0 - 1)== perso1.hp

def test_is_max_armor_protect_damage_taken():
    #Etant donné un perso1 possédant une armure de 1
    perso1 = create_default_char(100,1)
    hp0= perso1.hp

    #Quand heros reçoit des dommages égale à 1 de dégats
    perso1.take_damage(1)

    #la vie de perso1 ne doit pas changer.
    assert hp0 == perso1.hp

def test_is_armor_reducing_attack_receive():
    #Etant donné deux personnages, perso1 possédant une armure de 50 et perso
    perso1 = create_default_char(50,1)
    h0=perso1.hp
    perso = create_default_char()

    #Quand heros reçoit une attaque de perso qui a 0 de force et qui fera entre 0 et 1 de dégats
    perso.attack(perso1)

    #La vie du perso1 ne doit pas changer.

    assert perso1.hp == h0

def test_armor_is_reducing_more_than_received():
    #Etant donné un perso1 possédant une armure de 100
    perso1 = create_default_char(100,1)

    hp0= perso1.hp

    #Quand heros reçoit des dommages égale à 0 de dégats
    perso1.take_damage(0)

    #La vie du perso1 ne doit pas changer.
    assert hp0 == perso1.hp

# def test_demo_arme_attaque_hausse():
#     # Étant donné un personnage ayant une arme et un perso2
#     perso_arme = create_default_char(0, 1.2)
#     perso_sans_arme = create_default_char(0,1.2)
#     perso2 = create_default_char(0,1.2)
#     ennemi2 = create_default_char(0,1.2)

#     # Lorsque le personnage armé attaque l'perso2
#     perso_arme.attack(perso2)
#     perso_sans_arme.attack(ennemi2)

#     # Alors l'perso2 subit plus de dégâts que lors d'une attaque sans arme
#     assert perso2.hp <= 10 and perso2.hp >= 4
#     assert ennemi2.hp <= 10 and ennemi2.hp >= 5


# def test_demo_arme_attaque_baisse():
#     # Étant donné un personnage ayant une arme et un autre personnage
#     perso_arme = create_default_char(0, 0.5)
#     perso_sans_arme = create_default_char(0,1.2)
#     perso2 = create_default_char(0,1.2)
#     ennemi2 = create_default_char(0,1.2)

#     # Lorsque le personnage armé attaque le second personnage
#     perso_arme.attack(perso2)
#     perso_sans_arme.attack(ennemi2)

#     # Alors l'perso2 subit moins de dégâts que lors d'une attaque sans arme
#     assert perso2.hp <= 10 and perso2.hp >= 2.5
#     assert ennemi2.hp <= 10 and ennemi2.hp >= 5


def test_deux_persos_armures():
    #Etant donné trois personnages, perso1 possédant une armure de 50, un perso1 sans et perso
    perso1 = create_default_char(50,1)
    h0=perso1.hp

    perso2 = create_default_char(0,1)
    h02=perso2.hp

    perso = create_default_char(0,1.2)

    #Quand heros reçoit une attaque de perso qui a 0 de force et qui fera entre 0 et 1 de dégats
    perso.attack(perso1)
    perso.attack(perso2)

    #La vie du perso1 ne doit pas changer.

    assert perso1.hp == h0
    assert perso1.hp != perso2.hp

def test_demo_duel_gagne():
    # Étant un duel
    eq1_p1 = create_default_char(50, 1.5)
    eq1_p2 = create_default_char(0, 1)
    eq2_p1 = create_default_char(0, 1.1)
    eq2_p2 = create_default_char(20, 1.2)
    equipe1 = Equipe(eq1_p1, eq1_p2)
    equipe2 = Equipe(eq2_p1, eq2_p2)
    duel = Duel(equipe1, equipe2)

    #Quand le combat a lieu
    winner = duel.fight()

    #Alors il doit y avoir un gagnant
    assert winner in [1, 2]