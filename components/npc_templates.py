from __future__ import annotations

from engine import Engine
from entity import Entity, Actor

from components.bodyparts import Bodypart

class BaseComponent:
    entity: Entity  # Owning entity instance.

    @property
    def engine(self) -> Engine:
        return self.entity.gamemap.engine


class Fighter(BaseComponent):
    # basic class for entities that fight
    def __init__(self,
                 power: int = 0,
                 volume_blood: int = 100,
                 energy: int = 100,
                 move_cost:int = 100,
                 attack_cost:int = 100,
                 bleeds: bool = True,
                 ):

        self.power = power
        self.max_volume_blood = volume_blood
        self.volume_blood = volume_blood
        self.max_energy = energy
        self.energy = energy
        self.move_cost = move_cost
        self.attack_cost = attack_cost
        self.bleeds = bleeds
