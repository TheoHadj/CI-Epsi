from RPG import Character, Equipe, Duel

def test_demo_arme():
    # étant donné un personnage
    perso_arme = Character()
    
    # Lorsqu'on lui ajoute une arme
    perso_arme.ajouter_arme(1.2)
    
    # Alors il est bien armé 
    assert perso_arme.arme_multiplicator == 1.2
    
    
def test_demo_armure():
    # étant donné un personnage
    perso_armor = Character()
    
    # Lorsqu'on lui ajoute une armure
    perso_armor.ajouter_armure(2)
    
    # Alors il est bien armé 
    assert perso_armor.armor == 2
    
    
def test_demo_armure_attaque():
    # Étant donné un personnage avec une armure
    perso_armor = Character(2)
    perso_2 = Character()
    
    # Lorsqu'il se fait attaquer
    perso_2.attack(perso_armor)
    
    # Alors il perds moins de vie qu'un personnage non armé 
    assert perso_armor.hp <= 10 and perso_armor.hp >= 7
    
    
def test_demo_arme_attaque_hausse():
    # Étant donné un personnage ayant une arme et un perso_2
    perso_arme = Character(1, 1.2)
    perso_sans_arme = Character()
    perso_2 = Character()
    ennemi2 = Character()

    # Lorsque le personnage armé attaque l'perso_2
    perso_arme.attack(perso_2)
    perso_sans_arme.attack(ennemi2)
    
    # Alors l'perso_2 subit plus de dégâts que lors d'une attaque sans arme
    assert perso_2.hp <= 10 and perso_2.hp >= 4
    assert ennemi2.hp <= 10 and ennemi2.hp >= 5

    
def test_demo_arme_attaque_baisse():
    # Étant donné un personnage ayant une arme et un perso_2
    perso_arme = Character(0, 0.5)
    perso_sans_arme = Character()
    perso_2 = Character()
    ennemi2 = Character()
        
    # Lorsque le personnage armé attaque l'perso_2
    perso_arme.attack(perso_2)
    perso_sans_arme.attack(ennemi2)

    # Alors l'perso_2 subit moins de dégâts que lors d'une attaque sans arme
    assert perso_2.hp <= 10 and perso_2.hp >= 2.5
    assert ennemi2.hp <= 10 and ennemi2.hp >= 5


def test_deux_persos_armures():
    #Etant donné trois personnages, perso1 possédant une armure de 50, un perso1 sans et perso 
    perso1 = Character(50)
    h0=perso1.hp

    perso2 = Character(0)
    h02=perso2.hp

    perso = Character()

    #Quand heros reçoit une attaque de perso qui a 0 de force et qui fera entre 0 et 1 de dégats
    perso.attack(perso1)
    perso.attack(perso2)

    #La vie du perso1 ne doit pas changer.

    assert perso1.hp == h0 
    # assert perso1.hp != perso2.hp
    
    
    def test_demo_equipes():
        # Étant donné quatre personnage
        eq1_p1 = Character(1.5)
        eq1_p2 = Character(0.9)
        eq2_p1 = Character(1.1)
        eq2_p2 = Character(1.2)
        
        # Lorsque l'on créé deux équipes
        equipe_1 = Equipe(eq1_p1, eq1_p2)
        equipe_2 = Equipe(eq2_p1, eq2_p2)
        
        # Alors chaque équipe est composé de deux personnages
        assert equipe_1.perso_1.hp > 0
        assert equipe_1.perso_2.hp > 0
        
        assert equipe_2.perso_1.hp > 0
        assert equipe_2.perso_2.hp > 0
        
        
    def test_demo_duel_equipe():
        # Étant deux équipes
        eq1_p1 = Character(1.5)
        eq1_p2 = Character(0.9)
        eq2_p1 = Character(1.1)
        eq2_p2 = Character(1.2)
        equipe_1 = Equipe(eq1_p1, eq1_p2)
        equipe_2 = Equipe(eq2_p1, eq2_p2)
        
        # Lorsque l'on créé un duel
        duel = Duel(equipe_1, equipe_2)
        
        # Alors le duel est bien composé de deux équipe de deux joueurs chacune
        assert duel.hp_equipe(equipe_1) == 20
        assert duel.hp_equipe(equipe_2) == 20
        
        
    def test_demo_duel_attaque():
        # Étant un duel
        eq1_p1 = Character(2, 1.5)
        eq1_p2 = Character(0, 0.9)
        eq2_p1 = Character(0, 1.1)
        eq2_p2 = Character(1, 1.2)
        equipe_1 = Equipe(eq1_p1, eq1_p2)
        equipe_2 = Equipe(eq2_p1, eq2_p2)
        duel = Duel(equipe_1, equipe_2)
        
        # Lorsque l'équipe 1 attaque l'équipe 2
        duel.attaque_equipe(equipe_1, equipe_2.perso_2, equipe_2.perso_1)
        
        # Alors l'équipe 2 a subit des dégats et est toujours vivante
        assert duel.hp_equipe(equipe_2) <= 20 and duel.hp_equipe(equipe_2) >= 11
        assert not equipe_2.est_morte()
    
    
    def test_demo_duel_gagne():
        # Étant un duel
        eq1_p1 = Character(2, 1.5)
        eq1_p2 = Character(0, 0.9)
        eq2_p1 = Character(0, 1.1)
        eq2_p2 = Character(1, 1.2)
        equipe_1 = Equipe(eq1_p1, eq1_p2)
        equipe_2 = Equipe(eq2_p1, eq2_p2)
        duel = Duel(equipe_1, equipe_2)
        
        # Lorsqu'une équipe attaque l'autre plusieurs fois
        while not equipe_2.est_morte:   
            duel.attaque_equipe(equipe_1, equipe_2.perso_2, equipe_2.perso_1)
        
        # Alors l'équipe attaquante gagne le duel
        assert duel.who_wins() == 1
            
        
        
    
        
        
        
        
        
        

        

        
        

    

    
    
    
