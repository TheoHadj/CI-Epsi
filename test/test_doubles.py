from unittest.mock import MagicMock
from RPG.RPG import Character, Equipe

def test_attaque_appelle_take_damage_sur_cible():
    # ETANT DONNE un attaquant et une cible factice (Mock)
    attaquant = Character(level=1)
    cible_mock = MagicMock(spec=Character)
    cible_mock.is_alive.return_value = True
    
    # QUAND l'attaquant attaque la cible
    attaquant.attack(cible_mock)
    
    # ALORS la méthode take_damage de la cible doit être appelée
    assert cible_mock.take_damage.called

def test_who_lowest_calcul_ratio_correct():
    # ETANT DONNE une équipe avec des doublures dont on contrôle les PV
    p1 = MagicMock(spec=Character)
    p1.hp = 10
    p1.maxHp = 20 # 50%
    
    p2 = MagicMock(spec=Character)
    p2.hp = 5
    p2.maxHp = 20 # 25%
    
    equipe = Equipe(p1, p2)
    
    # QUAND on demande le plus faible
    resultat = equipe.whoLowest()
    
    # ALORS c'est p2 qui est choisi
    assert resultat == p2