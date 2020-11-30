#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include "solution.hpp"



TEST_CASE("test1") {
    Solution sol = Solution();
    REQUIRE(sol.isMatch("aa", "a*") == true);
}

