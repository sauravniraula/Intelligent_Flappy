import pygame
import os
import sys
import random

BASE_DIR = "/home/random/prac/game/flappy_bird"


class Pipe:
    pipe_res = (100, 400)
    pipe_img = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets", "pipe.png")), pipe_res)

    pipe1_img = pygame.transform.rotate(pipe_img, 180)
    pipe2_img = pipe_img

    def __init__(self, screen):
        self.screen = screen
        self.pipes = []
        self.vel = 1
        self.pipe_gap = 150
        self.min_pos = 50
        self.min_height = 40
        self.max_height = self.screen.get_height() - 280
        self.max_no_of_pipes_on_screen = 4
        self.nearest_pipe = 0
        self.pipe1 = None
        self.pipe2 = None
        self.all_pipes = []
        self.crossed_pipes = 0

    def show(self):
        self.nearest_pipe = self.screen.get_width()
        temp = []
        self.all_pipes = []

        for pipe in self.pipes:
            self.pipe1 = self.screen.blit(self.pipe1_img, [pipe['pos'], pipe['height'] - self.pipe_res[1]])
            self.pipe2 = self.screen.blit(self.pipe2_img, [pipe['pos'], pipe['height'] + self.pipe_gap])
            self.all_pipes.append(self.pipe1)
            self.all_pipes.append(self.pipe2)

            pipe['pos'] -= 1
            if self.screen.get_width() - pipe['pos'] < self.nearest_pipe: self.nearest_pipe = self.screen.get_width() - pipe['pos']
            if pipe['pos'] > 50: temp.append(pipe)

        if len(self.pipes) > len(temp):
            self.crossed_pipes += 1
            print(self.crossed_pipes)

        self.pipes = temp
        self.generate_pipe()

    def generate_pipe(self):
        if len(self.pipes) < self.max_no_of_pipes_on_screen and self.nearest_pipe > int((self.screen.get_width() - self.min_pos)/self.max_no_of_pipes_on_screen):
            self.pipes.append({
                'pos': self.screen.get_width(),
                'height': random.randint(self.min_height, self.max_height)
            })

    def check_collision(self, bird):
        for pipe in self.all_pipes:
            if (pipe.colliderect(bird.bird)):
                sys.exit()


            


# no of pipes in screen

# position of pipes in screen -> posn of bird to screen width