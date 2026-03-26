from RPG.RPG import Equipe, Duel
from test.utils.PersonnageBuilder import CharacterBuilder

def test_equipe_survie_si_un_membre_est_en_vie():
    # ETANT DONNE une équipe avec un membre mort et un membre vivant
    vivant = CharacterBuilder().with_lvl(1).build()
    mort = CharacterBuilder().with_lvl(1).build()
    mort.take_damage(100)
    equipe = Equipe(vivant, mort)
    
    # QUAND on vérifie si l'équipe est en vie
    # ALORS le résultat est vrai
    assert equipe.isAlive() is True

def test_ciblage_membre_plus_faible_valide():
    # ETANT DONNE une équipe avec un perso A (100% PV) et un perso B (50% PV)
    perso_a = CharacterBuilder().with_lvl(1).build()
    perso_b = CharacterBuilder().with_lvl(1).build()
    perso_b.take_damage(6)
    equipe = Equipe(perso_a, perso_b)
    
    # QUAND on cherche le membre le plus faible
    faible = equipe.whoLowest()
    
    # ALORS c'est le perso B qui est retourné
    assert faible == perso_b

def test_victoire_duel_equipe_surpuissante():
    # ETANT DONNE une équipe niveau 100 contre une équipe niveau 1
    fort_1 = CharacterBuilder().with_lvl(100).with_force(50).with_agilite(10).build()
    fort_2 = CharacterBuilder().with_lvl(100).with_force(50).with_agilite(10).build()
    faible_1 = CharacterBuilder().with_lvl(1).with_agilite(1).build()
    faible_2 = CharacterBuilder().with_lvl(1).with_agilite(1).build()
    
    eq1 = Equipe(fort_1, fort_2)
    eq2 = Equipe(faible_1, faible_2)
    duel = Duel(eq1, eq2)
    
    # QUAND le combat a lieu
    gagnant = duel.fight()
    
    # ALORS l'équipe 1 gagne forcément rapidement
    assert gagnant == 1
    assert eq2.isAlive() is False

def test_equipe_morte_quand_tous_les_membres_sont_morts():
    # ETANT DONNE deux personnages morts
    p1 = CharacterBuilder().build()
    p2 = CharacterBuilder().build()
    p1.take_damage(100)
    p2.take_damage(100)
    
    # QUAND ils forment une équipe
    equipe = Equipe(p1, p2)
    
    # ALORS l'équipe est considérée comme morte
    assert equipe.isAlive() is False