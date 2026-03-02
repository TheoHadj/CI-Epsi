from Personnage import Personnage

def test_points_vie():
    # Étant donné un personnage
    perso = Personnage()
    # Lorqu'il subit 1 dégat
    perso.subir_degats()
    # Ses points de vie baisse de 1 point par dégat
    assert perso.get_points_vie() == 9