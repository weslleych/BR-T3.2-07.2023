
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle:
    def __init__(self, images, type):
        self.image = images[type]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
    
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
        
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        
        if self.rect.x < -self.rect.width:
            obstacles.pop()
class Obstacle2:
    def __init__(self, images, choose, choose2):
        self.step_index = 0
        self.lista = images[choose], images[choose2]
        self.image = self.lista[0]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
                
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
        
    def update(self, game_speed, obstacles):
        self.image = self.lista[0] if self.step_index < 5 else self.lista[1]
        self.rect.x -= game_speed

        
        if self.rect.x < -self.rect.width:
            obstacles.pop()

        self.step_index += 1
        if self.step_index == 10:
            self.step_index = 0
         
        