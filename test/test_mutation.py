import pytest
from unittest.mock import patch
from RPG.RPG import Character, Duel, Equipe
from test.utils.PersonnageBuilder import CharacterBuilder

def test_exact_boundary_damage_rounding():
    # ETANT DONNE un perso avec 50% d'armure (MaxHP = 12)
    p = CharacterBuilder().with_armor(50).with_lvl(1).build()
    
    # QUAND il prend 0.4 dégâts (réduit à 0.2)
    # ALORS les dégâts sont arrondis à 0
    p.take_damage(0.4)
    assert p.hp == 12

def test_minimum_damage_logic_low_damage():
    # ETANT DONNE un perso avec 20% d'armure
    p = CharacterBuilder().with_armor(20).with_lvl(1).build()
    
    # QUAND il subit 1 de dégât (1 * 0.8 = 0.8, arrondi à 1)
    p.take_damage(1)
    
    # ALORS il perd 1 PV
    assert p.hp == 11

def test_who_lowest_dead_character_exclusion():
    # ETANT DONNE une équipe avec un survivant (100% PV) et un mort (0% PV)
    p1 = CharacterBuilder().build()
    p2 = CharacterBuilder().build()
    p2.take_damage(100) # Mort
    eq = Equipe(p1, p2)
    
    # QUAND on cherche le plus faible
    # ALORS il doit ignorer le mort et renvoyer le vivant (p1)
    assert eq.whoLowest() == p1

def test_duel_reaches_limit():
    # ETANT DONNE deux équipes de "sacs de frappe" qui ne font pas de dégâts
    # (On simule un combat qui dure via un mock d'attaque inoffensive)
    p1 = CharacterBuilder().build()
    p2 = CharacterBuilder().build()
    eq1 = Equipe(p1, p1)
    eq2 = Equipe(p2, p2)
    duel = Duel(eq1, eq2)
    
    with patch.object(Character, 'attack'):
        # QUAND le combat dépasse 1000 tours
        result = duel.fight()
        # ALORS il s'arrête (pas de boucle infinie)
        assert result in [1, 2]
        
def test_who_lowest_equality_case():
    # ETANT DONNE deux persos avec le MEME ratio de PV
    p1 = CharacterBuilder().with_lvl(1).build()
    p2 = CharacterBuilder().with_lvl(1).build()
    eq = Equipe(p1, p2)
    
    # QUAND on cherche le plus faible
    # ALORS il doit en retourner un (souvent le premier par défaut dans la logique)
    assert eq.whoLowest() in [p1, p2]

def test_who_lowest_full_dead_team():
    # ETANT DONNE une équipe où tout le monde est mort
    p1 = CharacterBuilder().build()
    p2 = CharacterBuilder().build()
    p1.take_damage(100)
    p2.take_damage(100)
    eq = Equipe(p1, p2)
    
    # ALORS whoLowest doit retourner None (pour éviter de taper un cadavre)
    assert eq.whoLowest() is None
    
def test_get_order_agility_sorting():
    # ETANT DONNE des persos avec des agilités différentes
    p_lent = CharacterBuilder().with_agilite(1).build()
    p_moyen = CharacterBuilder().with_agilite(10).build()
    p_rapide = CharacterBuilder().with_agilite(50).build()
    p_god = CharacterBuilder().with_agilite(100).build()
    
    eq1 = Equipe(p_lent, p_rapide)
    eq2 = Equipe(p_moyen, p_god)
    duel = Duel(eq1, eq2)
    
    # QUAND on récupère l'ordre
    ordre = duel.getOrder()
    
    # ALORS l'ordre doit être strictement : p_god, p_rapide, p_moyen, p_lent
    assert ordre == [p_god, p_rapide, p_moyen, p_lent]
    
def test_weapon_multiplier_impact():
    # ETANT DONNE un attaquant avec une arme de force 2
    attaquant = CharacterBuilder().with_force(5).with_arme(2).build()
    victime = CharacterBuilder().with_armor(0).build()
    
    # QUAND il attaque (on mock le dé sur 5)
    with patch('random.randint', return_value=5):
        attaquant.attack(victime)
        
    # ALORS les dégâts subis doivent être 10 (5 * 2)
    assert victime.hp == victime.maxHp - 10