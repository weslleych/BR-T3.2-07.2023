import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, SONGS,  DEFAULT_TYPE,SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, HAMMER_TYPE, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER,UMBRELLA_TYPE, DUCKING_UMBRELLA, JUMPING_UMBRELLA, RUNNING_UMBRELLA, SCREEN_WIDTH

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, UMBRELLA_TYPE: DUCKING_UMBRELLA}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE:JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, UMBRELLA_TYPE: JUMPING_UMBRELLA}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE:RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, UMBRELLA_TYPE: RUNNING_UMBRELLA}

X_POS = 80
Y_POS = 310
Y_DUCK = 345
JUMP_VEL = 8.5

class Dinosaur:
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.step_index = 0
        self.jump_vel = JUMP_VEL

        self.has_power_up = False
        self.has_hammer = False
        self.has_umbrella = False

        self.jump_song = SONGS[1]
        self.jump_song.set_volume(0.05)
    
    def run(self):
        self.image = RUN_IMG[self.type][self.step_index//5]

        self.dino_rect.y = Y_POS
        self.step_index+=1        
        
    
    def jump(self):
        self.image = JUMP_IMG[self.type]
        
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -=0.8
        
        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL
    
    def duck(self):
        
        self.image = DUCK_IMG[self.type][self.step_index//5]

        self.dino_rect.y =  Y_DUCK
        self.step_index += 1

        self.dino_duck = False
           
    
    
    def update(self, user_input):
        if (user_input[pygame.K_UP] or user_input[pygame.K_w] or user_input[pygame.K_SPACE]) and not self.dino_jump and not self.dino_duck:
            self.dino_jump = True
            self.dino_run = False
            self.jump_song.play()
       
        elif (user_input[pygame.K_DOWN] or user_input[pygame.K_LSHIFT] or user_input[pygame.K_s]) and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False

        elif not self.dino_jump:
            self.dino_run = True

        elif(user_input[pygame.K_DOWN] or user_input[pygame.K_LSHIFT] or user_input[pygame.K_s]) and self.dino_jump:
            self.jump_vel -=2

        if user_input[pygame.K_RIGHT]:
            self.dino_rect.x +=10
            if self.dino_rect.x >= SCREEN_WIDTH-100:
                self.dino_rect.x = SCREEN_WIDTH-100
            
        elif user_input[pygame.K_LEFT]:
            self.dino_rect.x -=10
            if self.dino_rect.x <= 0:
                self.dino_rect.x = 0

        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump() 
        if self.dino_duck:
            self.duck()               
            
        if self.step_index >= 10:
            self.step_index = 0
            
        
    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))