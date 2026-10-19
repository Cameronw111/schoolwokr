from tkinter import *
from tkinter import ttk
from model.player import Player
from model.exception.battle_exception import BattleException
from model.exception.full_hand_exception import FullHandException
from view.error_view import ErrorView
from view.styles import Style

class PlayerView:
    ROWS = 5

    def __init__(self, parent, player: Player, name):
        self.parent = parent
        self.player = player
        self.hand = player.get_hand()
        self.parent.title(name)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Player.Treeview", rowheight=26, font=("Arial", 11), fieldbackground="white", borderwidth=0)
        style.configure("Player.Treeview.Heading", font=("Arial", 11, "bold"), background="#d0d0d0", foreground="black", relief=FLAT)
        style.map("Player.Treeview", background=[("selected", "#bdbdbd")], foreground=[("selected", "black")])
        style.map("Player.Treeview.Heading", background=[("active", "#c4c4c4")])

        columns = ("name", "type", "strength")
        self.table = ttk.Treeview(self.parent, columns=columns, show="headings", height=PlayerView.ROWS, style="Player.Treeview")
        for column, heading in zip(columns, ("Name", "Type", "Strength")):
            self.table.heading(column, text=heading)
            self.table.column(column, anchor=CENTER)
        self.table.tag_configure("even", background="white")
        self.table.tag_configure("odd", background="#f0f0f0")
        self.table.pack(**Style.pack_stretch)
        self.table.bind("<<TreeviewSelect>>", self.update_buttons)

        self.empty_label = Label(self.table, text="Hand empty", font=("Arial", 11), background="white")

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
        cards = self.hand.get_cards()
        if cards:
            self.empty_label.place_forget()
            for i in range(max(PlayerView.ROWS, len(cards))):
                tag = "odd" if i % 2 else "even"
                if i < len(cards):
                    card = cards[i]
                    self.table.insert("", END, iid=str(i), values=(card.get_name(), card.get_type().name, card.get_strength()), tags=(tag,))
                else:
                    self.table.insert("", END, iid=f"blank{i}", values=("", "", ""), tags=(tag,))
        else:
            self.empty_label.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.update_buttons()

    def update_buttons(self, event=None):
        selected = self.table.selection()
        state = NORMAL if selected and not selected[0].startswith("blank") else DISABLED
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