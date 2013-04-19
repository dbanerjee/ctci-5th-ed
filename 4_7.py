# 4.7 Design an algorithm and write code to find the first common ancestor of
# two nodes in a binary tree. Avoid storing additional nodes in a data
# structure. Note: This is not necessarily a binary search tree.

import binary_search_tree as bst

def node_height(node):
  if not node:
    return None

  height = 0
  cur_node = node
  while cur_node:
    cur_node = cur_node.parent
    height += 1
  return height

def lowest_common_ancestor(a, b):
  if not a or not b:
    return None

  a_height = node_height(a)
  b_height = node_height(b)
  
  while a_height > b_height:
    a = a.parent
    a_height -= 1
  
  while b_height > a_height:
    b = b.parent
    b_height -= 1
  
  while a is not b:
    a = a.parent
    b = b.parent
  
  return a

t = bst.BinarySearchTree()
t.add(40)
t.add(20)
t.add(80)
t.add(10)
t.add(30)
t.add(60)
t.add(100)
t.add(5)
t.add(15)
t.add(25)
t.add(35)
t.add(1)

