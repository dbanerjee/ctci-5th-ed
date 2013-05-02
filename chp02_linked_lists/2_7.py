# Solution to Exercise 2.7 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import linked_list as lst
import doubly_linked_list as dublst

def palindrome_singly(lst):
  slow_runner = lst.head
  fast_runner = lst.head
  elems = []

  while True:
    elems.append(slow_runner.item)

    if fast_runner.next:
      fast_runner = fast_runner.next.next
    else:
      break

    slow_runner = slow_runner.next

  while elems:
    if elems.pop() is slow_runner.item:
      slow_runner = slow_runner.next
    else:
      return False

  return True

def palindrome_doubly(lst):
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

