# Solution to Exercise 4.8 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import stack as s
import binary_search_tree as bst

def scan_trees(t1_node, t2_root):
  t1_stack = s.Stack()
  t1_stack.push(t1_node)
  
  t2_stack = s.Stack()
  t2_stack.push(t2_root)

  while not t1_stack.is_empty() or not t2_stack.is_empty():
    t1_cur_node = t1_stack.pop()
    t2_cur_node = t2_stack.pop()
    
    if not t1_cur_node or not t2_cur_node:
      return False

    if t1_cur_node.item is not t2_cur_node.item:
      return False

    if t1_cur_node.right_child:
      t1_stack.push(t1_cur_node.right_child)
    if t2_cur_node.right_child:
      t2_stack.push(t2_cur_node.right_child)

    if t1_cur_node.left_child:
      t1_stack.push(t1_cur_node.left_child)
    if t2_cur_node.left_child:
      t2_stack.push(t2_cur_node.left_child)

  return True

def is_subtree(t1, t2):
  if not t1.root or not t2.root:
    return False

  t1_stack = s.Stack()
  t1_stack.push(t1.root)
  while not t1_stack.is_empty():
    cur_node = t1_stack.pop()
    if cur_node.item is t2.root.item:
      if scan_trees(cur_node, t2.root):
        return True

    if cur_node.right_child:
      t1_stack.push(cur_node.right_child)
    if cur_node.left_child:
      t1_stack.push(cur_node.left_child)

  return False
