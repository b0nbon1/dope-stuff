from collections import Counter


def permutationTwoStrings(s1, s2):
  if len(s1) != len(s2):
    return False
  countDict = Counter(s1)
  for char in s2:
    if char not in countDict or countDict[char] < 0:
      return False
    countDict[char]-=1
  return True

print(permutationTwoStrings("abbybot", "babybit"))
