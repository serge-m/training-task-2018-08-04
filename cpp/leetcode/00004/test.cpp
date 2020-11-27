#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include "solution.hpp"



TEST_CASE("test1_short") {
    Solution sol = Solution();
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1,2,3}, vector<int>{}) == 2);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1,2}, vector<int>{3}) == 2);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1,3}, vector<int>{2}) == 2);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{2,3}, vector<int>{1}) == 2);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{}, vector<int>{1,2,3}) == 2);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{3}, vector<int>{1,2}) == 2);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{2}, vector<int>{1,3}) == 2);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1}, vector<int>{2,3}) == 2);
}


TEST_CASE("test1_medium") {
    Solution sol = Solution();
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1,2,3,4,5,6,7}, vector<int>{}) == 4);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{2,3,4,5,6,7}, vector<int>{1}) == 4);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1,3,4,5,6,7}, vector<int>{2}) == 4);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1,2,4,5,6,7}, vector<int>{3}) == 4);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1,2,3,5,6,7}, vector<int>{4}) == 4);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1,2,3,4,6,7}, vector<int>{5}) == 4);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1,2,3,4,5,7}, vector<int>{6}) == 4);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1,2,3,4,5,6}, vector<int>{7}) == 4);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{3,4,5,6}, vector<int>{1,2, 7}) == 4);
}



TEST_CASE("test2_") {
    Solution sol = Solution();
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1,2,3,4,5,6,7}, vector<int>{}) == 4);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{1,2,3,4,5,6,7}, vector<int>{8}) == 4.5);
    REQUIRE(sol.findMedianSortedArrays(vector<int>{3,4,4,4}, vector<int>{1,2, 7}) == 4);
}

TEST_CASE("test2_complex") {
    Solution sol = Solution();
    REQUIRE(sol.findMedianSortedArrays(
            vector<int>{    3,4,5,  7},
            vector<int>{1,2,      6,  8}
    ) == 4.5);
    REQUIRE(sol.findMedianSortedArrays(
            vector<int>{    3,4,    7},
            vector<int>{1,2,    5,6,  8}
    ) == 4.5);
}

TEST_CASE("test3_complex") {
    Solution sol = Solution();
    REQUIRE(sol.findMedianSortedArrays(
            vector<int>{    3,  5,  7},
            vector<int>{1,2,  4,  6,  8}
    ) == 4.5);

    REQUIRE(sol.findMedianSortedArrays(
            vector<int>{    4,      },
            vector<int>{4,4,  4,5,6,7,  1231238}
    ) == 4.5);
}
