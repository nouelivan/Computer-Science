# This program returns the product of two numbers without using the multiplication operator.

def multiplication(num_1, num_2):
  num_2 -= 1
  if num_2 == 0:
    return num_1
  return multiplication(num_1, num_2) + num_1




# test cases
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)
