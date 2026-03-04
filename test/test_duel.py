from src.RPG import Character, Equipe, Duel

def test_demo_duel_gagne():
    # Étant donné un duel
    eq1_p1 = Character(2, 1.5)
    eq1_p2 = Character(0, 0.9)
    eq2_p1 = Character(0, 1.1)
    eq2_p2 = Character(1, 1.2)
    equipe_1 = Equipe(eq1_p1, eq1_p2)
    equipe_2 = Equipe(eq2_p1, eq2_p2)
    duel = Duel(equipe_1, equipe_2)
    
    # Lorsque le duel est terminé
    winner = duel.startDuel()

    # Un gagnant est désigné et l'une des deux équipe à ses personanges décédés
    assert winner != False
    assert winner == 1 or winner == 2