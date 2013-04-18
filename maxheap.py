# Implementation of max binary heap.

import unittest

class MaxHeap:

  def __init__(self):
    self.elems = []
    self.len = 0

  def perc_down(self, idx):
    i = idx + 1
    if i > self.len:
      return None

    done = False
    while not done:
      left = i * 2
      right = i * 2 + 1
      largest = i
      
      if left <= self.len and self.elems[left - 1] > self.elems[largest - 1]:
        largest = left
      
      if right <= self.len and self.elems[right - 1] > self.elems[largest - 1]:
        largest = right
      
      if largest is not i:
        tmp = self.elems[i - 1]
        self.elems[i - 1] = self.elems[largest - 1]
        self.elems[largest - 1] = tmp
        i = largest
      else:
        done = True

  def perc_up(self, idx):
    i = idx + 1
    if idx > self.len:
      return None
    
    parent = i / 2
    while parent is not 0:
      if self.elems[parent - 1] < self.elems[i - 1]:
        tmp = self.elems[parent - 1]
        self.elems[parent - 1] = self.elems[i - 1]
        self.elems[i - 1] = tmp
        i = parent
        parent /= 2
      else:
        return None

  def remove(self):
    if self.elems:
      item = self.elems[0]
      last = self.elems.pop()
      if self.elems:
        self.elems[0] = last
      self.len -= 1
      self.perc_down(0)
      return item

  def add(self, item):
    self.elems.append(item)
    self.len += 1
    self.perc_up(self.len - 1)

  def peek(self):
    if self.elems:
      return self.elems[0]

  def count(self):
    return self.len

  def clear(self):
    self.elems = []
    self.len = 0

