

#https://coderbyte.com/results/peettong:Codeland%20Username%20Validation:Python3

import re

def CodelandUsernameValidation(strParam):
  l = len(strParam)
  if l < 4 or l > 25:
    return "false"
  if not strParam[0].isalpha():
    return "false"
  if strParam[l-1] == "_":
    return "false"
  strParam = re.sub("_", "", strParam)
  if not strParam.isalnum():
    return "false"
  # code goes here
  return "true"

# keep this function call here 
print(CodelandUsernameValidation(input()))
