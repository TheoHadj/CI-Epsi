from RPG.RPG import Character

class CharacterBuilder:
    def __init__(self):
        self._force = 0
        self._endurance = 0
        self._agilite = 0
        self._chance = 0
        self._armor = 0
        self._arme = 1
        self._lvl = 1

    def with_force(self, v):
        self._force = v
        return self

    def with_endurance(self, v):
        self._endurance = v
        return self

    def with_agilite(self, v):
        self._agilite = v
        return self

    def with_chance(self, v):
        self._chance = v
        return self

    def with_armor(self, v):
        self._armor = v
        return self

    def with_arme(self, v):
        self._arme = v
        return self

    def with_lvl(self, v):
        self._lvl = v
        return self

    def build(self):
        return Character(
            level=self._lvl,
            end=self._endurance,
            force=self._force,
            agi=self._agilite,
            chn=self._chance,
            armor=self._armor,
            arme=self._arme
        )