from tkinter import *
from tkinter import ttk
from PIL import Image as PILImage
from tk_utils import TkUtils
from view.styles import Style

class ErrorView:
    def __init__(self, parent, error):
        self.parent = parent
        self.parent.title("Error")

        path = "view/image/error.png"
        width, height = PILImage.open(path).size
        TkUtils.Image(self.parent, path, int(width * 240 / height), 240).pack(padx=(80, 80), pady=(20, 20))
        ttk.Separator(self.parent).pack(**Style.pack_stretch)
        Label(self.parent, text=type(error).__name__, **Style.error).pack(**Style.padding_small)
        ttk.Separator(self.parent).pack(**Style.pack_stretch)
        Label(self.parent, text=str(error), font=("Arial", 12)).pack(**Style.padding_small)
        Button(self.parent, text="Close", command=self.parent.destroy, **Style.button).pack(**Style.pack_stretch)