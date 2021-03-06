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


class GameCharacter:
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._occupying = None
        self._name = None
        self._active = True
        self._character = None
        self._color = "\033[1;31m"

    # name getter
    def get_name(self):
        return self.name

    # row getter

    def get_row(self):
        return self.row

    # col getter

    def get_col(self):
        return self.col

    # active getter and setter

    def get_active(self):
        return self.active

    def set_active(self, active):
        self.active = active

    # occupying getter and setter

    def get_occupying(self):
        return self.occupying

    def set_occupying(self, cell):
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
        # return _color followed by _character for displaying
        return self._color+self._character
        # END


class Player(GameCharacter):
    def __init__(self, row, col, hp=10, oxygen=10):
        GameCharacter.__init__(self, row, col)
        self._valid_actions = ["U", "D", "R", "L"]
        self._hp = hp
        self._oxygen = oxygen
        self._name = "Player"
        self._character = "A"

    #  hp getter and setter
    def get_hp(self):
        return self.hp

    def set_hp(self, h):
        self.hp = h

    #  oxygen getter and setter
    def get_oxygen(self):
        return self.oxygen

    def set_oxygen(self, o):
        self.oxygen = o

    def act(self, map):
        next_cell = None
        next_pos = [0, 0]
        while next_cell == None:
            while correct_act == false:
                action = input("Next move (U, D, R, L): ".format(
                    self._row, self._col))
                next_act = action[0]
                # act method
                for i in range(0, len(self._valid_actions)):
                    if self._valid_actions[i] == next_act:
                        correct_act = true
                        break
                if(len(action) > 1):
                    correct_act = false
                if not(correct_act):
                    print(
                        "Invalid command. Please enter one of {U, D, R, L}.%n")
                else:
                    next_pos = self.cmd_to_pos(next_act)

            next_cell = map.get_cell(next_pos[0], next_pos[1])
            if(next_cell != null and next_cell.set_occupant(self)):
                self._row = next_pos[0]
                self._col = next_pos[1]
                self._oxygen -= self._occupying.get_hours(self)

                self._occupying.remove_occupant()
                self.set_occupying(next_cell)
            else:
                next_cell = null
            # END

    # return whether comer entering the cell successfully or not
    def interact_with(self, comer):
        if comer.name == "Goblin":
            print(
                '\033[1;31;46mPlayer meets a Goblin! Player\'s HP - %d.\033[0m' % (comer.damage))
            # interact_with method
            self.hp = self.hp-comer.getDamage()
            return false
        else:
            return false
            # END


class Goblin(GameCharacter):
    def __init__(self, row, col, actions):
        GameCharacter.__init__(self, row, col)
        self._actions = actions
        self._cur_act = 0
        self._damage = 1
        self._name = "Goblin"
        self._character = "G"

    # damage getter
    def get_damage(self):
        return self.damage

    def act(self, map):
        # act method of a Goblin
        nextMove = self._actions[self._cur_act % len(self._actions)]
        nextPos = self.cmd_to_pos(nextMove)
        nextCell = map.get_cell(nextPos[0], nextPos[1])

        # get the next cell according to _actions and _cur_act
        if (nextCell != null and nextCell.set_occupant(self)):  # condition:
            self._cur_act += 1
            self._row = nextPos[0]
            self._col = nextPos[1]
            self.occupying.remove_occupant()
            self.set_occupying(nextCell)
            print("\033[1;31;46mGoblin enters the cell (%d, %d).\033[0;0m" %
                  (self._row, self._col))
        # END

    # return whether comer entering the cell successfully or not
    def interact_with(self, comer):
        if comer.name == "Player":
            print(
                "\033[1;31;46mA goblin at cell (%d, %d) meets Player. The goblin died. Player's HP - 1.\033[0;0m"
                % (self._row, self._col)
            )
            # update properties of the player and the Goblin
            #       return whether the Player successfully enter the cell
            comer.set_hp(comer.get_hp-self._damage)
            self.set_active(false)
            return true
        return false
        # END
