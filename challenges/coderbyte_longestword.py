

#https://coderbyte.com/results/peettong:Longest%20Word:Python3

import re

def LongestWord(sen):
  wordz = re.findall('([a-zA-Z0-9]+)', sen)
  #print(wordz)
  longestwordlength = 0
  longestword = ""
  for word in wordz:
    if len(word) > longestwordlength:
      longestwordlength = len(word)
      longestword = word

  return longestword

# keep this function call here 
print(LongestWord(input()))
