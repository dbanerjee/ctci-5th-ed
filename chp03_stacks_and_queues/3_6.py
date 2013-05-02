# Solution to Exercise 3.6 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

def sort_stack(st):
  source = st
  remaining = []
  srted = []

  while source:
    srted.append(source.pop())

    while source:
      if source[-1] > srted[-1]:
        remaining.append(srted.pop())
        srted.append(source.pop())
      else:
        remaining.append(source.pop())

    source = remaining
    remaining = []
    
  while srted:
    st.append(srted.pop())
