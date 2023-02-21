from pygame.color import Color
from pygame.draw import rect
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.surface import Surface
from src.constants import CELLSIZE
from src.entities.GObject import GObject
from src.entities.Snake import Snake

class Fruit(GObject):
    def __init__(self, location : Vector2) -> None:
        super().__init__(location)
        self.__size = Vector2(CELLSIZE, CELLSIZE)
        self.__color = Color("green")

        self.add_on_collision(self.__destroy_on_eat)

    def __destroy_on_eat(self, object):
        if isinstance(object, Snake):
            self.destroy()

    def render(self, screen: Surface):
        rect(screen, self.__color, Rect(self.location.x, self.location.y, self.__size.x, self.__size.y))

    def is_colliding(self, object : GObject) -> bool:
        return Rect(self.location, self.__size).collidepoint(object.location)
    
