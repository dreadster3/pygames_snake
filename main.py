import pygame
from pygame.time import Clock
from src.constants import SIZE, FRAMERATE
from src.game_setup import init_game

pygame.init()


clock = Clock()
screen, game_controller, world, snake = init_game()

while not game_controller.is_quitting:
    for event in pygame.event.get():
        game_controller.process_event(event)

    screen.fill(pygame.Color("black"))

    delta = clock.tick(FRAMERATE)
    world.render(screen)
    world.update(delta, screen)
    world.generate_collisions()

    pygame.display.flip()

