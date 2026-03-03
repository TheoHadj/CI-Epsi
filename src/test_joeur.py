from personnage import Personnage


def test_personnage_commence_avec_10_hp():
    p = Personnage()
    assert p.hp == 10


def test_attaque_enleve_1_hp():
    attaquant = Personnage()
    defenseur = Personnage()

    attaquant.attaquer(defenseur)

    assert defenseur.hp == 9


def test_personnage_meurt_a_zero():
    p = Personnage()
    p.hp = 1

    attaquant = Personnage()
    attaquant.attaquer(p)

    assert p.est_vivant() is False
