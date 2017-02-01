from case import Case

class Board:

    def __init__(self, x, y):
        """
            Creates an empty world with primitive cases
        """
        self.world = [[Case(0) for a in range(x)] for b in range(y)]

