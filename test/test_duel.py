from src.RPG import Character, Equipe, Duel


def test_demo_duel_gagne():
    # Étant donné un duel
    eq1_p1 = Character(armor=2, arme=1.5)
    eq1_p2 = Character(armor=0, arme=0.9)

    eq2_p1 = Character(armor=0, arme=1.1)
    eq2_p2 = Character(armor=1, arme=1.2)

    equipe_1 = Equipe(eq1_p1, eq1_p2)
    equipe_2 = Equipe(eq2_p1, eq2_p2)

    duel = Duel(equipe_1, equipe_2)

    # Lorsque le duel est terminé
    winner = duel.startDuel()

    # Alors il y'a un gagnant
    assert winner in (1, 2)

    # Et l'équipe perdante est bien morte
    if winner == 1:
        assert equipe_2.est_morte()
        assert not equipe_1.est_morte()
    else:
        assert equipe_1.est_morte()
        assert not equipe_2.est_morte()
        
        
def test_demo_duel_gagne_agi():
    # Étant donné un duel
    eq1_p1 = Character(armor=1, arme=1.1, agilite=100)
    eq1_p2 = Character(armor=1, arme=1.1, agilite=50)

    eq2_p1 = Character(armor=1, arme=1.1, agilite=1)
    eq2_p2 = Character(armor=1, arme=1.1, agilite=2)

    equipe_1 = Equipe(eq1_p1, eq1_p2)
    equipe_2 = Equipe(eq2_p1, eq2_p2)

    duel = Duel(equipe_1, equipe_2)

    # Lorsque le duel est terminé
    winner = duel.startDuel()

    # Alors il y'a un gagnant
    assert winner in (1, 2)

    # Et l'équipe perdante est bien morte
    if winner == 1:
        assert equipe_2.est_morte()
        assert not equipe_1.est_morte()
    else:
        assert equipe_1.est_morte()
        assert not equipe_2.est_morte()

def test_demo_duel_gagne_chn():
    # Étant donné un duel
    eq1_p1 = Character(armor=1, arme=1.1, chance=100)
    eq1_p2 = Character(armor=1, arme=1.1, chance=50)

    eq2_p1 = Character(armor=1, arme=1.1, chance=1)
    eq2_p2 = Character(armor=1, arme=1.1, chance=2)

    equipe_1 = Equipe(eq1_p1, eq1_p2)
    equipe_2 = Equipe(eq2_p1, eq2_p2)

    duel = Duel(equipe_1, equipe_2)

    # Lorsque le duel est terminé
    winner = duel.startDuel()

    # Alors il y'a un gagnant
    assert winner in (1, 2)

    # Et l'équipe perdante est bien morte
    if winner == 1:
        assert equipe_2.est_morte()
        assert not equipe_1.est_morte()
    else:
        assert equipe_1.est_morte()
        assert not equipe_2.est_morte()