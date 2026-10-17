from tkinter import *
from model.game import Game
from view.game_view import GameView

if __name__ == "__main__":
    root = Tk()
    game = Game()
    GameView(root, game)
    root.mainloop()
