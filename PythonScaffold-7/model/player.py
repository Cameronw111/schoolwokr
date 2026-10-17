from model.player_hand import PlayerHand
from model.exception.battle_exception import BattleException
from model.exception.full_hand_exception import FullHandException

class Player:
    def __init__(self, battle_hand, discard_pile):
        self.__hand = PlayerHand()
        self.__battle_hand = battle_hand
        self.__discard_pile = discard_pile
    
    def get_hand(self):
        return self.__hand
    
    def place(self, card):
        self.__hand.place(card)
        
    def battle(self, card):
        if not self.__battle_hand.can_place(card):
            raise BattleException("Slot taken")
        if self.__hand.is_full():
            raise FullHandException("Your hand is full")
        self.__hand.draw(card)
        self.__battle_hand.place(card)
        
    def discard(self, card):
        self.__hand.draw(card)
        self.__discard_pile.add(card)
        
    def weaken(self, amount):
        if not self.__hand.is_protected():
            self.__hand.weaken(amount)
