from typing import Tuple
from pygame.display import set_mode
from pygame.constants import K_s,K_DOWN, K_LEFT, K_RIGHT, K_UP
from pygame.math import Vector2
from pygame.surface import Surface
from src.constants import CELLSIZE, HEIGHT, WIDTH, SIZE
from src.entities import Snake, Fruit, GObject
from src.services import World, GameController, GameState
import random


def init_game() -> Tuple[Surface, GameController, World, Snake]:
    screen = set_mode(SIZE)
    world = World()
    game_controller = GameController()
    game_state = GameState()
    snake = Snake()
    fruit = Fruit(Vector2(100, 100))

    world.add_game_object(snake)
    world.add_game_object(fruit)
    
    setup_inputs(game_controller, game_state = game_state, snake = snake)

    snake.add_on_collision(eat_fruit(game_state, snake))
    fruit.add_on_collision(spawn_fruit(screen, world))

    return (screen, game_controller, world, snake)
        

def eat_fruit(game_state : GameState, snake : Snake):
    def __eat_fruit(object : GObject):
        if isinstance(object, Fruit):
            snake.increase_length()                        
            game_state.add_to_score(10)
    return __eat_fruit

def spawn_fruit(screen: Surface, world : World):
    def __spawn_fruit(object : GObject):
        if isinstance(object, Snake):
            random_x = random.randint(0, int(screen.get_width()) - CELLSIZE)
            random_y = random.randint(0, int(screen.get_height()) - CELLSIZE)
            fruit = Fruit(Vector2(random_x, random_y))
            fruit.add_on_collision(spawn_fruit(screen, world))
            world.add_game_object(fruit)

    return __spawn_fruit
    
        


def setup_inputs(game_controller : GameController, **kwargs):
    snake = kwargs.get("snake")

    if not snake:
        raise Exception("Invalid snake")

    game_controller.add_input_mapping(K_UP, snake.set_velocity, Vector2(0, -1))
    game_controller.add_input_mapping(K_DOWN, snake.set_velocity, Vector2(0, 1))
    game_controller.add_input_mapping(K_RIGHT, snake.set_velocity, Vector2(1, 0))
    game_controller.add_input_mapping(K_LEFT, snake.set_velocity, Vector2(-1, 0))

    game_state = kwargs.get("game_state")
    if game_state:
        game_controller.add_input_mapping(K_s, lambda : print("Score:",game_state.score))
