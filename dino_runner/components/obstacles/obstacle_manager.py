import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SONGS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
         
    
    def update(self, game):
        self.sorteador = random.randint(0,2)
        self.sorteador2 = random.randint(0,2)
        if self.sorteador == 0 and len(self.obstacles) == 0:  
            self.obstacles.append(Cactus(SMALL_CACTUS, 325))
        if self.sorteador == 1 and len(self.obstacles) == 0:
            self.obstacles.append(Cactus(LARGE_CACTUS, 300))
        if self.sorteador == 2 and len(self.obstacles) == 0:
            if self.sorteador2 == 0:
                self.obstacles.append(Bird(BIRD, 230))
            if self.sorteador2 == 1:
                self.obstacles.append(Bird(BIRD, 270))
            if self.sorteador2 == 2:
                self.obstacles.append(Bird(BIRD, 320))
          
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    SONGS[2].set_volume (0.60)
                    SONGS[2].play()
                    game.playing = False
                    game.life_count-=1
                    break
                else:
                    self.obstacles.remove(obstacle)         
        
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacle(self):
        self.obstacles.clear()
        


