from tkinter import *
from tk_utils import TkUtils
from view.styles import Style

class ErrorView:
    def __init__(self, parent, error):
        self.parent = parent
        self.parent.title("Error")

        TkUtils.Image(self.parent, "view/image/error.png", 100, 100).pack(**Style.padding_small)
        Label(self.parent, text=type(error).__name__, **Style.error).pack(**Style.padding_small)
        Label(self.parent, text=str(error), font=("Arial", 12)).pack(**Style.padding_small)
        Button(self.parent, text="Close", command=self.parent.destroy, **Style.button).pack(**Style.pack_stretch)