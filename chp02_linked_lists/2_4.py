# Solution to Exercise 2.4 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi
#
# Assumptions:
# - Singly linked list has a tail pointer

import linked_list as lst
import doubly_linked_list as dublst

def partition_singly(x, singlst):
  before_x = lst.LinkedList()
  after_x = lst.LinkedList()

  cur_node = singlst.head
  item_count = 0
  while cur_node:
    if cur_node.item < x:
      before_x.add(cur_node.item)
    elif cur_node.item > x:
      after_x.add(cur_node.item)
    else:
      before_x.append(cur_node.item)
    
    cur_node = cur_node.next
  
  source_node = before_x.head
  target_node = singlst.head
  while source_node:
    target_node.item = source_node.item
    source_node = source_node.next
    target_node = target_node.next

  source_node = after_x.head
  while source_node:
    target_node.item = source_node.item
    source_node = source_node.next
    target_node = target_node.next

def partition_doubly(x, dublst):
  left = dublst.head
  right = dublst.tail
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

