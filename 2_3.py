# Implement an algorithm to delete a node in the middle of a singly linked list,
# given only access to that node.
# Example:
# Input: the node c from the linked list a-> b -> c -> d -> e
# Result: nothing is returned, but the new linked list looks like
# a -> b -> d -> e

import unittest
import linked_list as lst

def del_node(node):
  node.item = node.next.item
  node.next = node.next.next

my_lst = lst.LinkedList()
my_lst.add('a')
my_lst.add('b')
my_lst.add('c')
my_lst.add('d')
my_lst.add('e')

node = my_lst.head.next.next

class DelNodeTest(unittest.TestCase):

  def test_del_node(self):
    del_node(node)
    self.assertEqual(my_lst.enumerate(), ['e', 'd', 'b', 'a'])
    
if __name__ == '__main__':
  unittest.main()
