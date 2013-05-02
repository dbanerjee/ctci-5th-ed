# Solution to Exercise 4.3 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import binary_search_tree as bst

def partition(elems):
  if not elems:
    return None

  mid = len(elems) / 2
  val = [elems[mid]]
  left = partition(elems[:mid])
  right = partition(elems[mid + 1:])
  if left:
    val.extend(left)
  if right:
    val.extend(right)
  return val

def build_bst(coll):

  t = bst.BinarySearchTree()
  
  elems = partition(coll)
  for e in elems:
    t.add(e)

  return t



