# Implementation of a Directed Graph using adjacency lists and supporting
# Breadth-First Search and Depth-First Search.
#
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import sys

class Vertex:

  def __init__(self, key):
    self.key = key
    self.connected_to = {}
    self.colour = 'white'
    self.dist = sys.maxsize
    self.pred = None
    self.disc_time = 0
    self.fin_time = 0 

  def add_neighbour(self, vert, weight=0):
    self.connected_to[vert] = weight

  def get_connections(self):
    return self.connected_to.keys()

  def neighbours(self):
    return str(self.key) + ' connected to: ' +\
           str([x.key for x in self.connected_to])

  def get_key(self):
    return self.key

  def set_colour(self, colour):
    self.colour = colour

  def get_colour(self):
    return self.colour

  def set_pred(self, pred):
    self.pred = pred

  def get_pred(self):
    return self.pred

  def set_disc_time(self, time):
    self.disc_time = time

  def get_disc_time(self):
    return self.disc_time

  def set_fin_time(self, time):
    self.fin_time = time

  def get_fin_time(self):
    return self.fin_time

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



