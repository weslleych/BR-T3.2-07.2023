import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import hammer
from dino_runner.components.power_ups.umbrella import umbrella

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 400
    
    def generate_power_up(self, current_score):
        if len(self.power_ups) == 0 and self.when_appears == current_score:
            self.sorteador = random.randint(0,2)
            self.when_appears += random.randint(400,500)
            if self.sorteador == 0:
                self.power_ups.append(Shield())
            elif self.sorteador== 1:
                self.power_ups.append(hammer())
            elif self.sorteador == 2:
                self.power_ups.append(umbrella())
            
    def update(self, game):
        self.generate_power_up(game.current_score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            player = game.player
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                if self.sorteador == 0:
                    player.shield = True
                    player.has_power_up = True
                elif self.sorteador == 1:
                    player.hammer = True
                    player.has_hammer = True
                elif self.sorteador == 2:
                    player.umbrella = True
                    player.has_umbrella = True
                player.type = power_up.type #tipo de image que estaria utilizando
                player.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
                

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    