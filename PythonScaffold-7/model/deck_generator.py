from model.attack_type import AttackType
from model.card import Card

class DeckGenerator:
    
    CARDS = [
        Card("Firestorm", 24, AttackType.HEAT),
        Card("Blindside", 30, AttackType.ENERGY),
        Card("Freeze Fire", 40, AttackType.ICE),
        Card("Blazing Fury", 80, AttackType.FURY),
        Card("Firestorm", 24, AttackType.HEAT),
        Card("Shield of Steel", 24, AttackType.PROTECTOR),
        Card("Icicle", 10, AttackType.ICE),
        Card("Iceberg", 15, AttackType.ICE),
        Card("Showdown", 60, AttackType.FURY),
        Card("Blindside", 30, AttackType.ENERGY),
        Card("Icicle", 10, AttackType.ICE),
        Card("Firestorm", 24, AttackType.HEAT),
        Card("Shutdown", 100, AttackType.FURY),
        Card("Blazing Fury", 80, AttackType.FURY),
        Card("Blindside", 30, AttackType.ENERGY),
        Card("Icicle", 10, AttackType.ICE),
        Card("Cloak of Darkness", 24, AttackType.PROTECTOR),
        Card("Firestorm", 24, AttackType.HEAT),
        Card("Shutdown", 100, AttackType.FURY),
        Card("Blazing Fury", 80, AttackType.FURY),
        Card("Blindside", 30, AttackType.ENERGY),
        Card("Icicle", 10, AttackType.ICE)
    ]

    @classmethod
    def generate(cls, amount):
        return [card.copy() for card in cls.CARDS[:amount]]
