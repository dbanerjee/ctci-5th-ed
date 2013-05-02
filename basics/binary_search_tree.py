# Implementation of a Binary Search Tree.
#
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

class Tree:

  def __init__(self, item, parent=None, left_child=None, right_child=None):
    self.item = item
    self.parent = parent
    self.left_child = left_child
    self.right_child = right_child

  def is_leaf(self):
    return self.left_child is None and self.right_child is None

  def is_left_child(self):
    return self.parent and self.parent.left_child is self

  def is_right_child(self):
    return self.parent and self.parent.right_child is self

  def has_both_children(self):
    return self.left_child and self.right_child


class BinarySearchTree:

  def __init__(self):
    self.root = None
    self.len = 0

  def add(self, item):
    if not self.root:
      self.root = Tree(item)
      self.len += 1
    else:
      cur_node = self.root
      done = False
      while not done:
        if item <= cur_node.item:
          if cur_node.left_child:
            cur_node = cur_node.left_child
          else:
            node = Tree(item, cur_node)
            cur_node.left_child = node
            self.len += 1
            done = True
        elif item > cur_node.item:
          if cur_node.right_child:
            cur_node = cur_node.right_child
          else:
            node = Tree(item, cur_node)
            cur_node.right_child = node
            self.len += 1
            done = True
        else:
          return None

  def contains(self, item):
    cur_node = self.root
    while cur_node:
      if cur_node.item is item:
        return True
      elif item < cur_node.item:
        cur_node = cur_node.left_child
      else:
        cur_node = cur_node.right_child

    return False

  def find_successor(self, node):
    cur_node = node
    while cur_node.left_child:
      cur_node = cur_node.left_child

    return cur_node

  def remove(self, item):
    if not self.root:
      return None

    cur_node = self.root
    while cur_node:
      if item < cur_node.item:
        cur_node = cur_node.left_child
      elif item > cur_node.item:
        cur_node = cur_node.right_child
      elif item is cur_node.item:
        if cur_node.is_leaf():
          if cur_node.is_left_child():
            cur_node.parent.left_child = None
          elif cur_node.is_right_child():
            cur_node.parent.right_child = None
          else:
            self.root = None
        elif cur_node.has_both_children():
          successor = self.find_successor(cur_node.right_child)
          cur_node.item = successor.item
          print successor.parent.item
          print successor.left_child
          print successor.right_child

          if successor.is_left_child():
            successor.parent.left_child = None
          else:
            if successor.is_leaf():
              successor.parent.right_child = None
            else:
              successor.parent.right_child = successor.right_child
        else:
          if cur_node.is_left_child():
            if cur_node.left_child:
              cur_node.parent.left_child = cur_node.left_child
            else:
              cur_node.parent.left_child = cur_node.right_child
          else:
            if cur_node.left_child:
              cur_node.parent.right_child = cur_node.left_child
            else:
              cur_node.parent.right_child = cur_node.right_child

        self.len -= 1
        return item

    return None

  def count(self):
    return self.len

  def clear(self):
    self.root = None

  def _inorder(self, cur_node):
    if cur_node:
      self._inorder(cur_node.left_child)
      print cur_node.item
      self._inorder(cur_node.right_child)

  def inorder(self):
    self._inorder(self.root)

  def _preorder(self, cur_node):
    if cur_node:
      print cur_node.item
      self._preorder(cur_node.left_child)
      self._preorder(cur_node.right_child)

  def preorder(self):
    self._preorder(self.root)

  def _postorder(self, cur_node):
    if cur_node:
      self._postorder(cur_node.left_child)
      self._postorder(cur_node.right_child)
      print cur_node.item

  def postorder(self):
    self._postorder(self.root)

  





    
