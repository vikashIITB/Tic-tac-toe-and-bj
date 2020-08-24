from IPython.display import clear_output

def display_board(board):
    
    
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
   
    print('-----------')
    
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
   
    print('-----------')
    
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
   
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

 def place_marker(board, marker, position):
    
    board[position]=marker
    
def win_check(board, mark):
    mylist1=[1,2,3]
    mylist2=[4,5,6]
    mylist3=[7,8,9]
    mylist4=[1,4,7]
    mylist5=[2,5,8]
    mylist6=[3,6,9]
    mylist7=[1,5,9]
    mylist8=[3,5,7]
    megalist=[mylist1,mylist2,mylist3,mylist4,mylist5,mylist6,mylist7,mylist8]
    for item in megalist:
        if board[item[0]]==board[item[1]]==board[item[2]]==mark:
        
            return True
        else:
            
            continue
            
    return False   

import random

def choose_first():
    a=random.randint(0,1)
    if a==0:
        print('Player 1 goes first')
        return '1'
    else:
        print('Player 2 goes first') 
        return '2'

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    a=input('Do you want to play again (YES/NO)')
    return a.upper()=='YES'

print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    theboard=[' ']*10
    playerdata=player_input()
    player1=playerdata[0]
    player2=playerdata[1]
    turn=choose_first()

    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        
        if turn=='1':
            
            display_board(theboard)
            print("player 1's turn")
            position=player_choice(theboard)
            place_marker(theboard,player1,position)
            if win_check(theboard,player1):
                print('Congratulations! Player 1 have won the game!')
                game_on=False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = '2'
                    
        
        else:
            display_board(theboard)
            print("player 2's turn")
            position = player_choice(theboard)
            place_marker(theboard, player2,position)
            if win_check(theboard,player2):
                print('Congratulations! player 2 have won the game!')
                gane_on=False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = '1'
                    
    if not replay():
         break
           
            
            
        
                                