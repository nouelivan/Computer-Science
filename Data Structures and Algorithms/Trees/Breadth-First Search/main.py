# This program finds a file/folder within a directory.

from tree import TreeNode
from bfs import bfs

# Tree creation.
sample_root_node = TreeNode("Home")
docs = TreeNode("Documents")
photos = TreeNode("Photos")
sample_root_node.children = [docs, photos]
my_wish = TreeNode("WishList.txt")
my_todo = TreeNode("TodoList.txt")
my_cat = TreeNode("Fluffy.jpg")
my_dog = TreeNode("Spot.jpg")
docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]

# File path is printed to show its structure.
print(sample_root_node)

# The file/folder is searched.
goal_path = bfs(sample_root_node, "Fluffy.jpg")
if goal_path is None:
  print("No path found")
else:
  print("Path found")
  for node in goal_path:
    print(node.value)
