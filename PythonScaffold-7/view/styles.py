from tkinter import X, FLAT, CENTER, EW

class Style:
    button = {
        "foreground": "white",
        "background": "#30c252",
        "activebackground": "#70ff88",
        "font": ("Arial", 11, "bold"),
        "relief": FLAT
    }
    padding_small = {
        "padx" : (10, 10),
        "pady" : (10, 10)
    }
    padding_medium = {
        "padx" : (20, 20),
        "pady" : (20, 20)
    }
    padding_large = {
        "padx" : (50, 50),
        "pady" : (50, 50)
    }
    pack_stretch = {
        "expand" : True,
        "fill" : X
    }
    spacing = {
        "padx": (12, 12)
    }
    listbox = {
        "justify": CENTER,
        "width": 36,
        "height": 15,
        "font": ("Arial", 12),
        "foreground": "#333"
    }
    error = {
        "foreground": "red",
        "font": ("Monospace", 14, "bold")
    }
    grid_stretch = {
        "sticky": EW
    }
