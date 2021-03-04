

#https://coderbyte.com/results/peettong:Min%20Window%20Substring:Python3

import re

def isSubString(S, K):
  K = list(K)
  O = S
  S = list(S)
  #Where S is the bigger substring we evaluate if it contains all chars of K
  for c in range(len(K)):
    if K[0] not in S:
      break
    else:
      S.remove(K[0])
      K.remove(K[0])
  else:
    return O
  return "None"

def MinWindowSubstring(strArr):
  N = tuple(strArr[0]) # a fast list of characters
  K = tuple(strArr[1]) # a fast list of characters
  klen = len(K)
  nlen = len(N)
