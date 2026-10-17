from model.attack_type import AttackType

class Card:
    def __init__(self, name, strength, type):
        self.__name = name
        self.__strength = strength
        self.__type = type
    
    def get_name(self):
        return self.__name
    
    def get_strength(self):
        return self.__strength
    
    def get_type(self):
        return self.__type
    
    def weaken(self, amount):
        self.__strength -= amount
        if self.__strength < 0:
            self.__strength = 0
    
    def is_protector(self):
        return self.__type == AttackType.PROTECTOR
    
    def __str__(self):
        return f"{self.__name} ({self.__strength})"
    
    #Do not remove this. You do not need to use this in your implementation.
    def copy(self):
        return Card(self.__name, self.__strength, self.__type)
