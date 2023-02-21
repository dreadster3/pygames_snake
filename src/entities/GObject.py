from abc import abstractmethod
from pygame import Rect
from pygame.draw import rect
from pygame.surface import Surface
from pygame.math import Vector2

class GObject:
    def __init__(self, location : Vector2) -> None:
        self.__location : Vector2 = location
        self.__destroyed : bool = False
        self.__on_collision = []


    @abstractmethod
    def render(self, screen : Surface):
        pass

    @abstractmethod
    def update(self, delta : float, screen : Surface):
        pass

    def on_collision(self, object):
        for action in self.__on_collision:
            action(object)

    def destroy(self) -> None:
        self.__destroyed = True

    def self_colliding(self):
        return False

    @abstractmethod
    def is_colliding(self, object) -> bool:
        pass

    # Setters and Getters
    @property
    def location(self) -> Vector2:
        return self.__location

    def set_location(self, location : Vector2):
        self.__location = location

    def is_destroying(self):
        return self.__destroyed

    def add_on_collision(self, action):
        self.__on_collision.append(action)

