import pygame
import os

BASE_DIR = "/home/random/prac/game/flappy_bird"


class Background:
    background_img = pygame.image.load(os.path.join(BASE_DIR, "assets", "background.jpeg"))
    bottom_img = pygame.image.load(os.path.join(BASE_DIR, "assets", "bottom.png"))

    def __init__(self, screen):
        self.screen = screen
        self.vel = 1
        self.background_pos = [0, 0]
        self.bottom_wdt = self.bottom_img.get_rect().width
        self.bottom_hei = self.bottom_img.get_rect().height
        self.bottom_pos1 = [0, self.screen.get_height() - self.bottom_hei]
        self.bottom_pos2 = [self.screen.get_width(), self.screen.get_height() - self.bottom_hei]


    def show_background(self):
        self.screen.blit(self.background_img, self.background_pos)


    def show_ground(self):
        first_bottom_pos = self.screen.blit(self.bottom_img, self.bottom_pos1)
        second_bottom_pos = self.screen.blit(self.bottom_img, self.bottom_pos2)
        self.move_bottom(first_bottom_pos.width, second_bottom_pos.width)

    def move_bottom(self, wdt1, wdt2):
        if wdt1 == self.screen.get_width():
            self.bottom_pos2[0] = self.screen.get_width()

        elif wdt2 == self.screen.get_width():
            self.bottom_pos1[0] = self.screen.get_width()

        self.bottom_pos1[0] -= self.vel
        self.bottom_pos2[0] -= self.vel