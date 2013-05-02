# Implementation of a list-based queue.
#
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import linked_list as l

class Queue:

  def __init__(self):
    self.items = l.LinkedList()
    self.len = 0

  def enqueue(self, item):
    self.items.append(item)
    self.len += 1

  def dequeue(self):
    if not self.items.is_empty():
      self.len -= 1
      return self.items.pop()

  def peek(self):
    if not self.items.is_empty():
      return self.items.head.item

  def count(self):
    return self.len


