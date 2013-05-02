# Solution to Exercise 3.4 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

def move_disk(n, left, middle, right):
  if n > 0:
    move_disk(n - 1, left, right, middle)
    if left:
      right.append(left.pop())
    move_disk(n - 1, middle, left, right)
