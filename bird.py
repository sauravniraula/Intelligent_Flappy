import pygame
import sys
import os

BASE_DIR = "/home/random/prac/game/flappy_bird"


class Bird:
    bird_res = [50, 50]
    bird_img = pygame.image.load(os.path.join(BASE_DIR, "assets", "bird.png"))
    bird_img = pygame.transform.scale(bird_img, bird_res)

    def __init__(self, screen):
        self.screen = screen
        self.x = 150
        self.y = 50
        self.old_y = 0
        self.fall_vel = 2
        self.jump_vel = 20
        self.jump_height = 25
        self.jump_pressed = False
        self.is_jumping = False
        self.bird = None

    def show(self):
        self.bird = self.screen.blit(self.bird_img, [self.x, self.y])
        if self.bird.y <= 0 or self.bird.y > 440:
            sys.exit()

        self.jump()

    def jump(self):

        if self.jump_pressed:
            self.old_y = self.y
            self.jump_pressed = False
            self.is_jumping = True

        if self.is_jumping:
            if not self.old_y - self.y >= self.jump_height:
                self.y -= self.jump_vel
            else:
                self.is_jumping = False
        else:
            self.y += self.fall_vel