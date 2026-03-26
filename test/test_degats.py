from unittest.mock import patch
from test.utils.PersonnageBuilder import CharacterBuilder

def test_reduction_des_dommages_par_la_protection_physique():
    # ETANT DONNE un défenseur disposant de 50% de protection
    defenseur = CharacterBuilder().with_armor(50).with_lvl(1).build()
    sante_initiale = defenseur.hp
    
    # QUAND il reçoit une attaque de 10 points de dommages
    defenseur.take_damage(10)
    
    # ALORS sa santé ne diminue que de 5 points (moitié des dégâts)
    assert defenseur.hp == sante_initiale - 5

def test_invulnerabilite_avec_une_protection_totale():
    # ETANT DONNE un chevalier en armure complète (100% protection)
    chevalier = CharacterBuilder().with_armor(100).build()
    sante_initiale = chevalier.hp
    
    # QUAND il subit une attaque massive de 100 points
    chevalier.take_damage(100)
    
    # ALORS sa santé reste inchangée
    assert chevalier.hp == sante_initiale

def test_calcul_des_dommages_aleatoires_selon_la_force():
    # ETANT DONNE un attaquant de niveau 1
    attaquant = CharacterBuilder().with_lvl(1).with_force(0).build()
    cible = CharacterBuilder().build()
    
    # QUAND il porte un coup critique (jet de dé au maximum)
    with patch('random.randint', return_value=3):
        attaquant.attack(cible)
        
    # ALORS la cible subit exactement la valeur de l'attaque
    assert cible.hp == cible.maxHp - 3

def test_trepas_du_personnage_hors_de_combat():
    # ETANT DONNE un aventurier fragile
    aventurier = CharacterBuilder().with_lvl(1).build()
    
    # QUAND il subit des blessures fatales
    aventurier.take_damage(20)
    
    # ALORS sa santé tombe à zéro et il n'est plus en vie
    assert aventurier.hp == 0
    assert not aventurier.is_alive()