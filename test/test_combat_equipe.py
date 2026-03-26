from RPG.RPG import Equipe, Duel
from test.utils.PersonnageBuilder import CharacterBuilder
from unittest.mock import patch

# --- TESTS DE VIE ET SURVIE ---

def test_equipe_survie_si_un_membre_est_en_vie():
    # ETANT DONNE une équipe avec un membre mort et un membre vif
    membre_actif = CharacterBuilder().with_lvl(1).build()
    membre_hors_combat = CharacterBuilder().with_lvl(1).build()
    membre_hors_combat.take_damage(100)
    equipe = Equipe(membre_actif, membre_hors_combat)
    
    # ALORS l'équipe est toujours en vie
    assert equipe.isAlive() is True

def test_equipe_morte_quand_tous_les_membres_sont_morts():
    # ETANT DONNE deux personnages KO
    p1 = CharacterBuilder().build()
    p2 = CharacterBuilder().build()
    p1.take_damage(100)
    p2.take_damage(100)
    equipe = Equipe(p1, p2)

    # ALORS l'équipe est morte
    assert equipe.isAlive() is False

# --- TESTS DE CIBLAGE (whoLowest) ---

def test_ignore_membre_1_si_mort():
    # ETANT DONNE M1 mort et M2 vif
    m1 = CharacterBuilder().avec_sante(0, 10).as_mock().build()
    m2 = CharacterBuilder().avec_sante(10, 10).as_mock().build()
    equipe = Equipe(m1, m2)
    # ALORS on cible forcément M2
    assert equipe.whoLowest() == m2

def test_priorite_ciblage_symetrie_membre_2_danger():
    # ETANT DONNE M1 sain et M2 en danger
    m1 = CharacterBuilder().avec_sante(10, 10).en_danger(False).as_mock().build()
    m2 = CharacterBuilder().avec_sante(2, 10).en_danger(True).as_mock().build()
    equipe = Equipe(m1, m2)
    # ALORS on cible M2 (le danger est prioritaire)
    assert equipe.whoLowest() == m2

def test_priorite_danger_meme_si_pv_bruts_superieurs():
    # ETANT DONNE M1 en danger (29 PV / 100) et M2 sain (10 PV / 20)
    p_danger = CharacterBuilder().with_endurance(88).with_lvl(1).build() # 100 HP
    p_danger.take_damage(71) # Reste 29 (Danger)
    
    p_sain = CharacterBuilder().with_endurance(8).with_lvl(1).build() # 20 HP
    p_sain.take_damage(10) # Reste 10 (Sain)
    
    equipe = Equipe(p_danger, p_sain)
    # ALORS c'est p_danger qui est choisi (priorité à l'état de danger sur les PV bruts)
    assert equipe.whoLowest() == p_danger

def test_choix_pire_ratio_quand_deux_en_danger():
    # ETANT DONNE deux membres en danger (M1: 25% vs M2: 10%)
    m1 = CharacterBuilder().avec_sante(5, 20).en_danger(True).as_mock().build()
    m2 = CharacterBuilder().avec_sante(2, 20).en_danger(True).as_mock().build()
    equipe = Equipe(m1, m2)
    # ALORS on prend le plus bas (M2)
    assert equipe.whoLowest() == m2

def test_choix_membre_1_si_ratios_egaux():
    # ETANT DONNE deux membres avec le même ratio
    m1 = CharacterBuilder().avec_sante(10, 10).as_mock().build()
    m2 = CharacterBuilder().avec_sante(10, 10).as_mock().build()
    equipe = Equipe(m1, m2)
    # ALORS on prend le premier (pour tuer le mutant sur le <=)
    assert equipe.whoLowest() == m1

# --- TESTS DE DUEL ET ORDRE ---

def test_ordre_action_base_sur_agilite():
    # ETANT DONNE deux persos avec des agilités différentes
    lent = CharacterBuilder().with_agilite(1).build()
    rapide = CharacterBuilder().with_agilite(50).build()
    duel = Duel(Equipe(lent, lent), Equipe(rapide, rapide))
    
    ordre = duel.getOrder()
    # ALORS le plus rapide doit être en premier dans la liste
    assert ordre[0] == rapide

def test_victoire_equipe_surpuissante():
    fort = CharacterBuilder().with_lvl(100).with_force(50).build()
    faible = CharacterBuilder().with_lvl(1).build()
    eq1, eq2 = Equipe(fort, fort), Equipe(faible, faible)
    duel = Duel(eq1, eq2)
    assert duel.fight() == 1
    assert eq2.isAlive() is False

# --- TEST DE SEUIL (FIXÉ) ---

