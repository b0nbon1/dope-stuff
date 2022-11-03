# follow-up questions are the characters ASCII or unicode
# without additional space
# determine if string has unique characters

def isUnique(s):
  checkArr = [False]*128
  for char in s:
    if checkArr[ord(char)]:
      return False
    else:
      checkArr[ord(char)] = True
  return True

strings = ["baba", "bro", "confusing!", "are you?"]
for s in strings:
  check = isUnique(s)
  print(check, end=", ")