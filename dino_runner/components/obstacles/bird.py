import random

from dino_runner.components.obstacles.obstacle import Obstacle2

class BirdTop(Obstacle2):
    def __init__(self, images):
        self.choose = (1)
        self.choose2 = (0)
        super().__init__(images, self.choose, self.choose2)
        
        self.rect.y = 230

class BirdMid(Obstacle2):
    def __init__(self, images):
        self.choose = (1)
        self.choose2 = (0)
        super().__init__(images, self.choose, self.choose2)
        
        self.rect.y = 270

class BirdBottom(Obstacle2):
    def __init__(self, images):
        self.choose = (1)
        self.choose2 = (0)
        super().__init__(images, self.choose, self.choose2)
        
        self.rect.y = 320