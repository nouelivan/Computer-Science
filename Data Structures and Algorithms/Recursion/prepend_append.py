# This program prepends and appends characters to string.

# Function wrap_string
def wrap_string(str, n):
  if n <= 0:
    return str
  str = "<" + str + ">"
  return wrap_string(str, n - 1)

# Test code
wrapped = wrap_string("Pearl", 3)
print(wrapped)
