import pygame
from dino_runner.components.game import Game

class texto(Game):
    def add_texto_in_menu(self, game):
        if game.death_count == 0:
            self.text = game.font.render (f"Prees (S) to start playing", True,(0,0,0))
            self.align = (game.half_screen_width, game.half_screen_height)
        else:
            self.text = font.render (f"Prees (S) to start playing", True,(0,0,0)) 
            super().show_menu(self.text, self.align)   