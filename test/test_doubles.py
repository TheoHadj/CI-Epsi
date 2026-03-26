from RPG.RPG import Equipe
from test.utils.PersonnageBuilder import CharacterBuilder

def test_l_action_d_attaquer_declenche_la_reception_de_degats():
    # ETANT DONNE un attaquant réel et une cible simulée (Doublure)
    attaquant = CharacterBuilder().with_lvl(1).build()
    cible_simulee = CharacterBuilder().as_mock().build()
    
    # QUAND l'attaquant lance une offensive
    attaquant.attack(cible_simulee)
    
    # ALORS la cible doit enregistrer l'impact (appel de la méthode take_damage)
    assert cible_simulee.take_damage.called

def test_choix_du_membre_le_plus_vulnerable_selon_sa_sante_relative():
    # ETANT DONNE une équipe avec deux cibles aux états différents
    # Le premier membre est sain (50% PV, pas en danger)
    premier_membre = (CharacterBuilder()
                      .as_mock()
                      .avec_sante(10, 20)
                      .en_danger(False)
                      .build())
    
    # Le second membre est en danger critique (25% PV)
    second_membre = (CharacterBuilder()
                     .as_mock()
                     .avec_sante(5, 20)
                     .en_danger(True)
                     .build())
    
    equipe = Equipe(premier_membre, second_membre)
    
    # QUAND on demande d'identifier le membre le plus affaibli
    cible_identifiee = equipe.whoLowest()
    
    # ALORS c'est le second membre (en danger) qui est correctement priorisé
    assert cible_identifiee == second_membre

def test_identification_de_la_cible_unique_si_coequipier_hors_combat():
    # ETANT DONNE une équipe avec un membre valide et un membre tombé
    membre_valide = CharacterBuilder().as_mock().avec_sante(10, 10).build()
    membre_tombe = CharacterBuilder().as_mock().avec_sante(0, 10).build()
    
    equipe = Equipe(membre_valide, membre_tombe)
    
    # QUAND on cherche la cible la plus faible
    cible_choisie = equipe.whoLowest()
    
    # ALORS le système doit ignorer le membre mort et renvoyer le seul survivant
    assert cible_choisie == membre_valide