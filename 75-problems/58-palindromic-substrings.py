def countSubstrings(s):
  res = 0

  for i in range(len(s)):
    # odd length
    l, r = i, i
    while l >= 0 and r < len(s) and s[l] == s[r]:
      res+=1
      l -= 1
      r += 1
    # even length
    l, r = i, i+1
    while l >= 0 and r < len(s) and s[l] == s[r]:
      res+=1
      l -= 1
      r += 1
  return res

print(countSubstrings("aaa"))