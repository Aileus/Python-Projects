import random
import time

class TicTacToe():
    board = [" " for i in range(9)]
    boardguide = [ f'{i}' for i in range(9)]
    X_or_O = None
    
    def __init__(self):
        self.print_board(2)
        self.comp_moves()
##############################################################        
        
    def print_board(self,list_no):
        
        self.list_select = []
        if list_no == 1:
            self.list_select = self.board
            
        elif list_no == 2:
            self.list_select = self.boardguide
        
        for row in [self.list_select[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' | ')
            
        print('\n')
        
        self.play()
##############################################################        
    def my_moves(self):
        self.ending()
        
        try_move = int(input("Enter a valid space between 0-8: "))
        
        if try_move in [i for i, x in enumerate(self.board) if x == " "]:
            self.my_move = try_move
            TicTacToe.X_or_O = "X"
            self.update_board(self.my_move)
            
        elif try_move  not in [index for index, value in enumerate(self.board) if value == " "]:
            
            while try_move not in [index for index, value in enumerate(self.board) if value == " "]:
                try_move = int(input("Enter a space number that is unoccupied: "))
                for row in [self.boardguide[i*3:(i+1)*3] for i in range(3)]:
                    print(' | ' + ' | '.join(row) + ' | ')
                    
            self.my_move = try_move
            TicTacToe.X_or_O = "X"
            self.update_board(self.my_move)
            
                    
        
##############################################################        
    
    def comp_moves(self):
        
        self.comp_move = random.choice([i for i, x in enumerate(self.board) if x == " "])
        time.sleep(.6)
        TicTacToe.X_or_O = "O"
        self.update_board(self.comp_move)
        self.ending()
        
        
##############################################################        
    def update_board(self,move):
        
        self.ending()
        
        self.move = move
        if TicTacToe.X_or_O == "O":
            print("The computer moved to: ", move,'\n')
            
            if self.board[move] == " ":
                self.board[move] = TicTacToe.X_or_O
                self.print_board(1)
        
        elif TicTacToe.X_or_O == "X":
            print("You moved to: ", move,'\n')
            
            if self.board[move] == " ":
                self.board[move] = TicTacToe.X_or_O
                self.print_board(1)
        
##############################################################  
    def play(self):
        
        if TicTacToe.X_or_O == "O":
            self.my_moves()
        elif TicTacToe.X_or_O == "X":
            self.comp_moves()
            
##############################################################   

    def ending(self):
        
        if " " not in self.board:
            print("GAME OVER \n XYZ won the game")
            exit()
            print(self.board)
##############################################################        
    def winner(self):
        a = ["O" * 3]
        b = ["X" * 3]
        for row in [self.board[i*3,i+3] for i in range(3)] or         [self.board[i,i+6,3] for i in range(3)] :
            if row == a:
                print("Computer is the winner!!")
            elif row == b:
                print("You are the winner!!")
                
        

##############################################################        
TicTacToe() 