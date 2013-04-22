# 4.1 Implement a function to check if a binary tree is balanced. For the
# purposes of this question, a balanced tree is defined to be a tree such that
# the heights of the two subtrees of any node never differ by more than one.

def height(node):
  if not node:
    return False

  return 1 + max(height(node.left_child), height(node.right_child))

def is_balanced(node):
  if not node:
    return True

  left = height(node.left_child)
  right = height(node.right_child)

  if abs(left - right) <= 1 and\
     is_balanced(node.left_child) and\
     is_balanced(node.right_child):
    return True

  return False



