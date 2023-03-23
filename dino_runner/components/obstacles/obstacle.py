
from dino_runner.utils.constants import SCREEN_WIDTH, SONGS
from dino_runner.components.dinosaur import Y_POS

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
        if len (self.lista) == 2:
            screen.blit(self.image,(self.rect.x, self.rect.y))
            self.image = self.lista[0] if self.bat_index < 10 else self.lista[1]

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        
        
        if self.rect.x < -self.rect.width:
            obstacles.pop()

        self.bat_index += 1
        if self.bat_index == 20:
            self.bat_index = 0

class Obstacle2:
    def __init__(self, images, type, type2):
        self.lista = [images[type], images[type2]]

        self.image = self.lista[0]
        self.rect = self.image.get_rect()
        self.rect.y = -200

        self.boom = SONGS[4]

        self.cont = 0
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
 
    def update(self, game_speed, obstacles):
        self.rect.y += 15
        
        if self.rect.y >= (Y_POS-10):
            self.rect.y = Y_POS+10
            self.cont += 1
            self.boom.set_volume (0.05)
            self.boom.play() 
            
            self.image = self.lista[1]
            if self.cont == 15:
                obstacles.pop()
           
            
          