# This program simulates the Towers of Hanoi game.

from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Stack creation
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Game set up
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while(num_disks < 3):
  num_disks = int(input("\nEnter a number greater than or equal to 3.\n"))

for num in range(num_disks, 0, -1):
  left_stack.push(num)

num_optimal_moves = 2 ** num_disks - 1
print("The fastest you can solve this game is in {} moves.".format(num_optimal_moves))


# Get user input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while(True):
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {0} for {1}".format(letter, name))
    
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]



        
# The game is played.
num_user_moves = 0
while(stacks[2].get_size() != num_disks):
  print("\n\n\n...Current Stacks...")
  for i in stacks:
    i.print_items()
  while(True):
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again.")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again.")

print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))

 