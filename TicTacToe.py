"""
 - Extension: Computer player (start off with a random player, move towards a good AI) (min/max AI)
 - Aesthetics (optional)
"""
import os
import random

board1 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

def print_board(board):
  print("\n{} {} {}".format(*board[0]))
  print("{} {} {}".format(*board[1]))
  print("{} {} {}".format(*board[2]))

def IndexForBoard(user_input):
  for i in range(len(board1)):
    if user_input in board1[i]:
      return (i, board1[i].index(user_input))

def winOrlose (board):

  #check both diagonals
  diag1 = [board[0][0], board[1][1], board[2][2]]
  diag2 = [board[0][2], board[1][1], board[2][0]]

  diag1 = ''.join(diag1)
  diag2 = ''.join(diag2)

  if 'XXX' == diag1 or 'OOO' == diag1:
    return True, diag1[0]

  if 'XXX' == diag2 or 'OOO' == diag2:
    return True, diag2[0]

  #check all columns
  for i in range(3):
    col = [board[0][i], board[1][i], board[2][i]]
    col = ''.join(col)
    if 'XXX' == col or 'OOO' == col:
      return True, col[0]

  #check all rows
  for i in range (len(board)):
    row = ''.join(board[i])
    if 'XXX' == row or 'OOO' == row:
      return True, row[0]

  #check if board is not full
  for i in range(3):
    if '_' in board[i]:
      return False, '_'

  return True, '_'


def get_valid_input(player, board):

  markers = ('X', 'O')
  # markers[player-1]

  while True:
    user_input = input('\nPlayer {}: Where would you like to place your {} out of all the letters on the board: '.format(player, markers[player-1]))
    if len(user_input) == 1 and user_input in 'abcdefghi':
      #move is on the board
      move_index = IndexForBoard(user_input)
      if board[move_index[0]][move_index[1]] == '_':
        return user_input
    print("Invalid Input, please retry.")
  
def get_computer_move(board):
  valid = False
  while valid == False:
    computer_move = random.choice(['a','b','c','d','e','f','g','h','i'])
    print(computer_move)
    move_index = IndexForBoard(computer_move)
    if board[move_index[0]][move_index[1]] == '_':
      return computer_move

def main():

  player2 = input('Would you like player 2 to be a human or AI? (h/c)')
  
  board2 = [['_','_','_'],['_','_','_'],['_','_','_']]

  game_over = False
  print_board(board1)
  player_tokens = ['X', 'O']
  current_player = 0
    

  while not game_over:

    if player2 == 'c' and current_player == 1:
      player_input = get_computer_move(board2)
    else:
      player_input = get_valid_input(current_player+1, board2)

    index_player = IndexForBoard(player_input)

    board2[index_player[0]][index_player[1]] = player_tokens[current_player]
    
    game_over, winner = winOrlose(board2)

    os.system('clear')

    print_board(board2)
    print_board(board1)

    current_player = (current_player + 1) % 2
    
  if winner == '_':
    print("The game has ended in a tie.")
  elif winner == 'X':
    print("Congratulations, you are the winner of the game, player 1.")
  else: 
    print("Congratulations, you are the winner of the game player 2.")


play_again = True

while play_again:

  main()

  play_again = input("\nWould you like to play again? (Y/N) ") == 'Y'

