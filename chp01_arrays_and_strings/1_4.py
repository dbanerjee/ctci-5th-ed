# Solution to Exercise 1.4 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi
#
# Assumptions:
# - Regex can't be used

def replace_char(s, trgt, new_char):
  l = []
  for c in s:
    if c == trgt:
      l.append('%20')
    else:
      l.append(c)

  return "".join(l)
