from tkinter import *
from tkinter import ttk
from model.attack_type import AttackType
from model.game import Game
from view.styles import Style
from view.deck_view import DeckView
from tk_utils import TkUtils
class GameView:
    def __init__(self, parent, card):
        self.parent = parent
        self.card = card
        self.parent.title(card.get_name())

        path = f"images/cards/{card.get_name().lower().replace(' ', '')}.png"
        TkUtils.Image(self.parent, path, 300, 420).pack(**Style.padding_small)
        Button(self.parent, text="Close", command=self.parent.destroy, **Style.button).pack(**Style.pack_stretch)
        
        Label(self.parent, text="Battle Hand", font=("Arial", 18, "bold")).pack(**Style.padding_medium)
        ttk.Separator(self.parent).pack(**Style.pack_stretch)

        decks = Frame(self.parent)
        decks.pack(**Style.padding_large)
        self.add_deck(decks, 0, "Main Deck", self.model.get_main_deck())
        self.add_deck(decks, 1, "Special Deck", self.model.get_special_deck())
        self.add_deck(decks, 2, "Discard Pile", self.model.get_discard_pile())

        ttk.Separator(self.parent).pack(**Style.pack_stretch)

        entry_frame = Frame(self.parent)
        entry_frame.pack(**Style.padding_small)
        Label(entry_frame, text="Weaken:").grid(row=0, column=0, **Style.spacing)
        self.amount = StringVar()
        self.amount.trace_add("write", self.update_weaken)
        Entry(entry_frame, textvariable=self.amount).grid(row=0, column=1)

        buttons = Frame(self.parent)
        buttons.pack(**Style.pack_stretch)
        self.weaken_button = Button(buttons, text="Weaken", command=self.weaken, state=DISABLED, **Style.button)
        items = [
            Button(buttons, text="Deal", command=self.deal, **Style.button),
            Button(buttons, text="Restore", command=self.restore, **Style.button),
            Button(buttons, text="Battle Hand", command=self.open_battle_hand, **Style.button),
            self.weaken_button,
            Button(buttons, text="Exit", command=self.parent.destroy, **Style.button)
        ]
        for column, button in enumerate(items):
            buttons.columnconfigure(column, weight=1)
            button.grid(row=0, column=column, **Style.grid_stretch)

    def add_deck(self, parent, column, name, deck):
        image = TkUtils.Image(parent, "images/deck.png", 100, 150)
        image.grid(row=0, column=column, **Style.spacing)
        image.bind("<Button-1>", lambda event: self.open_deck(deck, name))

    def open_deck(self, deck, name):
        DeckView(Toplevel(self.parent), deck, name)

    def open_battle_hand(self):
        pass

    def deal(self):
        try:
            self.model.deal()
        except EmptyDeckException as e:
            self.show_error(e)

    def restore(self):
        try:
            self.model.restore()
        except EmptyDeckException as e:
            self.show_error(e)

    def weaken(self):
        try:
            self.model.weaken(int(self.amount.get()))
        except ValueError as e:
            self.show_error(e)

    def update_weaken(self, *args):
        self.weaken_button.config(state=NORMAL if self.amount.get() else DISABLED)

    def show_error(self, e):
        error_window = Toplevel(self.parent)
        error_window.title("Error")
        Label(error_window, text=type(e).__name__, **Style.error).pack(**Style.padding_small)
        Label(error_window, text=str(e), font=("Arial", 12)).pack(**Style.padding_small)
        Button(error_window, text="Close", command=error_window.destroy, **Style.button).pack(**Style.padding_small)