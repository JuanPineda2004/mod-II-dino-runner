
import random

from dino_runner.utils.constants import SHIELD_TYPE, HAMMER_TYPE, HEART_TYPE

from dino_runner.components.obstacles.bird import Bird

from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.cactus import SmallCactus
import pygame
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD



class Obstaclemanager:
    def __init__(self):
        self.obstacles=[]

    def generate_obstacle(self):
        obstacles_types ={
            0: SmallCactus(SMALL_CACTUS[0]),
            1: SmallCactus(SMALL_CACTUS[1]),
            2: SmallCactus(SMALL_CACTUS[2]),
            3: LargeCactus(LARGE_CACTUS[0]),
            4: LargeCactus(LARGE_CACTUS[1]),
            5: LargeCactus(LARGE_CACTUS[2]),
            6: Bird(BIRD[0])
        }
        return obstacles_types[random.randint(0, 6)]    

    def update(self, game):
        if len(self.obstacles)==0:
            self.obstacles.append(self.generate_obstacle())


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.type == SHIELD_TYPE:
                print("shield activated, no damage received")

            elif  game.player.type == HAMMER_TYPE:  
                print("hammer activate")
                if game.player.dino_rect.colliderect(obstacle.rect):
                    obstacle.rect = pygame.Rect(0, 0, 0, 0)
            elif game.player.type == HEART_TYPE:
                print("activate her")
                    

            elif game.player.dino_rect.colliderect(obstacle.rect):
                game.player.dead()
                
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    def remove_obstacles(self):
        self.obstacles=[]        
