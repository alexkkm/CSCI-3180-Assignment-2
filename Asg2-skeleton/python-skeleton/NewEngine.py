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

from Map import Map
from Cell import Plain, Mountain, Swamp
from GameCharacter import Player, Goblin
from Trap import Trap
from Volcano import Volcano


class NewEngine:
    def __init__(self, data_file):
        self._data_file = data_file
        self._actors = []
        self._remove = []
        self._map = None
        self._player = None
        with open(data_file, "r") as fp:
            line = fp.readline()
            if not line:
                return None
            else:
                items = line.split()
                if len(items) != 7:
                    print("INVALID DATA FILE.")
                    return None
                num_of_row = int(items[0])
                num_of_col = int(items[1])
                p_ox = int(items[2])
                p_hp = int(items[3])
                num_of_goblins = int(items[4])
                num_of_traps = int(items[5])
                num_of_volcanoes = int(items[6])

            self._map = Map(num_of_row, num_of_col)

            # TODO: initialize each cell of the map object
            #       using the build_cell method

            # END TODO

            self._player = Player(num_of_row - 1, 0, p_hp, p_ox)

            # TODO: initilize the position of the player
            #       using the set_occupant and set_occupying method;
            #       add the player to _actors array

            for gno in range(num_of_goblins):
                # TODO: initilize each Goblin on the map
                #       using the set_occupant and set_occupying method;
                #       add each Goblin to _actors array

                # END TODO

            for tno in range(num_of_traps):
                # TODO: initilize each Trap on the map
                #       using the set_occupant and set_occupying method;

                # END TODO

            for vno in range(num_of_volcanoes):
                # TODO: initilize each Volcano of the map object
                #       using the build_cell method
                #       add each volcano to _actors array

                # END TODO

    def run(self):
        # main rountine of the game
        self.print_info()
        while not self.state():
            for obj in self._actors:
                if obj.active:
                    obj.act(self._map)
            self.print_info()
            self.clean_up()
        self.print_result()

    def clean_up(self):
        # TODO:

        # END TODO

        # check if the game ends and return if the player win or not.
    def state(self):
        # TODO:

        # END TODO

    def print_info(self):
        self._map.display()
        # TODO:

        # END TODO

    def print_result(self):
        if self.state() == 1:
            print('\033[1;33;41mCongrats! You win!\033[0;0m')
        if self.state() == -1:
            print('\033[1;33;41mBad Luck! You lose.\033[0;0m')
