# Implement a function to check if a linked list is a palindrome.
# Assumes list is doubly-linked.

import unittest
import doubly_linked_list as lst

def palindrome(lst):
  if not lst.head:
    return False

  mid = lst.count / 2
  left = lst.head
  right = lst.tail

  for i in range(mid):
    if left.item == right.item:
      left = left.next
      right = right.prev
    else:
      return False

  return True

l = lst.DoublyLinkedList()
l.push_tail(1)
l.push_tail(2)
l.push_tail(3)
l.push_tail(2)
l.push_tail(1)

class PalindromeTest(unittest.TestCase):

  def test_palindrome(self):
    self.assertEqual(palindrome(l), True)

    l.push_tail(4)    
    self.assertEqual(palindrome(l), False)

if __name__ == '__main__':
    unittest.main()
