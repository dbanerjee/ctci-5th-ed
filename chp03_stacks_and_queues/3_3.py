# Solution to Exercise 3.3 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

class SetOfStacks:

  def __init__(self, sub_stack_size):
    self.sub_stack_size = sub_stack_size
    self.num_of_sub_stacks = 0
    self.cur_sub_stack_len = 0
    self.stacks = []

  def push(self, item):
    if not self.stacks or self.cur_sub_stack_len is self.sub_stack_size:
      self.stacks.append([item])
      self.num_of_sub_stacks += 1
      self.cur_sub_stack_len = 0
    else:
      self.stacks[-1].append(item)

    self.cur_sub_stack_len += 1

  def pop(self):
    if not self.stacks:
      return None

    item = self.stacks[-1].pop()
    if self.stacks[-1]:
      self.cur_sub_stack_len -= 1
    else:

      # This deals with cases where pop_at may have completely emptied an
      # earlier stack.
      while self.num_of_sub_stacks is not 0 and not self.stacks[-1]:
        self.stacks.pop()
        self.num_of_sub_stacks -= 1

      if self.stacks:
        self.cur_sub_stack_len = len(self.stacks[-1])
      else:
        self.cur_sub_stack_len = 0

    return item

  def pop_at(self, idx):
    if idx < 0 or idx >= self.num_of_sub_stacks:
      raise Exception("Stack index out of range")

    if self.stacks[idx]:
      return self.stacks[idx].pop()
