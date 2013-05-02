# Solution to Exercise 3.5 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

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
