def urlify(s, trueLength):
  # get new last index
  newIndex = len(s)-1
  splitted = list(s)
  for i in range(trueLength-1, -1,-1):
    if splitted[i] == " ":
      splitted[newIndex] = "0"
      splitted[newIndex-1] = "2"
      splitted[newIndex-2] = "%"
      newIndex-=3
    else:
      splitted[newIndex] = splitted[i]
      newIndex-=1
  return ''.join(splitted)


print(urlify("Mr John Smith    ", 13))