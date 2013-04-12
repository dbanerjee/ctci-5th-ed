# Write code to implement an algorithm to find the kth to last element of a
# singly-linked list.
# I'm assuming the list has a length property.

import unittest
import linked_list as lst

def kth_to_last(k, lst):
  end = lst.len()
  if k > end or k <= 0:
    return None

  cur_pos = k
  cur_node = lst.head
  while cur_pos != end:
    cur_pos += 1
    cur_node = cur_node.next

  return cur_node.item

my_lst = lst.LinkedList()
my_lst.add('a')
my_lst.add('b')
my_lst.add('c')
my_lst.add('d')
my_lst.add('e')
my_lst.add('f')
my_lst.add('g')
my_lst.add('h')


class KthToLastTest(unittest.TestCase):

  def test_kth_to_last(self):
    self.assertEqual(kth_to_last(1, my_lst), 'a')
    self.assertEqual(kth_to_last(2, my_lst), 'b')
    self.assertEqual(kth_to_last(8, my_lst), 'h')

    
if __name__ == '__main__':
  unittest.main()

