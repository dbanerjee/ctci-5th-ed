# Solution to Exercise 4.4 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import binary_search_tree as bst
import linked_list as ll

def collect_nodes(cur_node, d, height):
  if cur_node:
    collect_nodes(cur_node.left_child, d, height + 1)
    collect_nodes(cur_node.right_child, d, height + 1)
    if height in d:
      d[height].add(cur_node)
    else:
      d[height] = ll.LinkedList()
      d[height].add(cur_node)

def gen_node_list(t):
  d = {}
  collect_nodes(t.root, d, 0)
  return d

