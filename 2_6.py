# Given a circular linked list, implement an algorithm which returns the node at
# the beginning of the loop.
# Definition:
# Circular linked list: A (corrupt) linked list in which a node's next pointer
# points to an earlier node, so as to make a loop in the linked list.
# Example:
# Input: A -> B -> C -> D -> E -> C (the same as C as earlier)
# Output: C

import unittest
import doubly_linked_list as lst

def detect_loop(lst):
  visited = set()
  cur_node = lst.head

  while cur_node:
    if cur_node in visited:
      return cur_node
    else:
      visited.add(cur_node)
      cur_node = cur_node.next

  return None

l = lst.DoublyLinkedList()
l.push_tail('a')
l.push_tail('b')
l.push_tail('c')
l.push_tail('d')
l.push_tail('e')
l.tail.next = l.head.next.next

class DetectLoopTest(unittest.TestCase):

  def test_detect_loop(self):
    node = detect_loop(l)
    self.assertEqual(node, l.head.next.next)
    
if __name__ == '__main__':
  unittest.main()
