from xml.etree import ElementInclude
from Cell import Cell


class Map:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._cells = [[Cell() for x in range(cols)] for y in range(rows)]
    
    #TODO: rows getter
    
    #TODO: cols getter
    
    def get_cell(self, row, col):
        #TODO: 
        if # condition
            print("\033[1;31;46mNext move is out of boundary!\033[0;0m")
            return None 
        else:
            # return a cell 
        # END TODO 

    def build_cell(self, row, col, cell):
        #TODO:
        if # condition
            print("\033[1;31;46mThe position (%d, %d) is out of boundary!\033[0;0m" %(row, col))
            return False 
        else:
            # return a cell 
        # END TODO

    def get_neighbours(self, row, col):
        return_cells = []
        # TODO: 

        # END TODO
        

    def display(self):
        # TODO: 

        # END TODO
