# 4.8 You have two very large binary tree: T1, with millions of nodes, and T2,
# with hundreds of nodes. Create an algorithm to decide if T2 is a subtree of
# T1. A tree T2 is a subtree of T1 if there exists a node n in T1 such that the
# subtree of n is identical to T2. That is, if you cut off the tree at node n,
# the two trees would be identical.

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


t1 = bst.BinarySearchTree()
t2 = bst.BinarySearchTree()

t1.add(5)
t1.add(3)
t1.add(8)
t1.add(1)
t1.add(4)
t1.add(6)
t1.add(9)

t2.add(3)
t2.add(1)
t2.add(4)


