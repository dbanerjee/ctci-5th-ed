# 11.8 Imagine you are reading in a stream of integers. Periodically, you wish
# to be able to look up the rank of a number X (the number of values less than
# or equal to x). Implement the data structures and algorithms to support these
# operations. That is, implement the method track(int x), which is called when
# each number is generated, and the method getRankOfNumber(int x), which returns
# the number of values less than or equal to x (not including x itself).
# Example:
# Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
# getRankOfNumber(1) = 0
# getRankOfNumber(3) = 1
# getRankOfNumber(4) = 3

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

 
