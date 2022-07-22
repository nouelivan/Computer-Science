# This is a battleship game created using Python 2.

from random import randint

board = []
ships = []

# Board creation.
for x in range(5):
  board.append(["O"] * 5)

# Print board in visually appealing fasion.
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

# Ship row locations.
for i in range(3):
  ship_row = random_row(board)
  ship_col = random_col(board)
  ships.append([ship_row, ship_col])

# Test to see if any ships are on top of one another.
while True:
  if ships[0] == ships[1] or ships[0] == ships[2]:
    rand1 = random_row(board)
    rand2 = random_col(board)
    ships[0, 0] = rand1
    ships[0, 1] = rand2
  elif ships[1] == ships[2]:
    rand1 = random_row(board)
    rand2 = random_col(board)
    ships[1, 0] = rand1
    ships[1, 1] = rand2
  else:
    break

print ships[0]
print ships[1]
print ships[2]

# Game begins.
for turn in range(4):
  print "Current turn number is %s out of 4" % (turn + 1) 

  
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ships[0][0] and guess_col == ships[0][1]:
    print "Congratulations! You sunk my battleship!"
    break
  elif guess_row == ships[1][0] and guess_col == ships[1][1]:
    print "Congratulations! You sunk my battleship!"
    break
  elif guess_row == ships[2][0] and guess_col == ships[2][1]:
    print "Congratulations! You sunk my battleship!"
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    print_board(board)
  
  if turn == 3:
    print "Game Over"
  else:
    turn += 1
