# Write code to partition a linked list around a value x, such that all nodes
# less than x come before all nodes greater than or equal to x.
# Assumes x and list items are integers.

import unittest
import doubly_linked_list as lst

def partition(x, lst):
  left = lst.head
  right = lst.tail
  done = False
  while not done:
    while left is not right and left.item < x:
      left = left.next
    while right is not left and right.item >= x:
      right = right.prev

    if left is right:
      done = True
    else:
      tmp = left.item
      left.item = right.item
      right.item = tmp

my_lst = lst.DoublyLinkedList()
my_lst.push_head(1)
my_lst.push_head(2)
my_lst.push_head(3)
my_lst.push_head(4)
my_lst.push_head(5)

class PartitionTest(unittest.TestCase):

  def test_partition(self):
    partition(3, my_lst)
    self.assertEqual(my_lst.enumerate(), [1, 2, 3, 4, 5])
    
if __name__ == '__main__':
  unittest.main()
