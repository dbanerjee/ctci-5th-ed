# Solution to Exercise 1.2 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi
#

def reverse_str_a(s):
  l = []
  for i in range(len(s) - 1, -1, -1):
    l.append(s[i])

  return "".join(l)

def reverse_str_b(s):
  m = list(s)
  i = 0
  j = len(s) - 1
  while i < j:
    m[i], m[j] = m[j], m[i]
    i += 1
    j -=1 

  return "".join(m)