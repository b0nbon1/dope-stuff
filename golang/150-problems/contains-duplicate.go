package problems_150

// https://leetcode.com/problems/contains-duplicate/description/

func ContainsDuplicate(nums []int) bool {
	// initialize a set or map to keep duplicates
    map_set := make(map[int]bool)

	// loop through the array and identify which number is a duplicate, O(n)
    for _, n := range nums {
         if _, exists := map_set[n]; exists {
            return true
         }
         map_set[n] = true
    }
    return false
}
