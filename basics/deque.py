# Implementation of a Deque.
#
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import linked_list as l

class Deque:

  def __init__(self):
    self.deque = l.List()

  def enqueue_first(self, item):
    self.deque.add_tail(item)

  def dequeue_first(self):
    return self.deque.pop_tail()

  def enqueue_last(self, item):
    self.deque.add_head(item)

  def dequeue_last(self):
    return self.deque.pop_head()

  def peek_first(self):
    return self.deque.peek_tail()

  def peek_last(self):
    return self.deque.peek_head()

  def count(self):
    return self.deque.get_count()