from tkinter import *
from tkinter import ttk
from model.attack_type import AttackType
from model.battle_hand import BattleHand
from tk_utils import TkUtils
from view.styles import Style

class BattleView:
    def __init__(self, parent, battle_hand: BattleHand):
        self.parent = parent
        self.battle_hand = battle_hand
        self.parent.title("Battle Hand")

        Label(self.parent, text="Battle Hand", font=("Arial", 18, "bold")).pack(**Style.padding_medium)
        ttk.Separator(self.parent).pack(**Style.pack_stretch)

        self.strength_label = Label(self.parent, font=("Arial", 12, "bold"))
        self.strength_label.pack(**Style.padding_small)
        ttk.Separator(self.parent).pack(**Style.pack_stretch)

        slots = Frame(self.parent)
        slots.pack(**Style.padding_small)
        self.slot_labels = []
        for i in range(5):
            name = AttackType.name_from_slot(i).lower()
            TkUtils.Image(slots, f"view/image/logo/{name}.png", 70, 70).grid(row=i, column=0, padx=(10, 10), pady=(5, 5))
            label = Label(slots, font=("Arial", 12))
            label.grid(row=i, column=1, sticky=W)
            self.slot_labels.append(label)

        ttk.Separator(self.parent).pack(**Style.pack_stretch)
        Button(self.parent, text="Close", command=self.close, **Style.button).pack(**Style.pack_stretch)

        self.parent.protocol("WM_DELETE_WINDOW", self.close)
        self.battle_hand.subscribe(self.refresh)
        self.refresh()

    def refresh(self):
        for i, card in enumerate(self.battle_hand.get_cards()):
            self.slot_labels[i].config(text="Empty" if card is None else str(card))
        self.strength_label.config(text=f"Total Strength:  {self.battle_hand.get_strength()}")

    def close(self):
        self.battle_hand.unsubscribe(self.refresh)
        self.parent.destroy()