# Implementation of singly linked list. Needs refactoring to get rid of code
# duplication.

class Node:

  def __init__(self, item):
    self.item = item
    self.next = None

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def add(self, item):
    node = Node(item)
    node.next = self.head
    self.head = node

    if not self.tail:
      self.tail = node

    self.length += 1

  def remove(self, item):
    if not self.head:
      return None

    if self.head.item == item:
      self.head = self.head.next
      self.length -= 1

      if self.length == 0:
        self.tail = None

      return item

    trailing_node = self.head
    leading_node = self.head.next
    while leading_node:
      if leading_node.item == item:
        trailing_node.next = leading_node.next
        if self.tail == leading_node:
          self.tail = trailing_node
        self.length -= 1
        return item
      else:
        trailing_node = leading_node
        leading_node = leading_node.next

  def search(self, item):
    cur_node = self.head
    while cur_node:
      if cur_node.item == item:
        return True
      else:
        cur_node = cur_node.next

    return False

  def is_empty(self):
    return self.head == None

  def len(self):
    return self.length

  def append(self, item):
    node = Node(item)
    if self.tail:
      self.tail.next = node
    
    self.tail = node  
    
    if not self.head:
      self.head = node

    self.length += 1

  def index(self, item):
    cur_node = self.head
    idx = 0
    while cur_node:
      if cur_node.item == item:
        return idx
      else:
        cur_node = cur_node.next
        idx += 1

    return None

  def insert(self, pos, item):
    if pos == 0:
      self.add(item)
    elif pos > self.length - 1:
      self.append(item)
    else:
      idx = 1
      pred_node = self.head

      while idx != pos:
        idx += 1
        pred_node = pred_node.next

      post_node = pred_node.next
      node = Node(item)
      node.next = post_node
      pred_node.next = node

      self.length += 1

  def pop(self):
    if self.head:
      return self.remove(self.head.item)
    else:
      return None

  def pop_pos(self, pos):
    if pos == 0:
      return self.pop()
    elif pos > self.length -1:
      return None
    else:
      idx = 1
      pred_node = self.head
      while idx != pos:
        idx += 1
        pred_node = pred_node.next

      item = pred_node.next.item
      if pred_node.next == self.tail:
        self.tail = pred_node
        pred_node.next = None
      else:
        pred_node.next = pred_node.next.next

      self.length -= 1
      return item

  def enumerate(self):
    cur_node = self.head
    elems = []
    while cur_node:
      elems.append(cur_node.item)
      cur_node = cur_node.next

    return elems







    
