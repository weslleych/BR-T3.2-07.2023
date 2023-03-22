import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE , SONGS
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
        self.death_count = 0
        self.score = 0
        self.score_song = SONGS[0]
        self.score_song.set_volume (0.05)
        
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

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
        self.score = 0
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)       
        self.obstacle_manager.update(self)
        self.update_score()

    def update_score(self):
        self.score +=1
        self.lista_score = []
        if self.score %100 == 0:
            self.game_speed += 2
            self.score_song.play()
        if self.playing == False:
            self.lista_score.append(self.score)
            for points in self.lista_score:
                self.show_score = points
                
            
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.drawn_score()
        #pygame.display.update()
        pygame.display.flip()

    def drawn_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render (f"score {self.score}", True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
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
        self.screen.fill((255, 255, 255))

        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2

        font = pygame.font.Font(FONT_STYLE, 22)
        if self.death_count == 0:
            texto = font.render (f"Prees (S) to start playing", True,(0,0,0))
        else:
            texto = font.render (f"Your score was {self.show_score}. Prees (c) to continue or (R) to restart game", True,(0,0,0))
        text = texto
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        self.screen.blit(text, text_rect)

        pygame.display.update()

        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.plaiyng = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and self.death_count == 0:
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_r]:
                    self.reset_game()
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_c]:
                    self.game_continue()
                    self.run()

            
    