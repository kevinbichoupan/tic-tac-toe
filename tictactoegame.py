# Create Class for Board

class Board:
    def __init__(self):
        self.board = [['-', '1', '2', '3'], ['a', ' ', ' ' , ' '], ['b', ' ', ' ' , ' '], ['c', ' ', ' ' , ' ']]
        self.board_finished = False
    
    def update(self, player, coordinate):
        y_coordinate = int(coordinate[1])
        x_coordinate = coordinate[0]
        if x_coordinate == 'a': 
            x_coordinate = 1
        elif x_coordinate == 'b':
            x_coordinate = 2
        elif x_coordinate == 'c':
            x_coordinate = 3
        
        self.board[x_coordinate][y_coordinate] = player
    
    def check_if_finished(self):
        if ((self.board[1][1] == self.board[1][2] == self.board[1][3] != ' ') or
            (self.board[2][1] == self.board[2][2] == self.board[2][3] != ' ') or
            (self.board[3][1] == self.board[3][2] == self.board[3][3] != ' ') or
            
            (self.board[1][1] == self.board[2][1] == self.board[3][1] != ' ') or
            (self.board[1][2] == self.board[2][2] == self.board[3][2] != ' ') or
            (self.board[1][3] == self.board[2][3] == self.board[3][3] != ' ') or
            
            (self.board[1][1] == self.board[2][2] == self.board[3][3] != ' ') or
            (self.board[1][3] == self.board[2][2] == self.board[3][1] != ' ')):
            self.board_finished = True
        for i in self.board:
            for j in i:
                if j = ' ':
                    return
                
                
                # I NEED TO CHECK WHERE THE BOARD IF COMPLETELY FULL