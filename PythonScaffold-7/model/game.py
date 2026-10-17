from model.deck import Deck
from model.battle_hand import BattleHand
from model.player import Player
from model.exception.empty_deck_exception import EmptyDeckException

class Game:
    def __init__(self):
        self.__main_deck = Deck(20)
        self.__special_deck = Deck(8)
        self.__discard_pile = Deck(0)
        self.__battle_hand = BattleHand()
        
        self.__players = [Player(self.__battle_hand, self.__discard_pile), Player(self.__battle_hand, self.__discard_pile), Player(self.__battle_hand, self.__discard_pile)]
        
        self.__turn_counter = 0
    
    def get_main_deck(self):
        return self.__main_deck
    
    def get_special_deck(self):
        return self.__special_deck
    
    def get_discard_pile(self):
        return self.__discard_pile
    
    def get_players(self):
        return self.__players
    
    def get_battle_hand(self):
        return self.__battle_hand
    
    def weaken(self, amount):
        for player in self.__players:
            player.weaken(amount)
            
    def deal(self):
        if not self.can_play():
            raise EmptyDeckException("Not enough cards in the deck")
        for player in self.__players:
            self.__turn_counter += 1
            card = self.pick_card()
            player.place(card)
        
    def restore(self):
        if self.__discard_pile.is_empty():
            raise EmptyDeckException("Discard pile is empty")
        self.__main_deck.merge(self.__discard_pile)
        
    def can_play(self):
        return self.__main_deck.has_enough(3) and self.__special_deck.has_enough(1)
    
    def pick_card(self):
        if self.__turn_counter % 4 == 0:
            return self.__special_deck.draw()
        return self.__main_deck.draw()
