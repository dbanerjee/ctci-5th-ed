# In the classic problem of the Towers of Hanoi, you have 3 towers and N disks
# of different sizes which can slide onto any tower. The puzzle starts with
# disks sorted in ascending order of size from top to bottom (i.e. each disk
# sits on top of an even larger one). You have the following constraints:
# (1) Only one disk can be moved at a time
# (2) A disk is slid off the top of one tower onto the next tower
# (3) A disk can only be placed on top of a larger disk
# Write a program to move the disks from the first tower to the last using
# stacks.

# Uses Python lists as if they were stacks.

import unittest

def move_disk(n, left, middle, right):
  if n > 0:
    move_disk(n - 1, left, right, middle)
    if left:
      right.append(left.pop())
    move_disk(n - 1, middle, left, right)
        
left = [1, 2, 3, 4]
middle = []
right = []

move_disk(len(left), left, middle, right)

class TowersOfHanoiTest(unittest.TestCase):

  def test_towers_of_hanoi(self):
    self.assertEqual(left, [])
    self.assertEqual(middle, [])
    self.assertEqual(right, [1, 2, 3, 4])

if __name__ == '__main__':
  unittest.main()