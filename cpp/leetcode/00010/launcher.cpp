#include <iostream>
#include <cassert>
#include "solution.hpp"


#define REQUIRE assert

int main() {
    Solution sol = Solution();
    REQUIRE(sol.isMatch("aa", "a*") == true);
    return 0;
}
