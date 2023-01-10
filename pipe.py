import pygame
import os
import sys
import random
import math

BASE_DIR = os.path.dirname(__file__)


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
        self.min_pos = 80
        self.min_height = 40
        self.max_height = self.screen.get_height() - 280
        self.max_no_of_pipes_on_screen = 3
        self.nearest_pipe = 0
        self.pipe1 = None
        self.pipe2 = None
        self.all_pipes = []
        self.crossed_pipes = 0
        self.has_collided = False

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
            if pipe['pos'] > self.min_pos: temp.append(pipe)

        if len(self.pipes) > len(temp):
            self.crossed_pipes += 1

        self.pipes = temp
        self.generate_pipe()

    def generate_pipe(self):
        if len(self.pipes) < self.max_no_of_pipes_on_screen and self.nearest_pipe > int((self.screen.get_width() - self.min_pos)/self.max_no_of_pipes_on_screen):
            self.pipes.append({
                'pos': self.screen.get_width(),
                'height': random.randint(self.min_height, self.max_height)
            })

    def check_collision(self, bird):
        collided = False
        for pipe in self.all_pipes[:2]:
            try:
                if (pipe.colliderect(bird.bird)):
                    collided = True
                    break
            except:
                pass
        return collided

    def get_info(self, bird):
        try:
            if len(self.all_pipes) > 0:


                # bird_ = [bird.x+bird.bird.width, bird.y+bird.bird.height/2]
                # pipe1 = [self.all_pipes[0].x, self.all_pipes[0].height]
                # pipe2 = [self.all_pipes[1].x, self.all_pipes[1].y]

                # pygame.draw.line(self.screen, (153, 0, 0), bird_, pipe1, 2)
                # pygame.draw.line(self.screen, (153, 0, 0), bird_, pipe2, 2)
                # print(self.get_distance(pipe1, bird_), self.get_distance(pipe2, bird_))
                # return [bird.y, self.get_distance(pipe1, bird_), self.get_distance(pipe2, bird_)]


                return [bird.y, self.all_pipes[0].height, self.all_pipes[1].y, self.all_pipes[1].x-bird.x]
        except:
            pass
        return [0, 0, 0, 0]


    def get_distance(self, a, b):
        return int(math.sqrt(math.pow((a[0] - a[1]), 2) + math.pow((b[0] - b[1]), 2)))