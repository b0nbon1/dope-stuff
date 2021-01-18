#include <vector>
#include <unordered_map>
#include <iostream>

class Solution {
public:
    std::vector<int> twoSumVector(std::vector<int>& nums, int target) {
        /*
            2 => 2 +7, 2+11,2+15
            7 => ................
        */
       std::vector<int> pair = {0,0};
       int sum = 0;
       int solution = 0;

       for (size_t i = 0; i < nums.size(); i++)
       {
           for (size_t j = 0; j < nums.size(); j++)
           {
               if (j == i) continue;
               sum = nums[i] + nums[j];
               if (sum == target) {
                   pair[0] = i;
                   pair[1] = j;
                   solution = sum;
                   break;
               }

               if(sum >= solution && sum < target) {
                   pair[0] = i;
                   pair[1] = j;
                   solution = sum;
               }
           }
           if(solution == target) break;
       }
       


       return pair;
    }
    std::vector<int> twoSumHash(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> pair;
        std::vector<int> air = {0,0};
        int compliment;
       for (size_t i = 0; i < nums.size(); i++)
       {
           pair[nums[i]] = i;
       }
       for (size_t i = 0; i < nums.size(); i++)
       {
           compliment = target - nums[i];
           if(pair.count(compliment) > 0 && i != pair[compliment]) {
               air[0] = i;
               air[1] = pair[compliment];
               break;
           }

       }

       return air;
    }
};

int main() {
    Solution sol;

    std::vector<int> pair;
    std::vector<int> nums = {3,3,2,4};

    pair = sol.twoSumHash(nums, 6);

    std::cout << pair[0] << "\t" << pair[1] << std::endl;

    return 0;
}
