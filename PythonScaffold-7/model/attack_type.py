from enum import Enum

class AttackType(Enum):
    ENERGY = 0
    HEAT = 1
    ICE = 2
    FURY = 3
    PROTECTOR = 4

    def slot(self):
        return self.value

    @staticmethod
    def name_from_slot(slot):
        for attack_type in AttackType:
            if attack_type.slot() == slot:
                return attack_type.name

        raise ValueError("Invalid slot")
