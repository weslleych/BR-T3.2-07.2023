import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.metero import meteor
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SONGS, METEOR



class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) ==0:
            self.sorteador = random.randint(0,3)
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
        if self.sorteador == 3 and len(self.obstacles) == 0:
            self.obstacles.append(meteor(METEOR, random.randint(10,600)))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.has_power_up == True:
                    self.obstacles.remove(obstacle) 
                elif game.player.has_hammer and (self.sorteador==0 or self.sorteador==1):
                    self.obstacles.remove(obstacle) 
                elif game.player.has_umbrella and self.sorteador==3:
                    self.obstacles.remove(obstacle) 

                else:   
                    pygame.time.delay(500)
                    SONGS[2].set_volume (0.60)
                    SONGS[2].play()
                    game.playing = False
                    game.life_count-=1
                    break
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacle(self):
        self.obstacles.clear()


