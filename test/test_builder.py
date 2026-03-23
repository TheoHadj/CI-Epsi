
from test.Builder import CharacterBuilder


def test_builder():
    p = CharacterBuilder().with_force(10).with_agilite(5).build()

    assert p.force == 0
    assert p.agilite == 5