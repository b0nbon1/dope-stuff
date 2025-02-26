package problems_150

//https://leetcode.com/problems/valid-anagram/description/
func IsAnagram(s string, t string) bool {
	// create a map to store the chars/rune with how many they're
    map_anagram := make(map[byte]int)

	// make sure the string are of same length, otherwise they're not anagrams
    if len(s) != len(t) {
        return false
    }

	// loop through the characters of each is while increment on s and decrement on t, to make sure they've equal characters
    for i := range s {
        map_anagram[s[i]] += 1
        map_anagram[t[i]] -= 1
    }

	// if character were not the same they won't have zero on the map so check and eliminate if true
    for _, v := range map_anagram {
        if v != 0 {
            return false
        }
    }

    return true
}

