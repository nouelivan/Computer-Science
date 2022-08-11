# This program produces the sum of all digits in a positive number as if they were each a single number.

def sum_digits(n):
  if n <= 9:
    return n
  num = n % 10
  return sum_digits(n // 10) + num

    


# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)
