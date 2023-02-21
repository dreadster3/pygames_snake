from typing import List
from pygame.color import Color
from pygame.draw import rect
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.surface import Surface
from src.constants import CELLSIZE
from src.entities.GObject import GObject

class Snake(GObject):
    def __init__(self):
        super().__init__(Vector2(0, 0))
        self.__size = Vector2(CELLSIZE, CELLSIZE)
        self.__velocity : Vector2 = Vector2(0, 0)
        self.__color = Color("red")
        self.__speed_multiplier = 20
        self.__tail : List[Vector2] = []
        self.__previous_position = self.location

        self.add_on_collision(self.self_collision)

    @property
    def size(self):
        return self.__size

    @property
    def velocity(self) -> Vector2:
        return self.__velocity

    def self_colliding(self):
        head = Rect(self.location, self.size)
        for t in self.__tail:
            rect_t = Rect(t, self.size)
            if rect_t.collidepoint(self.location) and head.collidepoint(t):
                return True

        return False

    def self_collision(self, object):
        if isinstance(object, Snake):
            print("YOU LOSE")
            self.destroy()

    def is_colliding(self, object : GObject) -> bool:
        return Rect(self.location, self.size).collidepoint(object.location)

    def set_velocity(self, velocity):
        if self.velocity != Vector2(0, 0) and self.velocity.cross(velocity) == 0:
            return
        self.__velocity = velocity

    def increase_length(self):
        self.__tail.append(self.__previous_position)             

    def render(self, screen: Surface):
        # Draw Head
        rect(screen, self.__color, Rect(self.location.x, self.location.y, self.size.x, self.size.y))

        # Draw Tail
        for t in self.__tail:
            rect(screen, Color("yellow"), Rect(t.x, t.y, self.size.x, self.size.y))

    def update(self, delta : float, screen : Surface):
        if len(self.__tail) > 0:
            self.__previous_position = self.__tail.pop()
            self.__tail.insert(0, self.location)
        else:
            self.__previous_position = self.location
        temp_velocity = CELLSIZE * (delta / 1000) * (self.velocity * self.__speed_multiplier)
        new_location = self.location + temp_velocity
        new_x = new_location.x % screen.get_width()
        new_y = new_location.y % screen.get_height()
        self.set_location(Vector2(new_x, new_y))
        

    
