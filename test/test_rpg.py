from src.RPG import Character

def test_player_initialization():
    #ETANT DONNE UN PERSONNAGE
    p = Character()

    #doit avec hp==10
    assert p.hp == 10 + p.endurance

def test_attack_reduces_hp():
    # ETANT DONNE deux personnages un monstre et un hero avec 10 PV
    hero = Character()
    monster = Character()
    hp0 = monster.hp

    #QUAND LE HERO ATTAQUE LE MONSTRE
    hero.attack(monster)

    #LE MONSTRE doit perdre 1 hp
    assert hp0 - monster.hp == 1

def test_player_death():
    #ETANT DONNE UN PERSONNAGE
    monster = Character()

    #QUAND IL PREND DES ASSEZ DE COUPS
    while(monster.hp>0) :
        monster.take_damage(1)
    
    #IL DOIT avoir 0 hp et ne plus être en vie
    assert monster.hp == 0
    assert monster.is_alive() is False

def test_player_kill():
    #ETANT DONNE DEUX PERSONNAGES monstre et hero
    hero = Character()
    monster = Character()

    #QUAND MONSTRE TAPE HERO 10 FOIS
    while(hero.hp>0) :
        monster.attack(hero)
    
    #Hero doit mourir et avoir 0 hp
    assert hero.hp == 0
    assert hero.is_alive() is False

def test_player_over_damage():
    #ETANT DONNE DEUX PERSONNAGES monstre et hero
    hero = Character()
    monster = Character()

    #QUAND MONSTRE TAPE ASSEZ LE HERO POUR QU'IL MEURT, PUIS TAPE DEUX FOIS DE PLUS 
    while(hero.hp>0):
        monster.attack(hero)
    
    for i in range (2):
        monster.attack(hero)
        
    #Hero doit mourir et ne pas perdre plus d'hp que 0
    assert hero.hp == 0
    assert hero.is_alive() is False
 
def test_dead_player_cant_attack():
    #ETANT DONNE DEUX PERSONNAGES monstre et hero 
    hero = Character()
    heroHp0=hero.hp
    monster = Character()

    #QUAND MONSTRE EST MORT ET QU'IL ATTAQUE
    while(monster.hp>0):
        hero.attack(monster)

    #ALORS MONSTRE NE FAIT PAS DE DEGAT A HERO.
    assert hero.hp==heroHp0

def test_valid_take_damage_argument():
    # Etant donné un personnage
    hero = Character()
    hero_base_hp = hero.hp
    
    # Lorsqu'un personnage subit des dégats, et que la valeur des dégats subits n'est pas un nombre supérieur à 0
    hero.take_damage(-1)
    
    # Alors le monstre ne doit pas perdre points de vie
    assert hero.hp == hero_base_hp

    hero.take_damage("1")
    assert hero.hp == hero_base_hp
    
    hero.take_damage(hero)
    assert hero.hp == hero_base_hp

def test_has_endu():
    #Etant donné un personnage
    hero = Character()
    
    #Quand il vient d'être créé

    #Alors il a 1 d'endurance
    assert hero.endurance == 1

def test_end_impact_hp():
    #Etant donné un personnage
    hero = Character()

    #Alors ces hp sont égaux à baseHp + son endurance
    assert hero.hp == hero.baseHp + hero.endurance 
    
def test_caracteristique_force():
    # Étant donné un personnage
    perso = Character()
    ennemi = Character()

    perso_force = perso.force
    perso_base_hp = perso.hp
    
    # Il possède une caractéristique Force qui augmente ses dégats
    assert perso_force >= 0
    
    # Ses dégats sont augmentés en fonction de sa force (1 + force)
    ennemi.attack(perso)
    assert perso.hp < perso_base_hp
