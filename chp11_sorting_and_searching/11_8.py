# Solution to Exercise 11.8 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi.

class Node:

  def __init__(self, num):
    self.num = num
    self.left_child = None
    self.right_child = None
    self.left_tree_size = 0

  def is_leaf(self):
    return not self.left_child and not self.right_child

class RankingTree:

  def __init__(self):
    self.root = None

  def track(self, num):
    node = Node(num)

    if not self.root:
      self.root = node
    else:
      cur_node = self.root
      while True:
        if num <= cur_node.num:
          cur_node.left_tree_size += 1
          if not cur_node.left_child:
            cur_node.left_child = node
            break
          cur_node = cur_node.left_child        
        else:
          if not cur_node.right_child:
            cur_node.right_child = node
            break
          cur_node = cur_node.right_child        

    return self.root.left_tree_size

  def rank_of(self, num):
    cur_node = self.root
    rank = 0
    while cur_node:
      if cur_node.num is num:
        return rank + cur_node.left_tree_size
      elif num < cur_node.num:
        cur_node = cur_node.left_child
      else:
        rank += (1 + cur_node.left_tree_size)
        cur_node = cur_node.right_child

    return None

 
