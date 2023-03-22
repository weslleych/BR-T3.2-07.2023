import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, images, height):
        self.type = random.randint(0,2)
        self.type2= self.type
        super().__init__(images, self.type, self.type2)

        
        self.rect.y = height    

