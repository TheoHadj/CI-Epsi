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
    
def test_priorite_cible_en_danger_critique():
    # ETANT DONNE une équipe avec :
    # Membre A : 10/40 PV (25% -> EN DANGER)
    # Membre B : 8/20 PV (40% -> SAIN)
    membre_en_danger = CharacterBuilder().with_endurance(26).with_lvl(1).build() # maxHp 40
    membre_en_danger.take_damage(30) 
    
    membre_faible_mais_sain = CharacterBuilder().with_lvl(1).build() # maxHp 12
    membre_faible_mais_sain.take_damage(4) 
    
    equipe = Equipe(membre_en_danger, membre_faible_mais_sain)
    
    # QUAND l'ennemi cherche la cible
    cible = equipe.whoLowest()
    
    # ALORS il choisit celui qui est en danger (< 30%) même s'il a plus de PV bruts que l'autre
    assert cible == membre_en_danger