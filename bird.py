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
        self.y = 200
        self.old_y = 0
        self.fall_vel = 3
        self.jump_vel = 15
        self.jump_height = 30
        self.jump_pressed = False
        self.is_jumping = False
        self.bird = None
        self.bird_angle = 0

    def show(self):
        self.bird = self.screen.blit(pygame.transform.rotate(self.bird_img, self.bird_angle), [self.x, self.y])

        self.jump()

        # if pygame.key.get_pressed()[pygame.K_SPACE]:
        #     self.jump_pressed = True;

    def jump(self):

        if self.jump_pressed:
            self.old_y = self.y
            self.jump_pressed = False
            self.is_jumping = True
            self.bird_angle = 0

        if self.is_jumping:
            if not self.old_y - self.y >= self.jump_height:
                self.y -= self.jump_vel
                self.bird_angle += 20
            else:
                self.is_jumping = False
        else:
            self.y += self.fall_vel
            if self.bird_angle > -90:
                self.bird_angle -= .4


    def trigger_jump(self):
        self.jump_pressed = True


    def check_top_bottom(self):
        if self.y <= 0 or self.y > 440:
            return True

        return False