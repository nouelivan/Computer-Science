# This program counts matching patterns in a string.

# Pattern searching function.
def pattern_search(text, pattern):
  print("Input Text:", text, "Input Pattern:", pattern)
  for index in range(len(text)):
    print("Text Index:", index)
    match_count = 0
    for char in range(len(pattern)):
      print("Pattern Index:", char)
      try:
        if pattern[char] == text[index + char]:
          match_count += 1
        else:
          break
      except IndexError:
        break
    if match_count == len(pattern):
      print("{0} found at index {1}".format(pattern, index))

# Test Cases
text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLEN"
pattern = "NEEDLE"
pattern_search(text, pattern)

text2 = "SOMEMORERANDOMWORDSTOpatternSEARCHTHROUGH"
pattern2 = "pattern"
pattern_search(text2, pattern2)

text4 = "722615457824612704202682179992552072047396"
pattern4 = "42"
pattern_search(text4, pattern4)
