import pygame
import inspect

class GameController:
    def __init__(self) -> None:
        self.__quit_game = False
        self.input_mappings = {}
        self.event_mappings = {}

        self.initialize()

    def initialize(self):
        self.initialize_events()
        self.initialize_mappings()

    def initialize_events(self):
        self.add_event_mapping(pygame.KEYDOWN, self.process_key_event)
        self.add_event_mapping(pygame.QUIT, self.quit_game)

    def initialize_mappings(self):
        self.add_input_mapping(pygame.K_ESCAPE, self.quit_game)

    def add_input_mapping(self, key, action, *args):
        self.input_mappings[key] = (action, args)

    def add_event_mapping(self, key, action):
        self.event_mappings[key] = action

    def quit_game(self):
        self.__quit_game = True

    def process_key_event(self, event):
        if event.key not in self.input_mappings.keys():
            return

        tp = self.input_mappings[event.key]
        if tp[1]:
            tp[0](*tp[1])
        else:
            tp[0]()
            
    def process_event(self, event):
        if event.type not in self.event_mappings.keys():
            return

        action = self.event_mappings[event.type]        
        argspec = inspect.getargspec(action)
        if argspec and len(argspec[0]) == 2:
            action(event)
        else:
            action()

    @property
    def is_quitting(self):
        return self.__quit_game
