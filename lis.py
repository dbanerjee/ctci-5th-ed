# Basic use of dynamic programming to find longest increasing subsequence.

def lis(elems):

  m = [0]
  p = [None] * len(elems)

  for i in range(1, len(elems)):
    for j in range(len(m)):
      if elems[i] < elems[m[j]]:
        p[i] = m[j - 1]
        m[j] = i
        break
      elif elems[i] is elems[m[j]]:
        break
    if elems[i] > elems[m[-1]]:
        p[i] = m[-1]
        m.append(i)

  lis_elems = []
  pos = m[-1]
  for _ in range(len(m)):
    lis_elems.append(elems[pos])
    pos = p[pos]

  return "The LIS is " + str(len(m)) + ": " + str(lis_elems[::-1])







