from unittest.mock import MagicMock
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
        # Options pour les Mocks
        self._is_mock = False
        self._mock_danger = False
        self._mock_hp = 10
        self._mock_max_hp = 10

    def as_mock(self):
        self._is_mock = True
        return self

    def en_danger(self, state: bool):
        self._mock_danger = state
        return self

    def avec_sante(self, hp, max_hp):
        self._mock_hp = hp
        self._mock_max_hp = max_hp
        return self

    def with_force(self, v): self._force = v; return self
    def with_endurance(self, v): self._endurance = v; return self
    def with_agilite(self, v): self._agilite = v; return self
    def with_armor(self, v): self._armor = v; return self
    def with_arme(self, v): self._arme = v; return self
    def with_lvl(self, v): self._lvl = v; return self

    def build(self):
        if self._is_mock:
            mock = MagicMock(spec=Character)
            mock.hp = self._mock_hp
            mock.maxHp = self._mock_max_hp
            mock.is_alive.return_value = self._mock_hp > 0
            mock.est_en_danger.return_value = self._mock_danger
            return mock
        
        return Character(
            level=self._lvl, end=self._endurance, force=self._force,
            agi=self._agilite, chn=self._chance, armor=self._armor, arme=self._arme
        )