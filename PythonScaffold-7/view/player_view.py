from tkinter import *
from tkinter import ttk
from model.player import Player
from view.styles import Style
from model.exception.battle_exception import BattleException
from model.exception.full_hand_exception import FullHandException
from view.error_view import ErrorView
class PlayerView:
    def __init__(self, parent, player: Player, name):
        self.parent = parent
        self.player = player
        self.hand = player.get_hand()
        self.parent.title(name)

        columns = ("name", "type", "strength")
        self.table = ttk.Treeview(self.parent, columns=columns, show="headings", height=4)
        for column, heading in zip(columns, ("Name", "Type", "Strength")):
            self.table.heading(column, text=heading)
            self.table.column(column, anchor=CENTER)
        self.table.pack(**Style.pack_stretch)
        self.table.bind("<<TreeviewSelect>>", self.update_buttons)

        buttons = Frame(self.parent)
        buttons.pack(**Style.pack_stretch)
        self.discard_button = Button(buttons, text="Discard", command=self.discard, state=DISABLED, **Style.button)
        self.place_button = Button(buttons, text="Place in Battle Hand", command=self.place, state=DISABLED, **Style.button)
        for column, button in enumerate([self.discard_button, self.place_button]):
            buttons.columnconfigure(column, weight=1)
            button.grid(row=0, column=column, **Style.grid_stretch)

        self.parent.protocol("WM_DELETE_WINDOW", self.close)
        self.hand.subscribe(self.refresh)
        self.refresh()

    def refresh(self):
        self.table.delete(*self.table.get_children())
        for i, card in enumerate(self.hand.get_cards()):
            self.table.insert("", END, iid=str(i), values=(card.get_name(), card.get_type().name, card.get_strength()))
        self.update_buttons()

    def update_buttons(self, event=None):
        state = NORMAL if self.table.selection() else DISABLED
        self.discard_button.config(state=state)
        self.place_button.config(state=state)

    def selected_card(self):
        return self.hand.get_cards()[int(self.table.selection()[0])]

    def discard(self):
        self.player.discard(self.selected_card())

    def place(self):
        try:
            self.player.battle(self.selected_card())
        except (BattleException, FullHandException) as e:
            ErrorView(Toplevel(self.parent), e)

    def close(self):
        self.hand.unsubscribe(self.refresh)
        self.parent.destroy()