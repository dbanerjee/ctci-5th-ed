# Write code to remove duplicates from an unsorted linked list.  FOLLOW UP:
# How would you solve this problem if a temporary buffer is not allowed?
# Assumes lst param is non-empty.

import unittest
import linked_list as lst

def remove_dups(lst):
  elems = set()
  elems.add(lst.head.item)
  pred_node = lst.head
  
  while pred_node.next:
    if pred_node.next.item in elems:
      if lst.tail == pred_node.next:
        lst.tail = pred_node
        pred_node.next = None
      else:
        pred_node.next = pred_node.next.next

      lst.length -= 1
    
    else:
      elems.add(pred_node.next.item)
      pred_node = pred_node.next

  return lst.enumerate()

my_lst = lst.LinkedList()
my_lst.add('a')
my_lst.add('a')
my_lst.add('b')
my_lst.add('b')
my_lst.add('c')
my_lst.add('c')
my_lst.add('c')
my_lst.add('c')


class RemoveDupsTest(unittest.TestCase):

  def test_remove_dups(self):
     self.assertEqual(remove_dups(my_lst), ['c', 'b', 'a'])
    
if __name__ == '__main__':
  unittest.main()

