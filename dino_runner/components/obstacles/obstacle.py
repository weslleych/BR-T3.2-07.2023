
from dino_runner.utils.constants import SCREEN_WIDTH

class Obstacle:
    def __init__(self, images, type, type2):
        self.lista = [images[type], images[type2]]
        self.image = self.lista[0]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

        self.bat_index = 0
    
    def draw(self,screen):
        if len(self.lista) == 1:
            screen.blit(self.image,(self.rect.x, self.rect.y))
        if len (self.lista) > 1:
            screen.blit(self.image,(self.rect.x, self.rect.y))
            self.image = self.lista[0] if self.bat_index < 10 else self.lista[1]

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        
        
        if self.rect.x < -self.rect.width:
            obstacles.pop()

        self.bat_index += 1
        if self.bat_index == 20:
            self.bat_index = 0
        