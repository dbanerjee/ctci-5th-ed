# Solution to Exercise 2.3 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import linked_list as lst

def del_node(node):
  node.item = node.next.item
  node.next = node.next.next
