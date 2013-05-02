# Solution to Exercise 1.5 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi
#
# Assumptions:
# - whitespace is significant

def compress(s):
  if not s:
    return s

  count = 0
  char_reps = []
  last_char = s[0]

  for c in s:
    if c != last_char:
      char_reps.append("".join([last_char, str(count)]))
      count = 0

    count += 1
    last_char = c

  char_reps.append("".join([last_char, str(count)]))
  c_str = "".join(char_reps)
  if len(s) < len(c_str):
    return s
  else:
    return c_str
