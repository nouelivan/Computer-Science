# This program moves items to the end of a list based on its value.

def move_to_end(lst, val):
  result = []

  if lst == []:
    return []
  
  if lst[0] == val:
    result += move_to_end(lst[1:], val)
    result.append(lst[0])
  else:
    result.append(lst[0])
    result += move_to_end(lst[1:], val)
  
  return result

# Test code
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))
