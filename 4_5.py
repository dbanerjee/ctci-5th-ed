# Implement a function to check if a binary tree is a binary search tree.

import binary_search_tree as bin

def is_bst(cur_node):
  if not cur_node or cur_node.is_leaf():
    return True

  is_valid = False
  if cur_node.has_both_children():
    if cur_node.left_child.item < cur_node.item and\
       cur_node.right_child.item > cur_node.item:
      is_valid = True
  elif cur_node.left_child and cur_node.left_child.item < cur_node.item:
    is_valid = True
  elif cur_node.right_child and cur_node.right_child.item > cur_node.item:
    is_valid = True


  return is_valid and\
         is_bst(cur_node.left_child) and\
         is_bst(cur_node.right_child)
