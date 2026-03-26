from unittest.mock import MagicMock
from RPG.RPG import Character, Equipe

def test_l_action_d_attaquer_declenche_la_reception_de_degats():
    # ETANT DONNE un attaquant et un défenseur simulé (Mock)
    attaquant = Character(level=1)
    defenseur_fantome = MagicMock(spec=Character)
    defenseur_fantome.is_alive.return_value = True
    
    # QUAND l'attquant lance une offensive
    attaquant.attack(defenseur_fantome)
    
    # ALORS le défenseur doit enregistrer l'impact de l'attaque
    assert defenseur_fantome.take_damage.called

def test_choix_du_membre_le_plus_vulnerable_selon_sa_sante_relative():
    # ETANT DONNE une équipe avec deux membres
    # Premier membre : 10/20 (50%) -> PAS en danger
    premier_membre = MagicMock(spec=Character)
    premier_membre.hp = 10
    premier_membre.maxHp = 20
    premier_membre.is_alive.return_value = True
    premier_membre.est_en_danger.return_value = False 
    
    # Second membre : 5/20 (25%) -> EN DANGER
    second_membre = MagicMock(spec=Character)
    second_membre.hp = 5
    second_membre.maxHp = 20
    second_membre.is_alive.return_value = True
    second_membre.est_en_danger.return_value = True # Indispensable pour la nouvelle logique
    
    equipe = Equipe(premier_membre, second_membre)
    
    # QUAND on demande d'identifier le membre le plus affaibli
    plus_faible = equipe.whoLowest()
    
    # ALORS c'est le second membre qui est choisi car il est en danger (< 30%)
    assert plus_faible == second_membre