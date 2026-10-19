from tkinter import *
from model.deck import Deck
from view.card_view import CardView
from view.styles import Style

class DeckView:
    def __init__(self, parent, deck: Deck, name):
        self.parent = parent
        self.deck = deck
        self.parent.title(name)

        list_frame = Frame(self.parent)
        list_frame.pack()
        self.listbox = Listbox(list_frame, **Style.listbox)
        self.listbox.pack(side=LEFT)
        self.scrollbar = Scrollbar(list_frame, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", self.update_buttons)

        self.empty_label = Label(self.listbox, text="Empty", font=("Arial", 12), foreground="#333", background="white")

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
        cards = self.deck.get_cards()
        for card in cards:
            self.listbox.insert(END, str(card))
        if cards:
            self.empty_label.place_forget()
        else:
            self.empty_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        if len(cards) > int(self.listbox.cget("height")):
            self.scrollbar.pack(side=RIGHT, fill=Y)
        else:
            self.scrollbar.pack_forget()
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