def test_seuil_exact_danger_trente_pourcent_numerique():
    # ETANT DONNE un personnage ayant un maximum de 100 points de vie
    # (Calcul : 10 de base + 88 endurance + 2*1 niveau = 100 PV)
    perso = CharacterBuilder().with_endurance(88).with_lvl(1).build() 
    
    # QUAND il subit 70 points de dégâts pour atteindre exactement 30 PV
    perso.take_damage(70)
    
    # ALORS il n'est PAS considéré en danger (car 30/100 n'est pas strictement inférieur à 30%)
    assert perso.est_en_danger() is False
    
    # QUAND il subit 1 point de dégât supplémentaire (il tombe à 29 PV)
    perso.take_damage(1)
    
    # ALORS il passe en état de danger (car 29/100 est strictement inférieur à 30%)
    assert perso.est_en_danger() is True
    
def test_ciblage_membre_2_si_membre_1_mort_et_membre_2_en_danger():
    # ETANT DONNE une équipe où le membre 1 est mort
    # Et le membre 2 est en vie ET en danger
    m1_mort = CharacterBuilder().avec_sante(0, 10).as_mock().build()
    m2_danger = CharacterBuilder().avec_sante(2, 10).en_danger(True).as_mock().build()
    equipe = Equipe(m1_mort, m2_danger)
    
    # ALORS le système doit ignorer le mort et cibler le membre 2
    # (Cela tue les mutants qui inversent les ordres de priorité Vie vs Danger)
    assert equipe.whoLowest() == m2_danger

def test_identification_ennemi_duel():
    # ETANT DONNE un duel entre deux équipes
    eq1 = Equipe(CharacterBuilder().build(), CharacterBuilder().build())
    eq2 = Equipe(CharacterBuilder().build(), CharacterBuilder().build())
    duel = Duel(eq1, eq2)
    
    # QUAND on demande l'ennemi d'un membre de l'équipe 1
    # ALORS c'est l'équipe 2 qui est renvoyée
    assert duel.get_enemy_team(eq1.membre1) == eq2
    # ET inversement
    assert duel.get_enemy_team(eq2.membre1) == eq1

def test_get_enemy_team_renvoie_la_bonne_equipe():
    # ETANT DONNE un duel entre deux équipes distinctes
    eq1 = Equipe(CharacterBuilder().build(), CharacterBuilder().build())
    eq2 = Equipe(CharacterBuilder().build(), CharacterBuilder().build())
    duel = Duel(eq1, eq2)
    
    # QUAND on demande l'ennemi d'un membre de l'équipe 1
    # ALORS cela doit être l'équipe 2
    assert duel.get_enemy_team(eq1.membre1) == eq2
    assert duel.get_enemy_team(eq1.membre2) == eq2
    
    # ET QUAND on demande l'ennemi d'un membre de l'équipe 2
    # ALORS cela doit être l'équipe 1
    assert duel.get_enemy_team(eq2.membre1) == eq1
    
def test_ordre_action_agilite_identique():
    # ETANT DONNE deux personnages avec la MEME agilité
    p1 = CharacterBuilder().with_agilite(10).build()
    p2 = CharacterBuilder().with_agilite(10).build()
    duel = Duel(Equipe(p1, p1), Equipe(p2, p2))
    
    # QUAND on récupère l'ordre
    ordre = duel.getOrder()
    
    # ALORS la liste doit contenir les 4 membres (le tri ne doit pas en supprimer)
    assert len(ordre) == 4
    # ET l'ordre doit être stable (ne doit pas planter si les valeurs sont égales)
    assert p1 in ordre and p2 in ordre
    
def test_equipe_survie_si_membre_2_mort_uniquement():
    # ETANT DONNE M1 vivant et M2 mort
    m1 = CharacterBuilder().with_lvl(1).build()
    m2 = CharacterBuilder().with_lvl(1).build()
    m2.hp = 0
    equipe = Equipe(m1, m2)
    
    # ALORS l'équipe est toujours en vie (car M1 est là)
    assert equipe.isAlive() is True
    
def test_duel_victoire_equipe_2_si_equipe_1_vide():
    # Equipe 1 morte, Equipe 2 vivante
    eq1 = Equipe(CharacterBuilder().avec_sante(0, 10).build(), CharacterBuilder().avec_sante(0, 10).build())
    eq2 = Equipe(CharacterBuilder().with_lvl(10).build(), CharacterBuilder().with_lvl(10).build())
    duel = Duel(eq1, eq2)
    
    # Le gagnant DOIT être l'équipe 2
    assert duel.fight() == 2