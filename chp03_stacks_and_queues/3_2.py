# Solution to Exercise 3.2 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

class MinStack:

  def __init__(self):
    self.items = []
    self.len = 0
    self.mins = []

  def push(self, item):
    self.items.append(item)
    self.len += 1

    if self.mins:
      cur_min = self.mins[-1][0]
      if item < cur_min:
        self.mins.append([item, 0])
      else:
        self.mins[-1][1] += 1
    else:
      self.mins.append([item, 0])

  def pop(self):
    if not self.items:
      return None

    item = self.items.pop()
    self.len -= 1

    cur_min_count = self.mins[-1][1]
    if cur_min_count is 0:
      self.mins.pop()
    else:
      self.mins[-1][1] -= 1

    return item

  def min(self):
    if self.items:
      return self.mins[-1][0]

  def count(self):
    return self.len
