
from dino_runner.utils.constants import HAMMER_TYPE
from dino_runner.utils.constants import SHIELD_TYPE, HEART_TYPE
from dino_runner.utils.constants import DEFAULT_TYPE
import pygame
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING, DEAD, RUNNING_SHIELD,RUNNING_HAMMER,JUMPING_HAMMER,JUMPING_SHIELD,DUCKING_HAMMER,DUCKING_SHIELD

from pygame.sprite import Sprite

class DINOSAUR(Sprite):
    X_POS=120
    Y_POS=310
    JUMP_VELOCITY=10
    Y_POS_LIMIT = 125
    POWER_UP_TIME = 200 
                                 


    def __init__(self):
        self.image=RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS
        self.jump_vel=self.JUMP_VELOCITY
        self.step_index=0
        self.dino_run=True
        self.dino_duck=False
        self.dino_jump = False
        self.type = DEFAULT_TYPE
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER }
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER }
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER }
        self.power_up_time = 0

    def process_event(self, user_input):
        if user_input[pygame.K_DOWN]:
            self.dino_run=False
            self.dino_duck=True
            self.dino_jump = False
        elif user_input[pygame.K_UP]:
            self.dino_run=False
            self.dino_duck=False
            self.dino_jump = True    
        
    

    def update(self, user_input):
        self.process_event(user_input)
        if self.dino_duck:
            self.duck()
        elif self.dino_jump:
            self.jump()    
        else:
            self.run()  

        self.power_up_time -=1
        if self.power_up_time < 0:
            self.type=DEFAULT_TYPE
        self.step_index = self.step_index + 1
        if self.step_index == 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        
        self.image=self.run_img[self.type][0] if self.step_index <6 else self.run_img[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS     

    def duck(self):
        self.image=self.duck_img[self.type][0] if self.step_index <6 else self.duck_img[self.type][1] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS+35
        self.dino_duck=False

    def jump(self):
        
        self.image = self.jump_img[self.type]
        self.dino_rect.x=self.X_POS
        self.dino_rect.y -= self.jump_vel 
        if self.dino_rect.y <= self.Y_POS_LIMIT:
            self.jump_vel *= -1
        if self.dino_rect.y > self.Y_POS:
            self.jump_vel *= -1
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False  

    def dead(self):
        self.image = DEAD    
    def activate_power_up(self, power_up_type):
        if power_up_type == SHIELD_TYPE:
            self.type=SHIELD_TYPE
            self.power_up_time=self.POWER_UP_TIME

        elif power_up_type == HAMMER_TYPE:
            self.type=HAMMER_TYPE
            self.power_up_time=self.POWER_UP_TIME

        
               

        
        
        
