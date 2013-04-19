# 4.6 Write an algorithm to find the 'next' node (i.e., in order-successor) of
# a given node in a binary search tree. You may assume that each node has a
# link to its parent.

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

t = bst.BinarySearchTree()
t.add(7)
t.add(3)
t.add(9)
t.add(1)
t.add(4)
t.add(8)
t.add(10)

      