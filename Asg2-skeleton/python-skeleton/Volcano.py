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

from Cell import Mountain


class Volcano(Mountain):
    def __init__(self, row, col, freq):
        Mountain.__init__(self, row, col)
        self._countdown = freq
        self._frequency = freq
        self._color = '\u001b[41m'
        self._active = True

    # TODO: _active getter

    def act(self, map):
        # TODO:

    if  # condition:
    print("\033[1;33;41mVolcano erupts! \033[0;0m")
    # add game logic
    # END TODO

    def display(self):
        # TODO: return a string representing the Volcano

        # END TODO
