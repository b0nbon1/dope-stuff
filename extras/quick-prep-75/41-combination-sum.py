class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # initialise a list where the combinations will be stored
        result = []
        # create a dfs function, with the current index, curr list and current sum of the combinations
        def dfs(i, curr, total):
            # if the current sum is equal to total, add the values into our combinations and exit
            # we copy the curr_list because we don't wanna rewrite it once added
            if total == target:
                result.append(curr.copy())
                return
            # if the total is over the candidates or index out of bound, we exit our recursion
            if i >= len(candidates) or total > target:
                return
            # append current index multiple times -> eg. list => [1,2,3,4] and target is 3 will be => [1,1,1]
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            # remove the current, because we don't want duplicates in other forms
            curr.pop()
            # run the rest of the values without duplicates
            dfs(i+1, curr, total)
        # call the dfs func
        dfs(0, [], 0)
        return result
