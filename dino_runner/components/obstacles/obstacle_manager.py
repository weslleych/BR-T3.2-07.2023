import pygame
import random

from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import BirdTop, BirdBottom, BirdMid 
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
         
    
    def update(self, game):
        self.sorteador = random.randint(0,1)
        self.sorteador2 = random.randint(0,1)
        self.sorteador3 = random.randint(0,2)
        if self.sorteador == 0 and len(self.obstacles) == 0:
            if self.sorteador2 == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            if self.sorteador2 == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
        if self.sorteador == 1 and len(self.obstacles) == 0:
            if self.sorteador3 == 0:
                self.obstacles.append(BirdTop(BIRD))
            if self.sorteador3 == 1:
                self.obstacles.append(BirdMid(BIRD))  
            if self.sorteador3 == 2:
                self.obstacles.append(BirdBottom(BIRD))            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count+=1
                break                
        
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacle(self):
        self.obstacles.clear()
        


