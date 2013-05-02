# Implementation of Depth-First Search
#
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import graph as gph
import stack as stk

class DFS:

  def __init__(self):
    self.time = 0

  def dfs_visit(self, v):
    print v.get_key()
    
    v.set_colour('grey')
    self.time += 1
    v.set_disc_time(self.time)
    
    for n in v.get_connections():
      if n.get_colour() is 'white':
        n.set_pred(v)
        self.dfs_visit(n)
    
    v.set_colour('black')
    self.time += 1
    v.set_fin_time(self.time)
    
  def dfs(self, g):
    for v in g.get_vertices():
      g.verts[v].set_colour('white')
      g.verts[v].set_pred(None)

    for v in g.get_vertices():
      if g.verts[v].get_colour() is 'white':
        self.dfs_visit(g.verts[v])

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

  DFS().dfs(g)

if __name__ == "__main__":
   main()
