# Solution to Exercise 2.5 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi
#
# Assumptions:
# - Singly linked list has a tail pointer and a length property

import linked_list as lst

def add_lists(a, b):
  res = lst.LinkedList()
  top = None
  bottom = None
  carry = 0
  if a.length > b.length:
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

    res.append(n)
    top = top.next

  if carry is 1:
    res.append(1)

  return res
