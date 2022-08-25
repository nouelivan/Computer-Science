# This program implements a max-heap.

from random import randrange
from max_heap import MaxHeap 

# An instance of MaxHeap
max_heap = MaxHeap()

# Populate max_heap with random numbers
random_nums = [randrange(1, 101) for n in range(6)]
for el in random_nums:
  max_heap.add(el)


# Test
print(max_heap.heap_list)
