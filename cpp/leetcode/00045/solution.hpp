#include <vector>
#include <algorithm>

using std::vector;

class Solution {
public:
    int jump(vector<int> &nums) {
        size_t n = nums.size();
        auto max_cnt = std::numeric_limits<int>::max();
        vector<int> jumps(n, max_cnt);
        jumps[0] = 0;
        for (size_t i = 0; i < n; ++i) {
            auto new_val = jumps[i] + 1;
            auto last_jump = std::min<int>(i + nums[i], n - 1);
            for (auto j = i + 1; j < last_jump + 1; ++j) {
                if (jumps[j] > new_val) {
                    jumps[j] = new_val;
                }
                if (j == n - 1) {
                    return jumps[n - 1];
                }
            }
        }
        return jumps[n - 1];
    };
};