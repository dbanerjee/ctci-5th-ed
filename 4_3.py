# Given a sorted (increasing order) array, write an algorithm to create a
# binary search tree with minimal height.

# Assumes the entire array is given beforehand and they are of size less than
# 100. If the numbers were streaming or the array was huge, then some form of
# balanced BST would be used.

import binary_search_tree as bst

def partition(elems):
  if not elems:
    return None

  mid = len(elems) / 2
  val = [elems[mid]]
  left = partition(elems[:mid])
  right = partition(elems[mid + 1:])
  if left:
    val.extend(left)
  if right:
    val.extend(right)
  return val

def build_bst(coll):

  t = bst.BinarySearchTree()
  
  elems = partition(coll)
  for e in elems:
    t.add(e)

  return t

def height(node):
  if not node:
    return False

  return 1 + max(height(node.left_child), height(node.right_child))


