from tkinter import *
from PIL import Image as PILImage
from tk_utils import TkUtils
from view.styles import Style

class CardView:
    def __init__(self, parent, card):
        self.parent = parent
        self.parent.title(card.get_name())

        path = f"view/image/cards/{card.get_name().lower().replace(' ', '')}.png"
        width, height = PILImage.open(path).size
        TkUtils.Image(self.parent, path, int(width * 400 / height), 400).pack()
        Button(self.parent, text="Close", command=self.parent.destroy, **Style.button).pack(**Style.pack_stretch)