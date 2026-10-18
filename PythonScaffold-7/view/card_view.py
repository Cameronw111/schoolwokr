from tkinter import *
from tk_utils import TkUtils
from view.styles import Style

class CardView:
    def __init__(self, parent, card):
        self.parent = parent
        self.parent.title(card.get_name())

        path = f"view/image/cards/{card.get_name().lower().replace(' ', '')}.png"
        TkUtils.Image(self.parent, path, 300, 420).pack(**Style.padding_small)
        Button(self.parent, text="Close", command=self.parent.destroy, **Style.button).pack(**Style.pack_stretch)