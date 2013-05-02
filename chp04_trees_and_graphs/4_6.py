# Solution to Exercise 4.6 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import binary_search_tree as bst

def find_successor(node):
  if not node:
    return None

  if node.right_child:
    if node.right_child.left_child:
      left = node.right_child.left_child
      while left.left_child:
        left = left.left_child
      return left
    else:
      return node.right_child
  else:
    if node.is_left_child():
      return node.parent
    else:
      parent = node.parent
      while parent:
        if parent.is_left_child():
          return parent.parent
        else:
          parent = parent.parent

      return None

      