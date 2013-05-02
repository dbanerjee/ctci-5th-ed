# Solution to Exercise 1.3 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi
#
# Assumptions:
# - whitespace is significant
# - case-sensitive

def is_permutation_sort(s1, s2):
  if len(s1) != len(s2):
    return False

  return sorted(s1) == sorted(s2)

def is_permutation_char_freq(s1, s2):
  if len(s1) != len(s2):
    return False

  char_freq = {}
  for c in s1:
    if c in char_freq:
      char_freq[c] += 1
    else:
      char_freq[c] = 1

  for c in s2:
    if c in char_freq:
      char_freq[c] -= 1
      if char_freq[c] < 0:
        return False
    else:
      return False

  return True
