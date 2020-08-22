import pygame
import os
import sys

from bird import Bird
from background import Background
from pipe import Pipe


BASE_DIR = "/home/random/prac/game/flappy_bird"


#colors
black = (0, 0, 0)

# pygame 
SIZE = WIDTH, HEIGHT = 1000, 563
screen = pygame.display.set_mode(SIZE)

#background
background = Background(screen)

#pipe
pipe = Pipe(screen)

#bird
bird = Bird(screen)


def render():
    # screen.fill(black)

    background.show_background()
    pipe.show()
    background.show_ground()
    bird.show()

    # check collision
    pipe.check_collision(bird)

    pygame.display.flip()       
    pygame.display.update()

def main():
    render()



if __name__ == "__main__":

    while True:
        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump_pressed = True