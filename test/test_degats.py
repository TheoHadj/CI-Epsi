from unittest.mock import patch
from test.utils.PersonnageBuilder import CharacterBuilder

def test_reduction_des_dommages_par_la_protection_physique():
    # ETANT DONNE un défenseur disposant de 50% de protection
    defenseur = CharacterBuilder().with_armor(50).build()
    sante_initiale = defenseur.hp
    
    # QUAND il reçoit une attaque de 10 points de dommages
    defenseur.take_damage(10)
    
    # ALORS sa santé ne diminue que de 5 points (moitié des dégâts)
    assert defenseur.hp == sante_initiale - 5

def test_invulnerabilite_avec_une_protection_totale():
    # ETANT DONNE un sujet en armure complète (100% protection)
    sujet_blindé = CharacterBuilder().with_armor(100).build()
    sante_initiale = sujet_blindé.hp
    
    # QUAND il subit une attaque massive de 100 points
    sujet_blindé.take_damage(100)
    
    # ALORS sa santé reste inchangée
    assert sujet_blindé.hp == sante_initiale

def test_calcul_des_dommages_aleatoires_selon_la_puissance():
    # ETANT DONNE un attaquant et un défenseur sans protection
    attaquant = CharacterBuilder().with_lvl(1).with_force(0).build()
    defenseur = CharacterBuilder().build()
    sante_initiale = defenseur.hp
    
    # QUAND l'attaquant porte un coup (jet de dé fixé à 3 via mock)
    with patch('random.randint', return_value=3):
        attaquant.attack(defenseur)
        
    # ALORS le défenseur perd exactement la valeur de l'attaque
    assert defenseur.hp == sante_initiale - 3

def test_limite_basse_des_points_de_vie_a_zero():
    # ETANT DONNE un sujet avec peu de points de vie
    sujet = CharacterBuilder().with_lvl(1).build()
    
    # QUAND il subit des dommages largement supérieurs à sa santé
    sujet.take_damage(200)
    
    # ALORS sa santé ne devient pas négative, elle s'arrête à zéro
    assert sujet.hp == 0
    assert not sujet.is_alive()

def test_calcul_des_dommages_minimums_obligatoires():
    # ETANT DONNE un défenseur avec une armure quasi-impénétrable (99%)
    defenseur = CharacterBuilder().with_armor(99).build()
    sante_initiale = defenseur.hp
    
    # QUAND il subit 1 point de dégât
    defenseur.take_damage(1)
    
    # ALORS il perd au moins 1 PV (règle du dégât minimum pour éviter les arrondis à 0)
    assert defenseur.hp == sante_initiale - 1

def test_rejet_des_valeurs_de_degats_invalides():
    # ETANT DONNE un sujet intact
    sujet = CharacterBuilder().build()
    sante_initiale = sujet.hp
    
    # QUAND on tente d'infliger des dégâts négatifs ou des types non-numériques
    sujet.take_damage(-50)
    sujet.take_damage("attaque_magique")
    
    # ALORS la santé du sujet reste inchangée
    assert sujet.hp == sante_initiale

def test_gestion_des_arrondis_de_degats_flottants():
    # ETANT DONNE un défenseur avec 50% d'armure
    defenseur = CharacterBuilder().with_armor(50).build()
    sante_initiale = defenseur.hp
    
    # QUAND il subit une attaque de 0.4 (0.4 * 0.5 = 0.2)
    # L'arrondi doit être à l'entier le plus proche (0)
    defenseur.take_damage(0.4)
    
    # ALORS sa santé ne bouge pas
    assert defenseur.hp == sante_initiale

