# Write a program to sort a stack in ascending order (with biggest items on
# top). You may use additional stacks to hold items, but you may not copy the
# elements into any other data structure (such as an array). The stack supports
# the following operations: push, pop, peek, isEmpty.

# This solution uses Python lists as stacks and sticks to only the
# append (push), pop (pop), and -1 indexing [peek] ops.

import unittest

def sort_stack(st):
  source = st
  remaining = []
  srted = []

  while source:
    srted.append(source.pop())

    while source:
      if source[-1] > srted[-1]:
        remaining.append(srted.pop())
        srted.append(source.pop())
      else:
        remaining.append(source.pop())

    source = remaining
    remaining = []
    
  while srted:
    st.append(srted.pop())

my_st = [3, 6, 2, 9, 6, 3, 0, 1, 4, 8, 3, 5]

class SortStackTest(unittest.TestCase):

  def test_sort_stack(self):
    sort_stack(my_st)
    self.assertEqual(my_st, [0, 1, 2, 3, 3, 3, 4, 5, 6, 6, 8, 9])
    
if __name__ == '__main__':
  unittest.main()