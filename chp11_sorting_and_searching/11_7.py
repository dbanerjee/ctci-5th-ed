# Solution to Exercise 11.7 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi.

def partition(elems, attr, left, right):
  first = left
  piv = elems[first][attr]
  piv_pair = elems[first]

  while left <= right:

    while left <= right and elems[left][attr] <= piv:
      left += 1
    while left <= right and elems[right][attr] > piv:
      right -= 1

    if left < right:
      tmp = elems[left]
      elems[left] = elems[right]
      elems[right] = tmp
  
  elems[first] = elems[right]
  elems[right] = piv_pair
  return right

def _quicksort(elems, attr, left, right):
  if left < right:
    new_piv_index = partition(elems, attr, left, right)

    _quicksort(elems, attr, left, new_piv_index - 1)
    _quicksort(elems, attr, new_piv_index + 1, right)

def sort_persons(persons, attr):
  _quicksort(persons, attr, 0, len(persons) - 1)

def build_tower(persons):
  height = 0
  weight = 1
  sort_persons(persons, height)

  person_idxs = [0]
  preds = [None] * len(persons)

  for i in range(1, len(persons)):
    for j in range(len(person_idxs)):
      if persons[i][weight] < persons[person_idxs[j]][weight]:
        preds[i] = person_idxs[j - 1]
        person_idxs[j] = i
        break
      elif persons[i][weight] is persons[person_idxs[j]][weight]:
        break
    if persons[i][weight] > persons[person_idxs[-1]][weight]:
      preds[i] = person_idxs[-1]
      person_idxs.append(i)

  tower = []
  pos = person_idxs[-1]
  for _ in range(len(person_idxs)):
    tower.append(persons[pos])
    pos = preds[pos]

  return "The tower is " + str(len(tower)) + " persons high: " +\
          str(tower[::-1])
