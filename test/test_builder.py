from test.Builder import CharacterBuilder


def test_builder():
    p = CharacterBuilder().with_force(10).with_agilite(5).build()

    assert p.force == 10
    assert p.agilite == 5
    
    p2 = CharacterBuilder().with_force(10).with_agilite(5).with_armor(8).with_chance(3).with_endurance(4).build()
    assert p2.force == 10
    assert p2.agilite == 5
    assert p2.armor == 8
    assert p2.chance == 3
    assert p2.endurance == 4

