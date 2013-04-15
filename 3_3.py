# Imagine a (literal) stack of plates. If the stack gets too high, it might
# topple. Therefore, in real life, we would likely start a new stack when the
# previous stack exceeds some threshold. Implement a data structure called
# SetOfStacks that mimics this. SetOfStacks should be composed of several stacks
# and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetofStacks.pop() should behave identically to a single
# stack (that is, pop() should return the same values as it would if there were
# just a single stack).

# Follow-up: Implement a function popAt(index) which performs a pop operation on
# a specific sub-stack.

import unittest

class SetOfStacks:

  def __init__(self, sub_stack_size):
    self.sub_stack_size = sub_stack_size
    self.num_of_sub_stacks = 0
    self.cur_sub_stack_len = 0
    self.stacks = []

  def push(self, item):
    if not self.stacks or self.cur_sub_stack_len is self.sub_stack_size:
      self.stacks.append([item])
      self.num_of_sub_stacks += 1
      self.cur_sub_stack_len = 0
    else:
      self.stacks[-1].append(item)

    self.cur_sub_stack_len += 1

  def pop(self):
    if not self.stacks:
      return None

    item = self.stacks[-1].pop()
    if self.stacks[-1]:
      self.cur_sub_stack_len -= 1
    else:

      # This deals with cases where pop_at may have completely emptied an
      # earlier stack.
      while self.num_of_sub_stacks is not 0 and not self.stacks[-1]:
        self.stacks.pop()
        self.num_of_sub_stacks -= 1

      if self.stacks:
        self.cur_sub_stack_len = len(self.stacks[-1])
      else:
        self.cur_sub_stack_len = 0

    return item

  def pop_at(self, idx):
    if idx < 0 or idx >= self.num_of_sub_stacks:
      raise Exception("Stack index out of range")

    if self.stacks[idx]:
      return self.stacks[idx].pop()

s = SetOfStacks(3)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
s.push(9)

class SetOfStacksTest(unittest.TestCase):

  def test_set_of_stacks(self):
    self.assertEqual(s.stacks, [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]])

    
    self.assertEqual(s.pop(), 9)
    self.assertEqual(s.stacks, [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8]])

    s.pop()
    s.pop()
    self.assertEqual(s.stacks, [[1, 2, 3],
                                [4, 5, 6]])

    self.assertEqual(s.pop_at(0), 3)

    s.pop_at(0)
    s.pop_at(0)
    self.assertEqual(s.stacks, [[],
                                [4, 5, 6]])

    s.pop()
    s.pop()
    s.pop()
    self.assertEqual(s.stacks, [])

if __name__ == '__main__':
  unittest.main()