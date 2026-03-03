from personnage import Personnage
from combat import Combat


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

#def test_un_mort_ne_peut_pas_attaquer():
  #  attaquant = Personnage()
  #  defenseur = Personnage()

  #  attaquant.hp = 0  # mort
  #  attaquant.attaquer(defenseur)

  #  assert defenseur.hp == 10  # aucun dégât

def test_un_mort_ne_peut_pas_attaquer():
    p1 = Personnage()
    p2 = Personnage()

    p1.hp = 0
    p1.attaquer(p2)

    assert p2.hp == 10


def test_on_ne_peut_pas_attaquer_un_mort():
    attaquant = Personnage()
    defenseur = Personnage()

    defenseur.hp = 0  # mort
    attaquant.attaquer(defenseur)

    assert defenseur.hp == 0  # reste mort

def test_combat_tour_par_tour_jusqua_mort():
    p1 = Personnage()
    p2 = Personnage()

    combat = Combat(p1, p2)
    gagnant = combat.lancer()

    assert gagnant.est_vivant()
    assert not (p1.est_vivant() and p2.est_vivant())
