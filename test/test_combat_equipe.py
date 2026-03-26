from RPG.RPG import Equipe, Duel
from test.utils.PersonnageBuilder import CharacterBuilder

def test_equipe_survie_si_un_membre_est_en_vie():
    # ETANT DONNE une équipe composée d'un allié tombé et d'un allié valide
    allie_valide = CharacterBuilder().with_lvl(1).build()
    allie_tombe = CharacterBuilder().with_lvl(1).build()
    allie_tombe.take_damage(100)
    equipe = Equipe(allie_valide, allie_tombe)
    
    # QUAND on vérifie l'état de l'équipe
    # ALORS l'équipe est considérée comme encore apte au combat
    assert equipe.isAlive() is True

def test_ciblage_automatique_du_membre_le_plus_faible():
    # ETANT DONNE une équipe avec un guerrier en pleine forme et un archer blessé
    guerrier_sain = CharacterBuilder().with_lvl(1).build()
    archer_blesse = CharacterBuilder().with_lvl(1).build()
    archer_blesse.take_damage(6)
    equipe = Equipe(guerrier_sain, archer_blesse)
    
    # QUAND l'ennemi cherche la cible la plus vulnérable
    cible = equipe.whoLowest()
    
    # ALORS c'est l'archer blessé qui est désigné
    assert cible == archer_blesse

def test_victoire_logique_d_une_equipe_heroique_contre_des_monstres():
    # ETANT DONNE une équipe de héros puissants face à des adversaires faibles
    heros_1 = CharacterBuilder().with_lvl(100).with_force(50).with_agilite(10).build()
    heros_2 = CharacterBuilder().with_lvl(100).with_force(50).with_agilite(10).build()
    monstre_1 = CharacterBuilder().with_lvl(1).with_agilite(1).build()
    monstre_2 = CharacterBuilder().with_lvl(1).with_agilite(1).build()
    
    equipe_heros = Equipe(heros_1, heros_2)
    equipe_monstres = Equipe(monstre_1, monstre_2)
    duel = Duel(equipe_heros, equipe_monstres)
    
    # QUAND le duel se déroule
    vainqueur = duel.fight()
    
    # ALORS les héros remportent la victoire et les monstres sont vaincus
    assert vainqueur == 1
    assert equipe_monstres.isAlive() is False