#include <iostream>
#include <cassert>
#include "solution.hpp"


void REQUIRE(bool x) {
    assert(x);
}

int main() {
    Solution sol = Solution();

    vector<int> nums;

    nums = std::vector<int>{-7,-8,7,5,7,1,6,0};
    REQUIRE(sol.maxSlidingWindow(nums, 4) == std::vector<int>{7,7,7,7,7});


    nums = std::vector<int>{1,3,-1,-3,5,3,6,7};
    REQUIRE(sol.maxSlidingWindow(nums, 3) == std::vector<int>{3,3,5,5,6,7});


    return 0;
}

