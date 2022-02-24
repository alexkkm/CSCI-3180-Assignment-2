from abc import abstractmethod
from sqlalchemy import null, true

from GameCharacter import GameCharacter


class Cell:
    def __init__(self, row=0, col=0):
        self._row = row
        self._col = col
        self._occupant = None
        self._color = None
        self._hours = 0

    # TODO: hours getter

    def set_occupant(self, obj):
        # TODO: set occupant for the Plain cell
        #       return whether success or not
        if self.occupant() == null:
            self._occupant = obj
            return true
        else:
            if isinstance(self.occupant(), GameCharacter):
                if GameCharacter.interact_with(obj)

        # END TODO

    def remove_occupant(self):
        # TODO: remove the occupant
        self._occupant = null
        # END TODO

    @property
    def occupant(self):
        return self._occupant

    def display(self):
        # TODO: print a string to display the cell
        #       and the occupant in the cell

        # END TODO


class Plain(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = '\033[1;32;42m'
        self._hours = 1


class Mountain(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = '\033[1;37;47m'

    def set_occupant(self, obj):
        # TODO: return False

        # END TODO


class Swamp(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = '\033[1;34;44m'
        self._hours = 2
