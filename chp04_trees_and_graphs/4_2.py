# Solution to Exercise 4.2 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import queue as que
import graph as gph

def route_exists(g, from_key, to_key):
  for v in g.verts.keys():
    g.verts[v].set_colour('white')

  if from_key not in g.verts or to_key not in g.verts:
    return None

  cur_node = g.verts[from_key]
  cur_node.set_colour('grey')
  q = que.Queue()
  q.enqueue(cur_node)
  while q.count() > 0:
    for n in cur_node.get_connections():
      if n.get_colour() is 'white':
        if n.key is to_key:
          return True
        else:
          n.set_colour('grey')
          q.enqueue(n)

    cur_node.set_colour('black')
    cur_node = q.dequeue()

  return False

