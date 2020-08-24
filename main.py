import pygame
import os
import sys
import neat

from bird import Bird
from background import Background
from pipe import Pipe

pygame.font.init()
STAT_FONT = pygame.font.SysFont("comicsans", 50)

BASE_DIR = "/home/random/prac/game/flappy_bird"


#colors
black = (0, 0, 0)

# pygame 
SIZE = WIDTH, HEIGHT = 1000, 563
screen = pygame.display.set_mode(SIZE)


def render(birds, background, pipe):
    background.show_background()
    pipe.show()
    for bird in birds: bird.show()
    background.show_ground()

    pygame.display.update()


def main(genomes, config):
    global screen

    background = Background(screen)
    pipe = Pipe(screen)

    run = True

    nets = []
    ge = []
    birds = []

    for _, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird(screen))
        ge.append(genome)

    prev_score = 0

    while run and len(birds) > 0:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break


        for i, bird in enumerate(birds):
            ge[i].fitness += .01

            output = nets[i].activate(pipe.get_info(bird))
            if output[0] > 0.5:
                bird.trigger_jump()

            if prev_score < pipe.crossed_pipes:
                ge[i].fitness += 2
                prev_score += 1

            if pipe.check_collision(bird) or bird.check_top_bottom():
                ge[i].fitness -= 1 #?
                nets.pop(i)
                ge.pop(i)
                birds.pop(i)


        render(birds, background, pipe)




def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.StatisticsReporter())

    winner = p.run(main, 50)


if __name__ == "__main__":


    local_dir = os.path.dirname(__file__)
    config_file = os.path.join(local_dir, "neat_config.cfg")
    run(config_file)

    # while True:
    #     render()