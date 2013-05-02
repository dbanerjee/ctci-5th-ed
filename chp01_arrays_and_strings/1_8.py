# Solution to Exercise 1.8 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

def check_rotation(s1, s2):
  return s2 in s1 + s1
