#include <catch2/catch.hpp>
#include <func_lib.h>

TEST_CASE("catch_test1", "[42][theAnswer]") {
    int expected = 100;
    int result = func_square(10);
    REQUIRE(result == expected);
}

TEST_CASE("catch_test2", "[42][haha]") {
    int expected = 9;
    int result = func_square(3);
    REQUIRE(result == expected);
}