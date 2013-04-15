# How would you design an array which, in addition to push and pop, also has a
# function min which returns the minimum element? Push, pop, and min should all
# operate in O(1) time.

# Assumes numerical items

import unittest

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

s = MinStack()
s.push(5)
s.push(6)
s.push(7)
s.push(4)
s.push(4)
s.push(3)
s.push(2)
s.push(10)

class MinStackTest(unittest.TestCase):

  def test_min_stack(self):
    self.assertEqual(s.min(), 2)

    s.pop()
    self.assertEqual(s.min(), 2)

    s.pop()
    self.assertEqual(s.min(), 3)

    s.pop()
    self.assertEqual(s.min(), 4)

    s.pop()
    self.assertEqual(s.min(), 4)

    s.pop()
    self.assertEqual(s.min(), 5)

    s.pop()
    s.pop()
    self.assertEqual(s.min(), 5)

    self.assertEqual(s.mins, [[5, 0]])
    self.assertEqual(s.pop(), 5)
    self.assertEqual(s.mins, [])
    
if __name__ == '__main__':
  unittest.main()