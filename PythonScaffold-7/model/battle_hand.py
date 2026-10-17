from model.hand import Hand

class BattleHand(Hand):
    def __init__(self):
        super().__init__()
        self.__cards = []
        self.__strength = 0
        for i in range(5):
            self.__cards.append(None)
    
    def get_cards(self):
        return self.__cards
    
    def get_strength(self):
        return self.__strength
    
    def is_full(self):
        for card in self.__cards:
            if card is None:
                return False
        return True
    
    def place(self, card):
        self.__cards[card.get_type().slot()] = card
        self.set_strength()
    
    def can_place(self, card):
        return self.__cards[card.get_type().slot()] == None
    
    def set_strength(self):
        total = 0
        for card in self.__cards:
            if card == None:
                continue
            total += card.get_strength()
        self.__strength = total
