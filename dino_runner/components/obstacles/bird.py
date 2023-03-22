from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, images, height):
        self.type = (0)
        self.type2 = (1)
        super().__init__(images, self.type, self.type2)
        
        self.rect.y = height