import collections


def isPermutationPalindrome(phrase):
  countOdd = 0
  ## create table to store letters
  lettterTable = collections.defaultdict(int)
  for char in phrase:
    # increment the letter found
    lettterTable[char]+=1

    # if letter is odd increment count Odd
    if lettterTable[char] %2 == 1:
      countOdd+=1

    # if letter is even decrement count Odd
    else:
      countOdd-=1
  return countOdd <= 1

print(isPermutationPalindrome("racocar"))
