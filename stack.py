# Implementation of an array-based stack.

class Stack:

  def __init__(self):
    self.len = 0
    self.elems = []

  def push(self, elem):
    self.elems.append(elem)
    self.len += 1

  def pop(self):
    if self.elems:
      self.len -= 1
      return self.elems.pop()

  def peek(self):
    return self.elems[-1]

  def count(self):
    return self.len

  def is_empty(self):
    return self.len == 0



