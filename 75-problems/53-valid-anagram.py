#O(nlogn)
import collections

# O(nlogn) memory: O(1)
def isAnagram(self, s: str, t: str) -> bool:
  return sorted(s) == sorted(t)

# O(n) memory: O(n)
def isAnagram(s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      S = collections.Counter(s)
      for w in t:
        if w not in S:
          return False
        else:
          if S[w] == 0:
            return False
          else:
            S[w] -= 1
      return True

def isAnagram(s: str, t: str) -> bool:
      if len(s) != len(t):
        return False
      countS, countT = {}, {}
      for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
      for c in countS:
        if countS[c] != countT.get([c], 0):
          return False
      return True
