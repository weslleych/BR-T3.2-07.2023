import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE , SONGS, SPACE_BAR, MENUBG, DINO_CRY, GAME_OVER, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = -12
        self.life_count = 3
        self.current_score = 0
        self.max_score = 0
        self.contador = 0 #SpaceBar animation
        self.salvador = 0
        self.lista_score = []
        
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        
        self.score_song = SONGS[0]
        self.score_song.set_volume (0.08)
        
        pygame.mixer.music.set_volume(0.04)
        pygame.mixer.music.play(-1)

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing and self.life_count == 3:
                self.show_menu()
            if not self.playing and self.life_count < 3:
                self.pos_menu()
        
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_continue(self):
        self.obstacle_manager.reset_obstacle()
        self.player.dino_jump = False

    def reset_game(self):
        self.obstacle_manager.reset_obstacle()
        self.player.dino_jump = False
        self.game_speed = 20
        self.current_score = 0
        self.life_count = 3
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)       
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()
        self.draw_power_up_time()

    def update_contador(self):
        self.contador += 1  #spaceBar animation
        if self.contador == 100:
            self.contador = 0

    def update_score(self):
        self.current_score +=1
        self.lista_score.append(self.current_score)
        self.max_score = max(self.lista_score)
        if self.current_score %100 == 0:
            self.game_speed += 2
            self.score_song.play()
        if self.playing == False:
            if self.salvador < self.current_score:
                self.salvador = self.current_score
                self.lista_score.append(self.salvador)
         
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        
        self.player.draw(self.screen)
    
        self.drawn_score()
        self.drawn_life()
        self.drawn_element()

        self.power_up_manager.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        

        pygame.display.flip()

    def draw_power_up_time(self):
         if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show >=0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"Power Up: {time_to_show}", True, (255,0,0))
                text_rect = text.get_rect()
                text_rect.x = 425
                text_rect.y = 100
                self.screen.blit(text, text_rect)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def drawn_score(self):
        self.text_score = (f"HI    {self.max_score}     {self.current_score}")
        self.align_score = (1000, 50)

    def drawn_life(self):
        self.text_life = (f"Life(s): {self.life_count}")
        self.align_life = (50, 50)

    def drawn_element(self):
        font = pygame.font.Font(FONT_STYLE, 18)
        text = font.render(self.text_life, True, (82,82,82))
        text2 = font.render(self.text_score, True, (82,82,82))
        text_rect = text.get_rect()
        text_rect2 = text2.get_rect()
        text_rect.center = (self.align_life)
        text_rect2.center = (self.align_score)
        self.screen.blit(text, text_rect)
        self.screen.blit(text2, text_rect2)


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
            
        self.screen.fill((255, 255, 255))
        self.screen.blit(MENUBG, (250, 50))
        half_screen_width = SCREEN_WIDTH //2
        font = pygame.font.Font(FONT_STYLE, 22)
        self.imageBar = SPACE_BAR[0]
        self.imageBar = SPACE_BAR[0] if self.contador < 50 else SPACE_BAR[1]
        self.screen.blit(self.imageBar, (485, 425))
        self.update_contador()       
        text = font.render (f"Prees                        to start", True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, 450)
        self.screen.blit(text, text_rect)

        pygame.display.update()

        self.handle_events_on_menu()

    def pos_menu(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        half_screen_width = SCREEN_WIDTH //2

        if self.life_count < 3 and self.life_count > 0:
            self.screen.fill((255, 255, 255))
            self.screen.blit(DINO_CRY, (475,100))  
            self.textCR = font.render(f"You hit an obstacle.", True,(114,110,109))
            self.textCR_align = (half_screen_width, 300)
            self.textCR2 = font.render(f"Your score is {self.current_score} and you have more {self.life_count} life(s). Prees (C) to continuo or (R) to reset", True,(114,110,109))
            self.textCR2_align = (half_screen_width, 350)
        if self.life_count == 0:
            self.screen.fill((255, 255, 255))
            self.screen.blit(GAME_OVER, (300,0))   
            self.textCR = font.render(f"Press (R) to restart", True,(114,110,109))
            self.textCR_align = (half_screen_width, 500)
            self.textCR2 = font.render(f"Your Score was: {self.current_score}   The HI: {self.max_score}", True,(114,110,109))
            self.textCR2_align = (half_screen_width, 570)    
        text = self.textCR  
        text2 = self.textCR2
        text_rect = text.get_rect()
        text_rect2 = text2.get_rect()
        text_rect.center = (self.textCR_align)
        text_rect2.center = (self.textCR2_align)
        self.screen.blit(text, text_rect)
        self.screen.blit(text2, text_rect2)


        pygame.display.update()

        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.plaiyng = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE] and self.life_count == 3:
                    pygame.time.delay(500)
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_r]:
                    pygame.time.delay(500)
                    self.reset_game()
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_c] and self.life_count < 3 and self.life_count > 0:
                    pygame.time.delay(500)
                    self.game_continue()
                    self.run()
    
            
    