# Solution to Exercise 4.9 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import binary_search_tree as bst

def path_sum(node, target, cur_sum=0, nodes=[]):
  if not node:
    return None

  cur_nodes = nodes + [node]
  cur_sum += node.item

  if cur_sum is target:
    items = []
    for n in cur_nodes:
      items.append(n.item)
    print items

  path_sum(node.left_child, target, cur_sum, cur_nodes)
  path_sum(node.right_child, target, cur_sum, cur_nodes)

