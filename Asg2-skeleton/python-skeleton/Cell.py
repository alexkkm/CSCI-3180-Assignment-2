'''
/∗
 ∗ CSCI3180 Principles of Programming Languages
 ∗
 ∗ --- Declaration --- ∗
 ∗ I declare that the assignment here submitted is original except for source
 ∗ material explicitly acknowledged. I also acknowledge that I am aware of
 ∗ University policy and regulations on honesty in academic work, and of the
 ∗ disciplinary guidelines and procedures applicable to breaches of such policy
 ∗ and regulations, as contained in the website
 ∗ http://www.cuhk.edu.hk/policy/academichonesty/ ∗
 ∗ Assignment 2
 ∗ Name : Kong Kwai Man
 ∗ Student ID : 1155125979
 ∗ Email Addr : kmkong9@cse.cuhk.edu.hk
 ∗/
 '''

from abc import abstractmethod
from sqlalchemy import false, null, true

from GameCharacter import GameCharacter
from Trap import Trap


class Cell:
    def __init__(self, row=0, col=0):
        self._row = row
        self._col = col
        self._occupant = None
        self._color = None
        self._hours = 0

    # hours getter
    def get_hours(self):
        return self._hours

    def set_occupant(self, obj):
        # set occupant for the Plain cell
        #      return whether success or not
        if self.occupant() == null:
            self._occupant = obj
            return true
        else:
            if isinstance(self.occupant, GameCharacter):
                if GameCharacter.interact_with(obj):
                    self.occupant = obj
                    return true
                else:
                    return false
            else:
                return false
        # END

    def remove_occupant(self):
        # remove the occupant
        self._occupant = null
        # END

    @property
    def occupant(self):
        return self._occupant

    def display(self):
        # print a string to display the cell
        #       and the occupant in the cell
        if self.occupant != null:
            if isinstance(self.occupant, GameCharacter):
                print("%s %s%s \033[0m   " % (self.color, (
                    GameCharacter.occupant).display(), self.color))
            else:
                if isinstance(self.occupant, Trap):
                    print("%s %s%s \033[0m   " % (self.color,
                                                  (Trap.occupant).display(), self.color))
        else:
            print("%s   \033[0m   " % self.color)
        # END


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
        # return false
        return false
        # END


class Swamp(Cell):
    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self._color = '\033[1;34;44m'
        self._hours = 2
