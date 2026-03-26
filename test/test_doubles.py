from unittest.mock import MagicMock
from RPG.RPG import Character, Equipe

def test_l_action_d_attaquer_declenche_la_reception_de_degats():
    # ETANT DONNE un attaquant et un défenseur simulé (Mock)
    attaquant = Character(level=1)
    defenseur_fantome = MagicMock(spec=Character)
    defenseur_fantome.is_alive.return_value = True
    
    # QUAND l'attaquant lance une offensive
    attaquant.attack(defenseur_fantome)
    
    # ALORS le défenseur doit enregistrer l'impact de l'attaque
    assert defenseur_fantome.take_damage.called

def test_choix_du_membre_le_plus_vulnerable_selon_sa_sante_relative():
    # ETANT DONNE une équipe avec deux membres aux états de santé différents
    premier_membre = MagicMock(spec=Character)
    premier_membre.hp = 10
    premier_membre.maxHp = 20 # 50% de santé
    
    second_membre = MagicMock(spec=Character)
    second_membre.hp = 5
    second_membre.maxHp = 20 # 25% de santé
    
    equipe = Equipe(premier_membre, second_membre)
    
    # QUAND on demande d'identifier le membre le plus affaibli
    plus_faible = equipe.whoLowest()
    
    # ALORS c'est le second membre qui est correctement identifié
    assert plus_faible == second_membre