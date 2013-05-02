# Implementation of an array-based Binary Tree.
#
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

class BinaryTree:

  def __init__(self):
    self.elems = []
    self.len = 0

  def add(self, elem):
    self.elems.append(elem)
    self.len += 1

  def remove(self, elem):
    if self.elems:
      idx = 0
      for e in self.elems:
        if e is elem:
          item = e
          self.elems[idx] = self.elems[-1]
          self.elems.pop()
          self.len -= 1
          return item
        else:
          idx += 1

  def clear(self):
    self.elems = []
    self.len = 0

  def count(self):
    return self.len

  def preorder(self, root = 1):
    if root > self.len:
      return None
    else:
      print self.elems[root - 1]

    if root * 2 <= self.len:
      self.preorder(root * 2)

    if root * 2 + 1 <= self.len:
      self.preorder(root * 2 + 1)

  def inorder(self, root = 1):
    if root * 2 <= self.len:
      self.inorder(root * 2)

    if root > self.len:
      return None
    else:
      print self.elems[root - 1]

    if root * 2 + 1 <= self.len:
      self.inorder(root * 2 + 1)

  def postorder(self, root = 1):
    if root * 2 <= self.len:
      self.postorder(root * 2)

    if root * 2 + 1 <= self.len:
      self.postorder(root * 2 + 1)

    if root > self.len:
      return None
    else:
      print self.elems[root - 1]

    


