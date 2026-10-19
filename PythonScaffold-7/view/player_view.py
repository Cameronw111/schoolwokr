from tkinter import *
from tkinter import ttk
from model.player import Player
from model.exception.battle_exception import BattleException
from model.exception.full_hand_exception import FullHandException
from view.error_view import ErrorView
from view.styles import Style

class PlayerView:
    def __init__(self, parent, player: Player, name):
        self.parent = parent
        self.player = player
        self.hand = player.get_hand()
        self.parent.title(name)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"), background="#d9d9d9", foreground="black", relief=RAISED, borderwidth=1, bordercolor="#a8a8a8")
        style.map("Treeview.Heading", background=[("active", "#d9d9d9")])

        self.table = ttk.Treeview(self.parent, columns=("name", "type", "strength"), show="headings", height=5)
        self.table.heading("name", text="Name")
        self.table.heading("type", text="Type")
        self.table.heading("strength", text="Strength")
        self.table.column("name", anchor=CENTER)
        self.table.column("type", anchor=CENTER)
        self.table.column("strength", anchor=CENTER)
        self.table.tag_configure("grey", background="#f0f0f0")
        self.table.pack(**Style.pack_stretch)
        self.table.bind("<<TreeviewSelect>>", self.update_buttons)

        self.empty_label = Label(self.table, text="Hand empty", background="white")

        buttons = Frame(self.parent)
        buttons.pack(**Style.pack_stretch)
        buttons.columnconfigure(0, weight=1)
        buttons.columnconfigure(1, weight=1)

        self.discard_button = Button(buttons, text="Discard", command=self.discard, state=DISABLED, **Style.button)
        self.discard_button.grid(row=0, column=0, **Style.grid_stretch)
        self.place_button = Button(buttons, text="Place in Battle Hand", command=self.place, state=DISABLED, **Style.button)
        self.place_button.grid(row=0, column=1, **Style.grid_stretch)

        self.parent.protocol("WM_DELETE_WINDOW", self.close)
        self.hand.subscribe(self.refresh)
        self.refresh()

    def refresh(self):
        for row in self.table.get_children():
            self.table.delete(row)

        cards = self.hand.get_cards()
        for i in range(len(cards)):
            card = cards[i]
            values = (card.get_name(), card.get_type().name, card.get_strength())
            if i % 2 == 1:
                self.table.insert("", END, iid=str(i), values=values, tags=("grey",))
            else:
                self.table.insert("", END, iid=str(i), values=values)

        if len(cards) == 0:
            self.empty_label.place(relx=0.5, rely=0.6, anchor=CENTER)
        else:
            self.empty_label.place_forget()

        self.update_buttons()

    def update_buttons(self, event=None):
        if self.table.selection():
            self.discard_button.config(state=NORMAL)
            self.place_button.config(state=NORMAL)
        else:
            self.discard_button.config(state=DISABLED)
            self.place_button.config(state=DISABLED)

    def selected_card(self):
        index = int(self.table.selection()[0])
        return self.hand.get_cards()[index]

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