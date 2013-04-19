# Implement a function to check if a binary tree is a binary search tree.

import binary_search_tree as bin
import sys

def _is_bst(node, min_val, max_val):
  if node is None:
    return True

  if node.item > min_val and\
     node.item < max_val and\
     _is_bst(node.left_child, min_val, node.item) and\
     _is_bst(node.right_child, node.item, max_val):
    return True
  else:
    return False

def is_bst(node):
  return _is_bst(node, -sys.maxint - 1,  sys.maxint)
 


