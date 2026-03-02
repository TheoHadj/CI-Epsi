from personnage import Personnage

def test_points_vie():
    # Étant donné un personnage
    # Lorsqu'il est créé
    perso = Personnage()
    # Il possède 10 points de vie
    assert perso.get_points_vie() == 10