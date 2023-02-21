class GameState:
    def __init__(self):
        self.__score = 0

    def add_to_score(self, value : int):
        self.__score += value

    @property
    def score(self):
        return self.__score
        
