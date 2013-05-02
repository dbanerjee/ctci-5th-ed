# Implementation of a directed graph.

class Vertex:

  def __init__(self, key):
    self.key = key
    self.colour = 'white'
    self.connected_to = {}

  def add_neighbour(self, vert, weight=0):
    self.connected_to[vert] = weight

  def get_connections(self):
    return self.connected_to.keys()

  def neighbours(self):
    return str(self.key) + ' connected to: ' +\
           str([x.key for x in self.connected_to])

  def set_colour(self, c):
    self.colour = c

  def get_colour(self):
    return self.colour


class Graph:

  def __init__(self):
    self.vert_count = 0
    self.edge_count = 0
    self.verts = {}

  def add_vertex(self, key):
    new_vert = Vertex(key)
    self.verts[key] = new_vert
    self.vert_count += 1
    return new_vert

  def get_vertex(self, key):
    if key in self.verts:
      return self.verts[key]
    else:
      return False

  def add_edge(self, from_vert, to_vert, weight=0):
    if from_vert not in self.verts:
      self.add_vertex(from_vert)

    if to_vert not in self.verts:
      self.add_vertex(to_vert)

    self.verts[from_vert].add_neighbour(self.verts[to_vert], weight)
    self.edge_count += 1

  def get_vertices(self):
    return self.verts.keys()



