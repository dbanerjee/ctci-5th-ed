# Implement a MyQueue class which implements a queue using two stacks.

import unittest

class MyQueue:

  def __init__(self):
    self.inbox= []
    self.outbox = []
    self.len = 0

  def enqueue(self, item):
    self.inbox.append(item)
    self.len += 1

  def dequeue(self):
    if self.outbox:
      self.len -= 1
      return self.outbox.pop()
    elif self.inbox:
      while self.inbox:
        self.outbox.append(self.inbox.pop())
      self.len -= 1
      return self.outbox.pop()

  def count(self):
    return self.len

q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

class MyQueueTest(unittest.TestCase):

  def test_my_queue(self):
    self.assertEqual(q.dequeue(), 1)
    self.assertEqual(q.dequeue(), 2)

    q.enqueue(4)
    q.enqueue(5)
    self.assertEqual(q.dequeue(), 3)
    self.assertEqual(q.dequeue(), 4)

    self.assertEqual(q.count(), 1)

if __name__ == '__main__':
  unittest.main()
