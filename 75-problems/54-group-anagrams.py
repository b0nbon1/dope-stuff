# O(m*nlogn)
import collections


def groupAnagrams1(strs):
  grouped = {}
  for string in strs:
    sortedStr = ''.join(sorted(string))
    if sortedStr in grouped:
      grouped[sortedStr].append(string)
    else:
      grouped[sortedStr] = [string]
  return list(grouped.values())


def groupAnagrams(strs):
  res = collections.defaultdict(list) # mapping charCount to list of anagrams

  for s in strs:
    count = [0] * 26
    for c in s:
      count[ord(c)-ord("a")] += 1
    res[tuple(count)].append(s)
    print(count)
  res.values()

groupAnagrams(["eat","tea","tan","ate","nat","bat"])