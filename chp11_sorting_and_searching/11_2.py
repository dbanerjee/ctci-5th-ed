# Solution to Exercise 11.2 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

def hash(w):
  return reduce(lambda x, y: x + y, map(lambda x: ord(x), w))

def anagram_sort(ws):
  anagrams = {}
  for w in ws:
    key = hash(w)
    if key in anagrams:
      anagrams[key].append(w)
    else:
      anagrams[key] = [w]

  w_list = []
  for k in anagrams.keys():
    w_list.extend(anagrams[k])

  return w_list

