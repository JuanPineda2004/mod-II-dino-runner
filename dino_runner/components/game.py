from dino_runner.utils.text_utils import get_score_max
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD,DEAD,JUMPING_HAMMER
from dino_runner.utils.constants import VI
from dino_runner.utils.constants import RE
from dino_runner.utils.constants import GO
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import CLOUD
from dino_runner.components.cloud import clouds
from dino_runner.utils.text_utils import get_centered_message
from dino_runner.utils.text_utils import get_score_element
from dino_runner.components.obstacles.obstacle_manager import Obstaclemanager
from dino_runner.components.DINO import DINOSAUR
import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    INITIAL_SPEED=20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.INITIAL_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = DINOSAUR()
        self.obstacle_manager = Obstaclemanager()
        self.power_up_manager = PowerUpManager()
        self.death_count = 0
        self.points = 0
        self.high_score =self.points
        

    def show_score(self):
        self.points += 1

        if self.points % 100 ==0:
            self.game_speed +=1

        score, score_rect = get_score_element(self.points)
        self.screen.blit(score, score_rect)

    def show_max(self):
        
        score, score_rect = get_score_max(self.high_score)
        self.screen.blit(score, score_rect)    

    

      

    def show_menu(self):
        half_screen_width = SCREEN_WIDTH //2
        half_screen_height = SCREEN_HEIGHT //2
        
        if self.death_count==0:
            self.screen.fill((255, 255, 255))
            text, text_rect = get_centered_message('WELCOME TO DINO GAME!!!')
            self.screen.blit(text, text_rect)
            text, text_rect = get_centered_message(f"press any key to continue", y_offset=60, font_size=25 )
            self.screen.blit(text, text_rect)
            self.screen.blit(ICON, (half_screen_width -50, half_screen_height-200))
            self.screen.blit(CLOUD, (half_screen_width +100, half_screen_height-200))
            self.screen.blit(CLOUD, (half_screen_width -100, half_screen_height-200))
            self.screen.blit(CLOUD, (half_screen_width -300, half_screen_height-100))
            self.screen.blit(CLOUD, (half_screen_width +150, half_screen_height-250))
            self.screen.blit(CLOUD, (half_screen_width +50, half_screen_height-180))
            self.screen.blit(BIRD[0], (half_screen_width+50 , half_screen_height-100))
            self.screen.blit(BIRD[0], (half_screen_width-170 , half_screen_height-100))
            self.screen.blit(BIRD[1], (half_screen_width-50 , half_screen_height-100))
            self.screen.blit(LARGE_CACTUS[2], (half_screen_width-300 , half_screen_height+0))
            self.screen.blit(LARGE_CACTUS[2], (half_screen_width+200 , half_screen_height+0))
            image_width = BG.get_width()
            self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            if self.x_pos_bg <= -image_width:
                self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
                self.x_pos_bg = 0
            self.x_pos_bg -= self.game_speed
            
        else:
            self.screen.fill((255, 255, 255))
            
            self.screen.blit(GO, (half_screen_width -195, half_screen_height-140))
            self.screen.blit(DEAD, (half_screen_width -300, half_screen_height-100))
            self.screen.blit(JUMPING_HAMMER, (half_screen_width +200, half_screen_height-100))
            self.screen.blit(RE, (half_screen_width -50, half_screen_height-100))
            text, text_rect = get_centered_message('press any key to retry!')
            self.screen.blit(text, text_rect)
            text, text_rect = get_centered_message(f"ATTEMPS: {self.death_count}", y_offset=40, font_size=20 )
            self.screen.blit(text, text_rect)
        pygame.display.update()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                print('Game Over')
                self.death_count +=1
                print()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.run()    
                
        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.time.delay(1000)
        self.death_count +=1    
        self.playing=False
        self.points=0
        self.high_score+=self.points
        self.game_speed = self.INITIAL_SPEED
        self.obstacle_manager.remove_obstacles()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.show_score()
        self.show_max()
        
        self.clouds_1()
        pygame.display.update()
        pygame.display.flip()

    def clouds_1(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1020, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1070, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2030, self.y_pos_bg -300))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +900, self.y_pos_bg -120))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +3000, self.y_pos_bg -189))
            

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
