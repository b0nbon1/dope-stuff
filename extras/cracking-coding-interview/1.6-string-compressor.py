def stringCompressor(s):
  consecutiveCount = 0
  compressed_string = ""
  for i in range(len(s)):
    consecutiveCount+=1
    if i + 1 >= len(s) or s[i] != s[i+1]:
      compressed_string += (s[i]+str(consecutiveCount))
      consecutiveCount = 0
  return compressed_string

print(stringCompressor('aabccccaa'))