#include <iostream>
#include <cassert>
#include "solution.hpp"


void REQUIRE(bool x) {
    assert(x);
}

int main() {
    // memory for the lists is not released => memory leak
    Solution sol = Solution();

    vector<int> nums = std::vector<int>{2, 3, 1, 1, 4};
    REQUIRE(sol.jump(nums) == 2);


    return 0;
}
