import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5

class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.step_index = 0
        self.step_indexDuck = 0
        self.jump_vel = JUMP_VEL
    
    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1] #ternary operator 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index+=1        
        
        if self.step_index >= 10:
            self.step_index = 0
    
    def jump(self):
        self.image = JUMPING
        
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -=0.8
        
        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL
    
    def duck(self):
        
        self.image = DUCKING[0] if self.step_indexDuck < 5 else DUCKING[1]
        self.dino_rect.y = self.dino_rect.y + 35
        self.step_indexDuck+=1        
        
        if self.step_indexDuck >= 10:
            self.step_indexDuck = 0
    
    
    def update(self, user_input):
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_run = True
        if user_input[pygame.K_UP] and self.dino_duck:
            self.dino_duck=False
            self.dino_jump=True
        if user_input[pygame.K_DOWN]:
            self.dino_duck = True
        elif not user_input[pygame.K_DOWN]:
            self.dino_duck = False
        if user_input[pygame.K_DOWN] and self.dino_jump:
            self.dino_jump=False
            self.dino_duck=True      
        if user_input[pygame.K_UP] and user_input[pygame.K_DOWN] and self.dino_duck:
            self.dino_duck = False
            self.dino_jump= True
            
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump() 
        if self.dino_duck:
            self.duck()               
            
    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))