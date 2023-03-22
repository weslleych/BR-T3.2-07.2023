import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE , SONGS, SPACE_BAR, MENUBG, DINO_CRY, GAME_OVER
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

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
        self.y_pos_bg = 380
        self.life_count = 3
        self.current_score = 0
        self.max_score = 0
        self.contador = 0
        self.salvador = 0
        self.lista_score = []
        
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        
        self.score_song = SONGS[0]
        self.score_song.set_volume (0.08)
        
        pygame.mixer.music.set_volume(0.04)
        pygame.mixer.music.play(-1)

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        
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
    def reset_game(self):
        self.obstacle_manager.reset_obstacle()
        self.game_speed = 20
        self.current_score = 0
        self.life_count = 3
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)       
        self.obstacle_manager.update(self)
        self.update_score()
        print(self.life_count)

    def update_contador(self):
        self.contador += 1
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
        self.obstacle_manager.draw(self.screen)
        self.drawn_score()
        self.drawn_life()
        #pygame.display.update()
        pygame.display.flip()

    def drawn_score(self):
        font = pygame.font.Font(FONT_STYLE, 18)
        text = font.render (f"HI    {self.max_score}     {self.current_score}", True,(82,82,82))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def drawn_life(self):
        font = pygame.font.Font(FONT_STYLE, 18)
        text = font.render (f"Life(s): {self.life_count}", True, (82,82,82))
        text_rect = text.get_rect()
        text_rect.center = (50, 50)
        self.screen.blit(text, text_rect)


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        if self.life_count == 3:
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

        elif self.life_count < 3 and self.life_count > 0:
            self.screen.fill((255, 255, 255))
            half_screen_height = SCREEN_HEIGHT //2
            half_screen_width = SCREEN_WIDTH //2
            font = pygame.font.Font(FONT_STYLE, 22)
            self.screen.blit(DINO_CRY, (475,100))       
            text = font.render (f"You hit an obstacle.", True,(114,110,109))
            text2 = font.render (f"Your score is {self.current_score} and you have more {self.life_count} life(s). Prees (C) to continuo or (R) to reset", True,(114,110,109))
            text_rect = text.get_rect()
            text_rect2 = text2.get_rect()
            text_rect.center = (half_screen_width, 350)
            text_rect2.center = (half_screen_width, 380)
            self.screen.blit(text, text_rect)
            self.screen.blit(text2, text_rect2)

        if self.life_count == 0:
            self.screen.fill((255, 255, 255))
            half_screen_height = SCREEN_HEIGHT //2
            half_screen_width = SCREEN_WIDTH //2
            font = pygame.font.Font(FONT_STYLE, 22)
            self.screen.blit(GAME_OVER, (300, 0))
            text = font.render (f"Press (R) to restart", True,(114,110,109))
            text2 = font.render (f"Your Score was: {self.current_score}   The HI: {self.max_score}", True,(114,110,109))
            text_rect = text.get_rect()
            text_rect2 = text2.get_rect()
            text_rect.center = (half_screen_width, 500)
            text_rect2.center = (half_screen_width, 570)
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
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_r]:
                    self.reset_game()
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_c] and self.life_count < 3 and self.life_count > 0:
                    self.game_continue()
                    self.run()
    
            
    