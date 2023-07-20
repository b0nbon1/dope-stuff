def groupAnagrams(strs):
    # initialize a list with list as it's values
    countMap = collections.defaultdict(list)
    # loop through the array strings
    for string in strs:
        # initialize the count array for the with 26 letters
        count = [0] * 26
        # loop through the list
        for char in string:
            # count the letters on the string
            count[ord(char)-ord("a")] += 1
        # append the list to the respective anagram to group them
        countMap[tuple(count)].append(string)
    # get the values only in 2-D arr
    return countMap.values()