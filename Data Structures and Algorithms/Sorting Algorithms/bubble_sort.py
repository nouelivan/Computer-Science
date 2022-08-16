# This program sorts an array in ascending order.

nums = [5, 2, 9, 1, 5, 6]

def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp
  
# Define bubble_sort():
def bubble_sort(arr):
  for el in arr:
    for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
        swap(arr, i, i + 1)


# Test Sorting
print("Pre-Sort: {0}".format(nums))      
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))
