#TIC TAC TOE game by Vaibhav Sharma
def display_board(board):
    print(" "+board[7]+"|"+board[8]+"|"+board[9])
    print(" ------") 
    print(" "+board[4]+"|"+board[5]+"|"+board[6])
    print(" ------") 
    print(" "+board[1]+"|"+board[2]+"|"+board[3])
def player_input():
    marker=" "
    while marker!="X" and marker!="O":
        marker=input("Player 1 choose X or O :").upper()
    if marker=="X":
        return("X","O")
    else:
        return("O","X")
def place_marker(board,position,marker):
    board[position]=marker
def win_check(board,marker):
    return((board[1]==board[2]==board[3]==marker)or(board[4]==board[5]==board[6]==marker)or(board[7]==board[8]==board[9]==marker)
           or(board[7]==board[4]==board[1]==marker)or(board[8]==board[5]==board[2]==marker)
           or(board[9]==board[6]==board[3]==marker)or(board[1]==board[5]==board[9]==marker)or(board[7]==board[5]==board[3]==marker))

import random
def choose_first():
    flip=random.randint(0,1)
    if flip==1:
        return "Player 1"
    else:
        return "Player 2"
def space_check(board,position):
    return board[position]==" "
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Choose a position from 1 to 9 : "))
    return position
def replay():
    choice=input("Do U wanna play again ,Chosse Yes or No:- ")
    return choice=="Yes"
print("Welcome to Tic tac toe by:Vaibhav Sharma :) ")
board=[" "]*10
player_1,player_2=player_input()
turn=choose_first()
print(turn +" Will go first")
play_game=input("Ready to play the game : Y or N :- ").upper()
if play_game=="Y":
    game_on=True
else:
    game_on=False
while game_on:
    if turn=="Player 1":
        display_board(board)
        position=player_choice(board)
        place_marker(board,position,player_1)
        if win_check(board,player_1):
            display_board(board)
            print("Player 1 won the game")
            game_on=False
        else:
            if full_board_check(board):
                display_board(board)
                print("It's a Tie Game")
                game_on=False
            else:
                turn="Player 2"
    else:
        display_board(board)
        position=player_choice(board)
        place_marker(board,position,player_2)
        if win_check(board,player_2):
            display_board(board)
            print("Player 2 won the game")
            game_on=False
        else:
            if full_board_check(board):
                display_board(board)
                print("It's a Tie Game")
                game_on=False
            else:
                turn="Player 01"
        
