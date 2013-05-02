# Implementation of Breadth-First Search
#
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import graph as gph
import queue as que

def bfs(g, start):
  for v in g.get_vertices():
    g.verts[v].set_colour('white')
    g.verts[v].set_pred(None)

  q = que.Queue()
  start.set_colour('grey')
  q.enqueue(start)
  while q.count() > 0:
    cur = q.dequeue()
    print cur.get_key()
    for n in cur.get_connections():
      if n.get_colour() is 'white':
        n.set_colour('grey')
        n.set_pred(cur)
        q.enqueue(n)
    
    cur.set_colour('black')

def main():
  g = gph.Graph()

  g.add_edge(1, 2)
  g.add_edge(1, 3)
  g.add_edge(1, 4)
  g.add_edge(2, 5)
  g.add_edge(2, 6)
  g.add_edge(4, 7)
  g.add_edge(4, 8)
  g.add_edge(5, 9)
  g.add_edge(5, 10)
  g.add_edge(7, 11)
  g.add_edge(7, 12)

  bfs(g, g.get_vertex(1))

if __name__ == "__main__":
   main()
