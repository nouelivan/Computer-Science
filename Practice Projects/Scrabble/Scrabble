# Will calculate the total point value of words used in a Scrabble game.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# List comprehension to create a dictionary with the above lists.
letter_to_points = {key:value for key, value in zip(letters, points)}

# Key:Value pair for blank tile added.
letter_to_points[" "] = 0

# Function that calculates the value of words.
def score_word(word):
  point_total = 0
  
  for letter in word:
    for key, value in letter_to_points.items():
      if letter == key:
        point_total += value
      else:
        point_total += 0
  
  return point_total

# Dictionary that maps players to words.
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNErd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"] }

# Empty dictionary
player_to_points = {}

# Loop that calculates the total number of points for each player, and adds this as the value for the player_to_words dictionary.
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_words[player] = player_points

print(player_to_words)
