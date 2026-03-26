import pytest
from RPG.RPG import Character

def test_calcul_points_de_vie_initialisation():
    # ETANT DONNE un personnage de niveau 5 avec 10 d'endurance
    niveau = 5
    endurance = 10
    
    # QUAND le personnage est créé
    perso = Character(level=niveau, end=endurance)

    # ALORS ses PV doivent être 10 (base) + 10 (endu) + 2*5 (lvl) = 30
    assert perso.hp == 30

def test_erreur_armure_hors_limite_haute():
    # ETANT DONNE une valeur d'armure invalide de 101
    armure_invalide = 101
    
    # QUAND on tente de créer le personnage
    # ALORS une erreur ValueError est levée
    with pytest.raises(ValueError):
        Character(armor=armure_invalide)

def test_erreur_niveau_negatif():
    # ETANT DONNE un niveau invalide de 0
    niveau_invalide = 0
    
    # QUAND on tente de créer le personnage
    # ALORS une erreur ValueError est levée
    with pytest.raises(ValueError):
        Character(level=niveau_invalide)