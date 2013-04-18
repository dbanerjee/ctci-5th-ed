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
