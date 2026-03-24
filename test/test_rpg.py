from RPG.RPG import Character, Equipe, Duel
# from src.RPG.Character import Character #Refacto
from unittest.mock import MagicMock, Mock, patch

import pytest

from test.PersonnageBuilder import CharacterBuilder

def create_default_char(armor=0, arme=1):
    # return CharacterBuilder(level=1, end=0, force=0, agi=0, chn=0, armor=armor, arme=arme).build()
    return CharacterBuilder().with_lvl(1).with_endurance(0).with_force(0).with_agilite(0).with_armor(armor).with_arme(arme).build()

def test_player_initialization():
    #ETANT DONNE UN PERSONNAGE
    p = create_default_char()

    #doit avoir hp==10 + endurance + 2*lvl
    assert p.hp == 10 + p.endurance + 2* p.lvl

def test_player_initialization():
    #ETANT DONNE UN PERSONNAGE NIVEAU 1 AVEC 0 ENDURANCE
    p = create_default_char()

    #doit avoir hp==10 + 0 + 2*1 == 12
    assert p.hp == 12


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
    

def test_end_impact_hp():
    #Etant donné un personnage
    perso1 = create_default_char()

    #Alors ces hp sont égaux à baseHp = 10 et son base endurance = 0
    assert perso1.hp == 12
    assert perso1.endurance == 0

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

def test_armor_is_reducing_more_than_received():
    #Etant donné un perso1 possédant une armure de 100
    perso1 = create_default_char(100,1)

    hp0= perso1.hp

    #Quand heros reçoit des dommages égale à 0 de dégats
    perso1.take_damage(0)

    #La vie du perso1 ne doit pas changer.
    assert hp0 == perso1.hp

def test_degats_fixes():
    #Etant donné 2 Characters
    attaquant = Character() 
    cible = Character()
    
    #Quand l'attaquant attaque 6 hp à la cible
    with patch('src.RPG.RPG.random.randint', return_value=6):
        attaquant.attack(cible)
        
    #Alors la cible, qui a 12 hp, perd 6 hp, et se retrouve à 6 hp  
    assert cible.hp == 6

def test_deux_persos_armures():
    #Etant donné trois personnages, defenseurArmure possédant une armure de 50, un defenseurSansArmure et Attaquant
    defenseurArmure = create_default_char(50,1)
    h0=defenseurArmure.hp

    defenseurSansArmure = create_default_char(0,1)
    h02=defenseurSansArmure.hp

    Attaquant = create_default_char(0,1)

    #Quand heros reçoit une attaque de Attaquant qui a 0 de force et qui fera entre 0 et 1 de dégats, içi 1
    with patch('src.RPG.RPG.random.randint', return_value=1):
        Attaquant.attack(defenseurArmure)
        Attaquant.attack(defenseurSansArmure)

    #La vie du defenseurArmure ne doit pas changer.
    #La vie du perso1 ne doit pas changer.

    assert defenseurArmure.hp == h0
    assert defenseurSansArmure.hp < h02
    assert defenseurArmure.hp > defenseurSansArmure.hp

def test_demo_duel_gagne():
    # Étant un duel
    eq1_p1 = create_default_char()
    eq1_p2 = create_default_char(0, 1)
    eq2_p1 = create_default_char(0, 1.1)
    eq2_p2 = create_default_char(20, 1.2)
    equipe1 = Equipe(eq1_p1, eq1_p2)
    equipe2 = Equipe(eq2_p1, eq2_p2)
    duel = Duel(equipe1, equipe2)

    #Quand une équipe attaque une autre
    winner = duel.fight()

    #Alors il doit y avoir un gagnant
    assert winner in [1, 2]
    
    
# --------- Spy, Stubs and Dummys -----
def test_attack_calls_take_damage_spy():
    # Étant donné un attaquant et un défenseur (Spy)
    attacker = create_default_char()
    target_spy = MagicMock(wraps=create_default_char())
    
    # Lorsque l'attaquant porte un coup
    attacker.attack(target_spy)
    
    # Alors on vérifie que la méthode take_damage du défenseur a bien été appelée
    target_spy.take_damage.assert_called_once()

def test_who_lowest_logic_stub():
    # Étant donné une équipe avec deux personnages aux santés différentes (Stubs)
    p1 = MagicMock(spec=Character)
    p1.hp = 1
    p1.maxHp = 10
    p2 = MagicMock(spec=Character)
    p2.hp = 9
    p2.maxHp = 10
    eq = Equipe(p1, p2)
    
    # Lorsque on cherche le membre le plus faible
    result = eq.whoLowest()
    
    # Alors le personnage avec le plus bas ratio de PV est retourné
    assert result == p1

def test_duel_fight_with_dummies_and_stubs():
    # Étant donné un duel entre deux équipes composées de personnages fictifs (Dummies)
    p_dummy1 = Mock(spec=Character)
    p_dummy2 = Mock(spec=Character)
    p_dummy3 = Mock(spec=Character)
    p_dummy4 = Mock(spec=Character)
    
    eq1 = Equipe(p_dummy1, p_dummy2)
    eq1.isAlive = MagicMock(return_value=True) # Stub
    
    eq2 = Equipe(p_dummy3, p_dummy4)
    eq2.isAlive = MagicMock(side_effect=[True, False]) # Stub pour simuler la fin du combat
    
    duel = Duel(eq1, eq2)
    duel.getOrder = MagicMock(return_value=[p_dummy1, p_dummy3, p_dummy2, p_dummy4])
    duel.get_enemy_team = MagicMock(return_value=eq2)
    
    # Lorsque le combat se déroule
    winner = duel.fight()
    
    # Alors l'équipe 1 est déclarée vainqueur
    assert winner == 1

def test_demo_duel_gagne_with_stubs():
    # Étant donné des personnages avec des agilités fixes pour supprimer l'aléatoire (Stubs)
    eq1_p1 = MagicMock(spec=Character)
    eq1_p1.agi = 10
    eq1_p2 = MagicMock(spec=Character)
    eq1_p2.agi = 5
    
    eq2_p1 = MagicMock(spec=Character)
    eq2_p1.agi = 8
    eq2_p2 = MagicMock(spec=Character)
    eq2_p2.agi = 2
    
    equipe1 = Equipe(eq1_p1, eq1_p2)
    equipe1.isAlive = MagicMock(side_effect=[True, True, True])
    
    equipe2 = Equipe(eq2_p1, eq2_p2)
    equipe2.isAlive = MagicMock(side_effect=[True, False])
    
    duel = Duel(equipe1, equipe2)
    duel.getOrder = MagicMock(return_value=[eq1_p1, eq2_p1, eq1_p2, eq2_p2])
    
    # Lorsque le combat a lieu
    winner = duel.fight()
    
    # Alors l'issue du combat est déterministe
    assert winner == 1