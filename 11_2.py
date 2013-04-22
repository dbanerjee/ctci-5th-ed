# 11.2 Write a method to sort an array of strings so that all the anagrams are
# next to each other.

# Assumes strings are lower-case with no spaces and, aside from anagrams being
# next to each-other, no other ordering matters.

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

words = ["meat", "tan", "calm", "team", "ant", "mate", "clam"]
