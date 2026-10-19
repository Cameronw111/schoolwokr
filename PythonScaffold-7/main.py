import os
from tkinter import *
from model.game import Game
from view.game_view import GameView
from view.player_view import PlayerView

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    root = Tk()
    game = Game()
    GameView(root, game)
    for i, player in enumerate(game.get_players()):
        PlayerView(Toplevel(root), player, f"Player {i + 1}")
    root.mainloop()