import pygame
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING
from pygame.sprite import Sprite

class DINOSAUR(Sprite):
    X_POS=120
    Y_POS=310
    JUMP_VELOCITY=8.5
    def __init__(self):
        self.image=RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS
        self.jump_vel=self.JUMP_VELOCITY
        self.step=0
        self.dino_jump = False
        
    

    def update(self, user_input):
        if user_input[pygame.K_DOWN]:
            self.duck()
        elif user_input[pygame.K_UP]:
            self.jump()    
        else:
            self.run()    
        
        self.step+=1
        if self.step == 10:
            self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image=RUNNING[0] if self.step <6 else RUNNING[1]
        
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS     

    def duck(self):
        self.image=DUCKING[0] if self.step <6 else DUCKING[1] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS+35

    def jump(self):
        
        self.image = JUMPING
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS-130
        self.dino_rect.y -= self.jump_vel * 4
        self.jump_vel -= 0.8
       
        
        
        
