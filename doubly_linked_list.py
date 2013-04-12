class Node:

  def __init__(self, item):
    self.item = item
    self.prev = None
    self.next = None

class DoublyLinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0

  def push_head(self, item):
    node = Node(item)
    if not self.head:
      self.head = node
      self.tail = node
    else:
      node.next = self.head
      self.head.prev = node
      self.head = node
    self.count += 1

  def push_tail(self, item):
    node = Node(item)
    if not self.tail:
      self.tail = node
      self.head = node
    else:
      node.prev = self.tail
      self.tail.next = node
      self.tail = node
    self.count += 1

  def pop_head(self):
    if not self.head:
      return None

    item = self.head.item
    if self.head == self.tail:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next

    self.count -= 1
    return item

  def pop_tail(self):
    if not self.tail:
      return None

    item = self.tail.item
    if self.tail == self.head:
      self.tail = None
      self.head = None
    else:
      self.tail = self.tail.prev

    self.count -= 1
    return item

  def enumerate(self):
    elems = []
    cur_node = self.head
    while cur_node:
      elems.append(cur_node.item)
      cur_node = cur_node.next

    return elems










