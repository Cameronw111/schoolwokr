import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class TkUtils:
    class Image(tk.Label):
        def __init__(self, parent, path, width, height, background=None):
            image_ = ImageTk.PhotoImage(Image.open(path).resize((width, height)))
            super().__init__(parent, image=image_, background=background)
            self.photo = image_
