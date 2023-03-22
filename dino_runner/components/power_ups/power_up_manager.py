import random
import pygame

from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 600
    
    def generate_power_up(self, current_score):
        if len(self.power_ups) == 0 and self.when_appears == current_score:
            self.when_appears += random.randint(600,700)
            self.power_ups.append(Shield())
            
    def update(self, game):
        self.generate_power_up(game.current_score)
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            player = game.player
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.shield = True
                player.has_power_up = True
                player.type = power_up.type #tipo de image que estaria utilizando
                player.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
                
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset_power_ups(self):
        self.power_ups.clear()
        self.when_appears = random.randint(600,700)# es necessario esto?