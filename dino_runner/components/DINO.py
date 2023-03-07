import pygame
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING
from pygame.sprite import Sprite

class DINOSAUR(Sprite):
    X_POS=120
    Y_POS=310
    JUMP_VELOCITY=10
    Y_POS_LIMIT = 200
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
        
        self.step_index = self.step_index + 1
        if self.step_index == 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image=RUNNING[0] if self.step_index <6 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS     

    def duck(self):
        self.image=DUCKING[0] if self.step_index <6 else DUCKING[1] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS+35
        self.dino_duck=False

    def jump(self):
        
        self.image = JUMPING
        self.dino_rect.x=self.X_POS
        self.dino_rect.y -= self.jump_vel 
        if self.dino_rect.y <= self.Y_POS_LIMIT:
            self.jump_vel *= -1
        if self.dino_rect.y > self.Y_POS:
            self.jump_vel *= -1
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False    
        
       
        
        
        
