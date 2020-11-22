#include <algorithm>
#include <unordered_set>

using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen{};
        for (int i = 0; i < nums.size(); ++ i) {
            auto found = seen.find(target - nums[i]);
            if (found != seen.end()) {
                return vector<int>{found->second, i};
            }
            seen[nums[i]] = i;
        }
        return {-1, -1};
    }
};

