from model.hand import Hand

class PlayerHand(Hand):
    MAX_SIZE = 4
    def __init__(self):
        super().__init__()
        self.__cards = []
        
    def get_cards(self):
        return self.__cards
    
    def is_full(self):
        return len(self.__cards) >= PlayerHand.MAX_SIZE
    
    def is_protected(self):
        for card in self.__cards:
            if card.is_protector():
                return True
        return False
    
    def weaken(self, amount):
        for card in self.__cards:
            card.weaken(amount)
            
    def place(self, card):
        self.__cards.append(card)
        
    def draw(self, card):
        self.__cards.remove(card)
