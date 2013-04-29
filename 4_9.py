# 4.9 You are given a Binary Tree in which each node contains a value. Design
# an algorithm to print all paths which sum to a given value. Note that a path
# can start or end anywhere in the tree.

import binary_search_tree as bst

def path_sum(node, target, cur_sum=0, nodes=[]):
  if not node:
    return None

  cur_nodes = nodes
  cur_nodes = nodes + [node]
  cur_sum += node.item

  if cur_sum is target:
    items = []
    for n in cur_nodes:
      items.append(n.item)
    print items

  path_sum(node.left_child, target, cur_sum, cur_nodes)
  path_sum(node.right_child, target, cur_sum, cur_nodes)

t = bst.BinarySearchTree()
t.add(5)
t.add(3)
t.add(7)
t.add(-3)
t.add(4)
t.add(6)
t.add(8)
t.add(3)
