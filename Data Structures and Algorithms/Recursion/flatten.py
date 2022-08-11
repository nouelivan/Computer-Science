# This program removes nested lists within a list.

# Flatten funtion
def flatten(my_list):
  result = []
  for element in my_list:
    if isinstance(element, list):
      print("list found!")
      flat_list = el
      result += flat_list
    else:
      result.append(element)
  return result


# List to test
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))
