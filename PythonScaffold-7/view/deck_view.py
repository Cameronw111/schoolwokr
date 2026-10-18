from tkinter import *
from model.deck import Deck
from view.card_view import CardView
from view.styles import Style

class DeckView:
    def __init__(self, parent, deck: Deck, name):
        self.parent = parent
        self.deck = deck
        self.parent.title(name)

        self.listbox = Listbox(self.parent, **Style.listbox)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.update_buttons)

        buttons = Frame(self.parent)
        buttons.pack(**Style.pack_stretch)
        self.view_button = Button(buttons, text="View", command=self.view, state=DISABLED, **Style.button)
        self.shuffle_button = Button(buttons, text="Shuffle", command=self.deck.shuffle, **Style.button)
        close_button = Button(buttons, text="Close", command=self.close, **Style.button)
        for column, button in enumerate([self.view_button, self.shuffle_button, close_button]):
            buttons.columnconfigure(column, weight=1)
            button.grid(row=0, column=column, **Style.grid_stretch)

        self.parent.protocol("WM_DELETE_WINDOW", self.close)
        self.deck.subscribe(self.refresh)
        self.refresh()

    def refresh(self):
        self.listbox.delete(0, END)
        for card in self.deck.get_cards():
            self.listbox.insert(END, str(card))
        self.update_buttons()

    def update_buttons(self, event=None):
        self.view_button.config(state=NORMAL if self.listbox.curselection() else DISABLED)
        self.shuffle_button.config(state=DISABLED if self.deck.is_empty() else NORMAL)

    def view(self):
        card = self.deck.get_cards()[self.listbox.curselection()[0]]
        CardView(Toplevel(self.parent), card)

    def close(self):
        self.deck.unsubscribe(self.refresh)
        self.parent.destroy()