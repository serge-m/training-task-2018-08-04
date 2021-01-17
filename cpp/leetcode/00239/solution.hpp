/*
239. Sliding Window Maximum
Hard

t=36

*/
#include <vector>
#include <algorithm>
#include <vector>
#include <set>

using std::vector;
using std::set;
using std::multiset;


class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        multiset<int> window{nums.begin(), nums.begin()+k};
        int n = nums.size();
        vector<int> result;
        for (int i = 0; i < n - k; ++i) {
            result.push_back(*window.rbegin());
            auto itr = window.find(nums[i]);
            window.erase(itr);
            window.insert(nums[i+k]);
        }
        result.push_back(*window.rbegin());
        return result;
    }
};