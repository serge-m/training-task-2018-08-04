#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include "solution.hpp"

TEST_CASE("test1") {
    vector<int> expected = {1,2,3};
    vector<int> input = {2,7,11,15};
    Solution solution{};
    auto result = solution.twoSum(input, 9);
    REQUIRE(result == vector<int>{0, 1});

    input = {3,2,4};
    result = solution.twoSum(input, 6);
    REQUIRE(result == vector<int>{1, 2});

    input = {3,3};
    result = solution.twoSum(input, 6);
    REQUIRE(result == vector<int>{0, 1});
}
