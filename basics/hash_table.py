# Implementation of a Hash Table.
#
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

class HashTable:

  def __init__(self):
    self.size = 9973
    self.slots = [None] * self.size
    self.data = [None] * self.size
    self.alpha = 26

  def _hash_fn(self, key):
    key_len = len(key)
    raw_hash = reduce(lambda x, y: x + y,
                 map(lambda x, y: self.alpha**(key_len - (x + 1)) * ord(y),
                     range(key_len), key))
    return raw_hash % self.size

  def _rehash(self, old_hash):
    return (old_hash + 1) % self.size

  def put(self, key, val):
    if key == '***':
      raise KeyError("'***' is a reserved key")
    
    hash_val = self._hash_fn(key)

    if self.slots[hash_val] == None or self.slots[hash_val] == '***':
      self.slots[hash_val] = key
      self.data[hash_val] = val
    elif self.slots[hash_val] == key:
      self.data[hash_val] = val
    else:
      next_slot = self._rehash(hash_val)
      while self.slots[next_slot] != None and self.slots[next_slot] != key:
        next_slot = self._rehash(next_slot)

      if self.slots[next_slot] == None:
        self.slots[next_slot] = key
        self.data[next_slot] = data
      elif self.slots[next_slot] == key:
        self.data[next_slot] = val

  def _get(self, key):   
    start_slot = self._hash_fn(key)
    
    cur_pos = start_slot
    while self.slots[cur_pos] != None:
      if self.slots[cur_pos] == key:
        return cur_pos
      else:
        cur_pos = self._rehash(cur_pos)
        if cur_pos == start_slot:
          return None

    return None

  def get(self, key):
    if key == '***':
      raise KeyError("'***' is a reserved key")
    
    loc = self._get(key)
    if loc:
      return self.data[loc]
    else:
      return None

  def __getitem__(self, key):
    return self.get(key)

  def __setitem__(self, key, data):
    return self.put(key, data)

  def delete(self, key):
    if key == '***':
      raise KeyError("'***' is a reserved key")
  
    loc = self._get(key)
    if loc:
      self.slots[loc] = '***'
      return self.data[loc]
    else:
      return None

  def contains(self, key):
    if key == '***':
      raise KeyError("'***' is a reserved key")

    if self._get(key):
      return True
    else:
      return False






