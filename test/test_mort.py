from Personnage import Personnage

def test_points_vie():
    # Étant donné un personnage
    perso = Personnage()
    # Lorsqu'il meurt
    for i in range (10):
            perso.subir_degats()
    # Ses points de vie sont à 0
    assert perso.get_points_vie() == 10