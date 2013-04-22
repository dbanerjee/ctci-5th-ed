# Given a directd graph, design an algorithm to find out whether there is a
# route between two nodes.

# This implementation assumes a graph implementation using adjacency lists, and
# there is a way to mark nodes (using colour in this case).

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
          return Truereload
        else:
          n.set_colour('grey')
          q.enqueue(n)

    cur_node.set_colour('black')
    cur_node = q.dequeue()

  return False

