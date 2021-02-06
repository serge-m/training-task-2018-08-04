/*
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium
*/

#include <vector>
#include <set>
#include <iostream>
using namespace std;

class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        std::multiset<int> s;
        int start = 0;
        int end = 0;
        while (end < nums.size()) {
            s.insert(nums[end]);
            if (*s.rbegin() - *s.begin() > limit) {
                s.erase(s.find(nums[start]));
                start += 1;
            }
            end += 1;
        }
        return end - start;
    }
};


int main() {
    auto sol = Solution();
    vector<int> input = {6,5,4,3,2,1};
    auto result = sol.longestSubarray(input, 2);
    cout << result << "\n";
    return 0;
}