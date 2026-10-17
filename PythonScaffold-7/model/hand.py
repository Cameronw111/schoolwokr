from abc import ABC, abstractmethod
from model.observable import Observable 

class Hand(ABC, Observable):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def place(self, card):
        pass
    
    @abstractmethod
    def is_full(self):
        pass
