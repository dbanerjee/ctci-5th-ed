# You have two numbers represented by a linked list, where each node contains a
# single digit. The digits are stored in reverse order, such that the 1's digit
# is at the head of the list. Write a function that adds the two numbers and
# returns the sum as a linked list.
# Example:
# Input: ( 7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295
# Output: 2 -> 1 -> 9. That is, 912.
# Follow up:
# suppose the digits are stored in forward order. repeat the above problem.
# Example:
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is 617 + 295
# Output: 9 -> 1 -> 2. That is, 912

# Assumes use of doubly-linked list. For the forward order variation, a similar
# solution would be done starting from the tail rather than the head.

import unittest
import doubly_linked_list as lst

def add_lists(a, b):
  res = lst.DoublyLinkedList()
  top = None
  bottom = None
  carry = 0
  if a.count > b.count:
    top = a.head
    bottom = b.head
  else:
    top = b.head
    bottom = a.head

  while top:
    n = None
    if bottom:
      n = carry + top.item + bottom.item
      bottom = bottom.next
    else:
      n = carry + top.item

    if n >= 10:
      n = n % 10
      carry = 1
    else:
      carry = 0

    res.push_tail(n)
    top = top.next

  if carry is 1:
    res.push_tail(1)

  return res

lst_a = lst.DoublyLinkedList()
lst_a.push_tail(7)
lst_a.push_tail(1)
lst_a.push_tail(6)

lst_b = lst.DoublyLinkedList()
lst_b.push_tail(5)
lst_b.push_tail(9)
lst_b.push_tail(2)

lst_c = lst.DoublyLinkedList()
lst_c.push_tail(9)
lst_c.push_tail(9)
lst_c.push_tail(9)
lst_c.push_tail(9)
lst_c.push_tail(9)

class AddTest(unittest.TestCase):

  def test_add(self):
    res = add_lists(lst_a, lst_b)
    self.assertEqual(res.enumerate(), [2, 1, 9])

    res = add_lists(lst_a, lst_c)
    self.assertEqual(res.enumerate(), [6, 1, 6, 0, 0, 1])

if __name__ == '__main__':
  unittest.main()
