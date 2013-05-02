# Solution to Exercise 4.7 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

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
  