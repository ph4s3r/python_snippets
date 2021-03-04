

#https://coderbyte.com/results/peettong:Bracket%20Matcher:Python3

import re

def BracketMatcher(strParam):

  l = len(strParam)
  obc = len(re.findall("\(", strParam))
  cbc = len(re.findall("\)", strParam))
  # non matching number of opening and closing brackets return 0
  if obc != cbc: 
    return 0
  # if str contains no brackets return 1
  if obc == 0 and cbc == 0: 
    return 1

  for j in range(2): #this is a trick here, no comment
  # remove all i-long substrings where the first character is an ob, last is cb 
    for i in range(l):
      while True:
        strParam, replaces = re.subn("\(.{" + str(i) + "}\)", "", strParam)
        if replaces == 0:
          break
        else:
          pass
          #print("inner brackets removed, new string:", strParam)
    
  obc = len(re.findall("\(", strParam))
  cbc = len(re.findall("\)", strParam))
  if obc == 0 and cbc == 0:
    return 1
  
  return 0


# keep this function call here 
print(BracketMatcher(input()))
