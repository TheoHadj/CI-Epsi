from src.RPG.Character import Character


class CharacterBuilder:

    @staticmethod
    def stub():
        return CharacterBuilder().build()

    @staticmethod
    def sac_de_frappe():
        return CharacterBuilder().with_endurance(1000).with_lvl(1000).build()

    def __init__(self):
        self._force = 0
        self._endurance = 0
        self._agilite = 0
        self._chance = 0
        self._armor = 0
        self._arme = 1
        self._lvl = 0

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
        c = Character(
            armor=self._armor,
            arme_multiplicator=self._arme
        )

        c.force = self._force
        c.endurance = self._endurance
        c.agilite = self._agilite
        c.chance = self._chance
        c.lvl = self._lvl
        c.hp = c.baseHp + c.endurance

        return c