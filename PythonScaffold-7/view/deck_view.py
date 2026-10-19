from tkinter import *
from model.deck import Deck
from view.card_view import CardView
from view.styles import Style

class DeckView:
    def __init__(self, parent, deck: Deck, name):
        self.parent = parent
        self.deck = deck
        self.parent.title(name)

        frame = Frame(self.parent)
        frame.pack()
        self.listbox = Listbox(frame, **Style.listbox)
        self.listbox.pack(side=LEFT)
        self.scrollbar = Scrollbar(frame, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", self.update_buttons)

        self.empty_label = Label(self.listbox, text="Empty", background="white")

        buttons = Frame(self.parent)
        buttons.pack(**Style.pack_stretch)
        buttons.columnconfigure(0, weight=1)
        buttons.columnconfigure(1, weight=1)
        buttons.columnconfigure(2, weight=1)

        self.view_button = Button(buttons, text="View", command=self.view, state=DISABLED, **Style.button)
        self.view_button.grid(row=0, column=0, **Style.grid_stretch)
        self.shuffle_button = Button(buttons, text="Shuffle", command=self.deck.shuffle, **Style.button)
        self.shuffle_button.grid(row=0, column=1, **Style.grid_stretch)
        close_button = Button(buttons, text="Close", command=self.close, **Style.button)
        close_button.grid(row=0, column=2, **Style.grid_stretch)

        self.parent.protocol("WM_DELETE_WINDOW", self.close)
        self.deck.subscribe(self.refresh)
        self.refresh()

    def refresh(self):
        self.listbox.delete(0, END)
        cards = self.deck.get_cards()
        for i in range(len(cards)):
            self.listbox.insert(END, str(cards[i]))
            if i % 2 == 1:
                self.listbox.itemconfig(i, background="#f0f0f0")

        if self.deck.is_empty():
            self.empty_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            self.empty_label.place_forget()

        if len(cards) > 15:
            self.scrollbar.pack(side=RIGHT, fill=Y)
        else:
            self.scrollbar.pack_forget()

        self.update_buttons()

    def update_buttons(self, event=None):
        if self.listbox.curselection():
            self.view_button.config(state=NORMAL)
        else:
            self.view_button.config(state=DISABLED)

        if self.deck.is_empty():
            self.shuffle_button.config(state=DISABLED)
        else:
            self.shuffle_button.config(state=NORMAL)

    def view(self):
        index = self.listbox.curselection()[0]
        card = self.deck.get_cards()[index]
        CardView(Toplevel(self.parent), card)

    def close(self):
        self.deck.unsubscribe(self.refresh)
        self.parent.destroy()