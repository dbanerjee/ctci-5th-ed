# Solution to Exercise 2.6 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import linked_list as lst

def detect_loop_with_floyds(lst):
  slow_runner = lst.head.next
  fast_runner = lst.head.next.next
  
  while slow_runner is not fast_runner:
    slow_runner = slow_runner.next  

    if fast_runner.next:
      fast_runner = fast_runner.next.next
    else:
      return None
    
  slow_runner = lst.head
  while slow_runner is not fast_runner:
    slow_runner = slow_runner.next
    fast_runner = fast_runner.next

  return slow_runner

def detect_loop_with_set(lst):
  visited = set()
  cur_node = lst.head

  while cur_node:
    if cur_node in visited:
      return cur_node
    else:
      visited.add(cur_node)
      cur_node = cur_node.next

  return None
