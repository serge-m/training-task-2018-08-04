#include <iostream>
#include <cassert>
#include "solution.hpp"


#define  REQUIRE assert

int main() {
    Solution sol{};
    if (0) {
        auto res = sol.findMedianSortedArrays(
                vector<int>{10, 20, 30, 40, 50, 60},
                vector<int>{5, 15, 100}
        );

        std::cout << "res " << res << "\n";
    }
    if (0) {
        auto res = sol.findMedianSortedArrays(
                vector<int>{10, 20, 30, 40, 50, 60},
                vector<int>{5, 15, 25}
        );

        std::cout << "res " << res << "\n";
    }
    if (0) {
        auto res = sol.findMedianSortedArrays(
                vector<int>{1, 1, 1, 10},
                vector<int>{2, 2, 3}
        );

        std::cout << "res " << res << "\n";
    }
    if (0) {
        auto res = sol.findMedianSortedArrays(
                vector<int>{1, 1, 1, 10},
                vector<int>{0, 0, 0}
        );

        std::cout << "res " << res << "\n";
    }
    if (1) {
        vector<int> rest{3,2, 0};


        Solution sol = Solution();
        REQUIRE(sol.findMedianSortedArrays(vector<int>{1, 3}, vector<int>{2}) == 2);
    }
    return 0;
}
