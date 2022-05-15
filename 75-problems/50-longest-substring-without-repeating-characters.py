def lengthOfLongestSubstring(s):
    unique = {}
    l = 0
    res = 0
    for r in range(len(s)):
      if s[r] in unique:
        if unique[s[r]] < l:
          res = max(res, r-l+1)
        else:
          l = unique[s[r]] + 1
      else:
        res = max(res, r-l+1)
      unique[s[r]] = r
    return res
