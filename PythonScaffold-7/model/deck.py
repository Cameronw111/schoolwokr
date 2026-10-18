from model.deck_generator import DeckGenerator
from model.observable import Observable
import random

class Deck(Observable):
    
    def __init__(self, amount):
        super().__init__()
        self.__cards = DeckGenerator.generate(amount)
    
    def get_cards(self):
        return self.__cards
    
    def add(self, card):
        self.__cards.append(card)
        self.notify()
        
    def draw(self):
        card = self.__cards.pop(0)
        self.notify()
        return card
    
    def is_empty(self):
        return len(self.__cards) == 0
    
    def has_enough(self, amount):
        return len(self.__cards) >= amount
    
    def merge(self, deck):
        for card in deck.__cards:
            self.__cards.append(card)
        self.shuffle()
        deck.clear()
    
    def clear(self):
        self.__cards.clear()
        self.notify()
    
    def shuffle(self):
        random.shuffle(self.__cards)
        self.notify()