import random

from dino_runner.components.obstacles.obstacle import Obstacle2

class meteor(Obstacle2):
    def __init__(self, images, width):
        self.type = (0)
        self.type2 = (1)
        super().__init__(images, self.type, self.type2)

        self.width = width
        self.rect.x = self.width