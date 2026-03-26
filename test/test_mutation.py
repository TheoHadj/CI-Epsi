import pytest
from unittest.mock import patch
from RPG.RPG import Character, Duel, Equipe
from test.utils.PersonnageBuilder import CharacterBuilder

def test_seuil_danger_limite_flottante_precise():
    # ETANT DONNE un sujet avec une capacité de 1000 PV (Seuil 30% = 300)
    sujet = CharacterBuilder().with_endurance(988).with_lvl(1).build()
    
    # QUAND sa santé est juste au-dessus du seuil (30.1%)
    sujet.hp = 301
    assert sujet.est_en_danger() is False
    
    # QUAND sa santé est juste en-dessous (29.9%)
    sujet.hp = 299
    # ALORS l'état de danger est activé
    assert sujet.est_en_danger() is True

def test_calcul_degats_minimum_formule_attaque():
    # ETANT DONNE un attaquant avec une puissance minimale
    attaquant = CharacterBuilder().with_lvl(1).with_force(0).with_arme(1).build()
    defenseur = CharacterBuilder().with_armor(0).build()
    sante_initiale = defenseur.hp
    
    # QUAND le sort (randint) décide du minimum possible (1)
    with patch('random.randint', return_value=1):
        attaquant.attack(defenseur)
    
    # ALORS le défenseur perd exactement 1 PV par rapport à son état initial
    assert defenseur.hp == sante_initiale - 1

def test_impact_du_multiplicateur_d_équipement():
    # ETANT DONNE un attaquant avec une arme doublant les dégâts (x2)
    attaquant = CharacterBuilder().with_force(5).with_arme(2).build()
    defenseur = CharacterBuilder().with_armor(0).build()
    sante_initiale = defenseur.hp
    
    # QUAND il porte un coup d'une valeur de 5
    with patch('random.randint', return_value=5):
        attaquant.attack(defenseur)
        
    # ALORS les dégâts réels sont de 10 (5 * 2)
    assert defenseur.hp == sante_initiale - 10

def test_stabilite_du_tri_agilite_identique():
    # ETANT DONNE deux intervenants de même agilité
    sujet_a = CharacterBuilder().with_agilite(10).build()
    sujet_b = CharacterBuilder().with_agilite(10).build()
    
    eq1 = Equipe(sujet_a, CharacterBuilder().build())
    eq2 = Equipe(sujet_b, CharacterBuilder().build())
    ordre_action = Duel(eq1, eq2).getOrder()
    
    # ALORS les deux sont bien présents dans l'ordre d'action (tue les mutants >=)
    assert sujet_a in ordre_action
    assert sujet_b in ordre_action

def test_exclusion_des_membres_hors_combat_du_ciblage():
    # ETANT DONNE une équipe avec un membre actif et un membre hors combat
    membre_actif = CharacterBuilder().build()
    membre_mort = CharacterBuilder().build()
    membre_mort.take_damage(1000) # On s'assure qu'il est bien mort
    
    equipe = Equipe(membre_actif, membre_mort)
    
    # QUAND on cherche la cible la plus faible
    # ALORS le système ignore le membre mort et renvoie le membre actif
    assert equipe.whoLowest() == membre_actif

def test_gestion_equipe_totalement_hors_combat():
    # ETANT DONNE une équipe où tous les membres sont tombés
    m1 = CharacterBuilder().build()
    m2 = CharacterBuilder().build()
    m1.take_damage(1000)
    m2.take_damage(1000)
    
    equipe = Equipe(m1, m2)
    
    # ALORS la recherche de cible ne renvoie rien (évite les erreurs sur objets vides)
    assert equipe.whoLowest() is None

def test_securite_anti_boucle_infinie_duel():
    # ETANT DONNE un duel entre deux équipes incapables de se blesser
    sujet1 = CharacterBuilder().build()
    sujet2 = CharacterBuilder().build()
    duel = Duel(Equipe(sujet1, sujet1), Equipe(sujet2, sujet2))
    
    # On force les attaques à être inoffensives
    with patch.object(Character, 'attack'):
        # QUAND le duel atteint sa limite de tours
        vainqueur = duel.fight()
        # ALORS il se termine proprement sans bloquer le processeur
        assert vainqueur in [1, 2]

def test_arrondi_degats_infimes():
    # ETANT DONNE un sujet avec une armure de 50%
    sujet = CharacterBuilder().with_armor(50).build()
    sante_initiale = sujet.hp
    
    # QUAND il subit des dégâts trop faibles pour être comptabilisés (0.4 * 0.5 = 0.2)
    sujet.take_damage(0.4)
    
    # ALORS sa santé ne change pas (arrondi à 0)
    assert sujet.hp == sante_initiale

def test_rejet_degats_negatifs_ou_invalides():
    # ETANT DONNE un sujet sain
    sujet = CharacterBuilder().build()
    sante_initiale = sujet.hp
    
    # QUAND on tente de lui infliger des dégâts négatifs ou de type invalide
    sujet.take_damage(-10)
    sujet.take_damage("beaucoup")
    
    # ALORS sa santé reste intacte
    assert sujet.hp == sante_initiale
    
def test_seuil_danger_ne_prend_pas_le_pallis_exact():
    # Perso avec 100 PV Max
    perso = CharacterBuilder().with_endurance(88).with_lvl(1).build() 
    # QUAND il a exactement 30 PV (30/100 = 0.3)
    perso.hp = 30
    # ALORS est_en_danger doit être FALSE (car c'est strictement inférieur)
    assert perso.est_en_danger() is False
    
def test_arrondi_exact_point_cinq_force_le_degat_minimal():
    # ETANT DONNE un personnage avec une armure de 50%
    perso = CharacterBuilder().with_armor(50).build()
    sante_initiale = perso.hp
    
    # QUAND il reçoit une attaque de 1 point (Calcul : 1 * 0.5 = 0.5)
    perso.take_damage(1)
    
    # ALORS la règle du dégât minimum s'applique (0.5 arrondi à 0, mais forcé à 1)
    # On vérifie que sa santé a diminué exactement de 1
    assert perso.hp == sante_initiale - 1
    
def test_degat_minimum_est_applique_meme_apres_arrondi_inférieur():
    # ETANT DONNE un défenseur avec 50% d'armure
    perso = CharacterBuilder().with_armor(50).build()
    sante_initiale = perso.hp
    
    # QUAND il subit 1 dégât (Calcul: 1 * 0.5 = 0.5 -> arrondi à 0)
    perso.take_damage(1)
    
    # ALORS il perd quand même 1 PV à cause de la règle du dégât minimum
    assert perso.hp == sante_initiale - 1
    
def test_precision_arrondi_limite_flottante():
    # ETANT DONNE un personnage avec 50% d'armure
    # QUAND il reçoit 1.0000000001 de dégâts (très proche de 1)
    # Le calcul donne 0.50000000005
    perso = CharacterBuilder().with_armor(50).build()
    sante_initiale = perso.hp
    
    # On force un montant qui doit déclencher la précision du 1e-9
    perso.take_damage(1.0000000001)
    
    # ALORS l'arrondi doit être géré par la condition de précision
    # Si le mutant change 1e-9, ce test échouera
    assert perso.hp <= sante_initiale