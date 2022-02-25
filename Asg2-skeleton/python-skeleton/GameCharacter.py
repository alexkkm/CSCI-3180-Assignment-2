from tables import Col
from abc import abstractmethod
from Map import Map


class GameCharacter:
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._occupying = None
        self._name = None
        self._active = True
        self._character = None
        self._color = "\033[1;31m"

    # : name getter
    def getName(self):
        return self.name

    # : row getter

    def getRow(self):
        return self.row

    # : col getter

    def getCol(self):
        return self.col

    # : active getter and setter

    def getActive(self):
        return self.active

    def setActive(self, active):
        self.active = active

    # : occupying getter and setter

    def getOccupying(self):
        return self.occupying

    def setOccupying(self, cell):
        self.occupying = cell

    def cmd_to_pos(self, char):
        next_pos = [self._row, self._col]
        if char == "L":
            next_pos[1] -= 1
        elif char == "R":
            next_pos[1] += 1
        elif char == "U":
            next_pos[0] -= 1
        elif char == "D":
            next_pos[0] += 1
        else:
            print("Invalid Move.")
        return next_pos

    @abstractmethod
    def act(self, map):
        pass

    @abstractmethod
    def interact_with(self, comer):
        pass

    def display(self):
        # TODO: return _color followed by _character for displaying
        return
        # END TODO


class Player(GameCharacter):
    def __init__(self, row, col, hp=10, oxygen=10):
        GameCharacter.__init__(self, row, col)
        self._valid_actions = ["U", "D", "R", "L"]
        self._hp = hp
        self._oxygen = oxygen
        self._name = "Player"
        self._character = "A"

    # TODO: hp getter and setter

    # TODO: oxygen getter and setter

    def act(self, map):
        next_cell = None
        next_pos = [0, 0]
        while next_cell == None:
            action = input("Next move (U, D, R, L): ".format(
                self._row, self._col))
            # TODO: act method

            # END TODO

    # return whether comer entering the cell successfully or not
    def interact_with(self, comer):
        if comer.name == "Goblin":
            print(
                '\033[1;31;46mPlayer meets a Goblin! Player\'s HP - %d.\033[0m' % (comer.damage))
            # TODO: interact_with method

            # END TODO


class Goblin(GameCharacter):
    def __init__(self, row, col, actions):
        GameCharacter.__init__(self, row, col)
        self._actions = actions
        self._cur_act = 0
        self._damage = 1
        self._name = "Goblin"
        self._character = "G"

    # TODO: damage getter

    def act(self, map):
        # TODO: act method of a Goblin
        nextMove = self._actions[self._cur_act % len(self._actions)]
        nextPos = self.cmd_to_pos(nextMove)
        # TODO: DOING
        nextCell = map.

        # get the next cell according to _actions and _cur_act
        if:  # condition:
        print("\033[1;31;46mGoblin enters the cell (%d, %d).\033[0;0m" %
              (self._row, self._col))
        # END TODO

    # return whether comer entering the cell successfully or not
    def interact_with(self, comer):
        if comer.name == "Player":
            print(
                "\033[1;31;46mA goblin at cell (%d, %d) meets Player. The goblin died. Player's HP - 1.\033[0;0m"
                % (self._row, self._col)
            )
            # TODO: update properties of the player and the Goblin
            #       return whether the Player successfully enter the cell

            # END TODO
