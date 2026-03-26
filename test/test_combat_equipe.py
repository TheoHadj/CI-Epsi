from RPG.RPG import Equipe, Duel
from test.utils.PersonnageBuilder import CharacterBuilder

def test_equipe_survie_si_un_membre_est_en_vie():
    # ETANT DONNE une équipe composée d'un membre hors de combat et d'un membre actif
    membre_actif = CharacterBuilder().with_lvl(1).build()
    membre_hors_combat = CharacterBuilder().with_lvl(1).build()
    membre_hors_combat.take_damage(100)
    equipe = Equipe(membre_actif, membre_hors_combat)
    
    # QUAND on vérifie l'état de l'équipe
    # ALORS l'équipe est considérée comme encore active
    assert equipe.isAlive() is True

def test_ciblage_prioritaire_du_defenseur_le_plus_faible():
    # ETANT DONNE une équipe avec un défenseur intact et un défenseur blessé
    def_intact = CharacterBuilder().with_lvl(1).build()
    def_blesse = CharacterBuilder().with_lvl(1).build()
    def_blesse.take_damage(6)
    equipe = Equipe(def_intact, def_blesse)
    
    # QUAND un attaquant cherche la cible la plus vulnérable
    cible = equipe.whoLowest()
    
    # ALORS c'est le défenseur blessé qui est désigné
    assert cible == def_blesse
    
def test_victoire_logique_d_une_equipe_a_haut_niveau():
    # ETANT DONNE une équipe A de haut niveau face à une équipe B de bas niveau
    a1 = CharacterBuilder().with_lvl(100).with_force(50).with_agilite(10).build()
    a2 = CharacterBuilder().with_lvl(100).with_force(50).with_agilite(10).build()
    b1 = CharacterBuilder().with_lvl(1).with_agilite(1).build()
    b2 = CharacterBuilder().with_lvl(1).with_agilite(1).build()

    equipe_a = Equipe(a1, a2)
    equipe_b = Equipe(b1, b2)
    duel = Duel(equipe_a, equipe_b)

    # QUAND le duel se déroule
    gagnant = duel.fight()

    # ALORS l'équipe A remporte la victoire
    assert gagnant == 1
    assert equipe_b.isAlive() is False

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
    
def test_priorite_cible_sous_le_seuil_de_danger():
    # ETANT DONNE une équipe avec :
    # Défenseur A : 25% de santé (Sous le seuil de 30%)
    # Défenseur B : 40% de santé (Au-dessus du seuil)
    def_en_danger = CharacterBuilder().with_endurance(26).with_lvl(1).build() # maxHp 40
    def_en_danger.take_damage(30)
    
    def_sain = CharacterBuilder().with_lvl(1).build() # maxHp 12
    def_sain.take_damage(4)
    
    equipe = Equipe(def_en_danger, def_sain)
    
    # QUAND on cherche la cible prioritaire
    cible = equipe.whoLowest()
    
    # ALORS le défenseur sous le seuil de danger est priorisé
    assert cible == def_en_danger
    
def test_seuil_exact_danger_trente_pourcent():
    # ETANT DONNE un personnage avec 100 PV Max
    perso = CharacterBuilder().with_endurance(88).with_lvl(1).build() # maxHp 100
    
    # QUAND il a exactement 30 PV (30/100 = 30%)
    perso.take_damage(70)
    
    # ALORS il n'est PAS encore considéré en danger (car la règle est < 30%)
    assert perso.est_en_danger() is False
    
    # QUAND il perd 1 PV de plus (29/100 = 29%)
    perso.take_damage(1)
    
    # ALORS il est considéré en danger
    assert perso.est_en_danger() is True

def test_priorite_danger_meme_si_pv_bruts_superieurs():
    # ETANT DONNE une équipe avec :
    # Attaquant A : 29/100 PV (29% -> EN DANGER)
    # Attaquant B : 10/20 PV  (50% -> SAIN)
    p_danger = CharacterBuilder().with_endurance(88).with_lvl(1).build() # 100HP
    p_danger.take_damage(71)
    
    p_sain = CharacterBuilder().with_endurance(8).with_lvl(1).build() # 20HP
    p_sain.take_damage(10)
    
    equipe = Equipe(p_danger, p_sain)
    
    # QUAND on cherche la cible la plus prioritaire
    cible = equipe.whoLowest()
    
    # ALORS c'est celui en danger qui est choisi, malgré ses 29 PV contre 10
    assert cible == p_danger
