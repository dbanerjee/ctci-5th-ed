# Describe how you would use a single array to implement three stacks.
# This solution grows the first stack from the left, the second stack from the
# right, and the third stack from the middle by alternating left and right.
# This solution is best when the third (middle) stack is favoured.

class TertiaryStack:

  def __init__(self, size):
    if size <= 0:
      raise Exception("Size must be at least one")

    self.items = [None] * size
    self.st_one_len = 0
    self.st_one_cur = -1
    self.st_two_len = 0
    self.st_two_cur = size
    self.st_three_len = 0
    self.st_three_cur = size / 2
    self.st_three_cur_dir = 1

  def push(self, st_num, item):
    if item is None:
      raise Exception("Item cannot be None (reserved).")

    if st_num is 1:
      if self.st_one_cur + 1 >= self.st_three_cur or\
         self.items[self.st_one_cur + 1] is not None:
        raise Exception("Stack one is full")

      self.items[self.st_one_cur + 1] = item
      self.st_one_cur += 1
      self.st_one_len += 1

    elif st_num is 2:
      if self.st_two_cur - 1 <= self.st_three_cur or\
         self.items[self.st_two_cur - 1] is not None:
        raise Exception("Stack two is full")

      self.items[self.st_two_cur - 1] = item
      self.st_two_cur -= 1
      self.st_two_len += 1

    elif st_num is 3:
      next_slot = self.st_three_cur + (self.st_three_len *
                                       self.st_three_cur_dir)

      if next_slot <= self.st_one_cur or next_slot >= self.st_two_cur or\
         self.items[next_slot] is not None:
        raise Exception("Stack three cannot expand further")

      self.items[next_slot] = item
      self.st_three_cur = next_slot
      self.st_three_len += 1
      self.st_three_cur_dir *= -1

    else:
      raise Exception("Unknown stack referenced")

  def pop(self, st_num):
    if st_num is 1:
      if self.st_one_len > 0:
        item = self.items[self.st_one_cur]
        self.items[self.st_one_cur] = None
        self.st_one_len -= 1
        self.st_one_cur -= 1
        return item

    elif st_num is 2:
      if self.st_two_len > 0:
        item = self.items[self.st_two_cur]
        self.items[self.st_two_cur] = None
        self.st_two_len -= 1
        self.st_two_cur += 1
        return item

    elif st_num is 3:
      if self.st_three_len > 0:
        item = self.items[self.st_three_cur]
        self.items[self.st_three_cur] = None
        self.st_three_len -= 1
        self.st_three_cur += self.st_three_len * self.st_three_cur_dir
        self.st_three_cur_dir *= -1
        return item

    else:
      raise Exception("Unknown stack referenced")

  def peek(self, st_num):
    if st_num is 1:
      if self.st_one_len > 0:
        return self.items[self.st_one_cur]
    elif st_num is 2:
      if self.st_two_len > 0:
        return self.items[self.st_two_cur]
    elif st_num is 3:
      if self.st_three_len > 0:
        return self.items[self.st_three_cur]
    else:
      raise Exception("Unknow stack referenced")

  def count(self, st_num):
    if st_num is 1:
      return self.st_one_len
    elif st_num is 2:
      return self.st_two_len
    elif st_num is 3:
      return self.st_three_len
    else:
      raise Exception("Unknow stack referenced")

  def enumerate(self):
    return self.items

