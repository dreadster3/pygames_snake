from typing import List
from pygame.surface import Surface
from src.entities import GObject

class World:
    def __init__(self) -> None:
        self.__game_objects : List[GObject] = []

    def add_game_object(self, object : GObject):
        self.__game_objects.append(object)

    def update(self, delta : float, screen : Surface):
        for go in self.__game_objects:
            if not go.is_destroying():
                go.update(delta, screen)
            else:
                self.__game_objects.remove(go)

    def render(self, screen : Surface):
        for go in self.__game_objects:
            go.render(screen)
                
    def generate_collisions(self):
        for i in range(len(self.__game_objects)):
            game_object_1 = self.__game_objects[i]

            if game_object_1.self_colliding():
                game_object_1.on_collision(game_object_1)

            for j in range(i + 1, len(self.__game_objects)):
                game_object_2 = self.__game_objects[j]
                if game_object_1.is_colliding(game_object_2) or game_object_2.is_colliding(game_object_1):
                    game_object_1.on_collision(game_object_2)
                    game_object_2.on_collision(game_object_1)
        
    
