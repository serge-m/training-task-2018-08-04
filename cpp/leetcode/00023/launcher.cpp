#include <iostream>
#include <cassert>
#include "list_node.h" // must go before solution definition
#include "solution.hpp"
#include <iterator>


void REQUIRE(bool x) {
    assert(x);
}

int main() {
    // memory for the lists is not released => memory leak
    Solution sol = Solution();
    vector<ListNode *> lists;

    lists = vector<ListNode *>{};
    REQUIRE(as_vector(sol.mergeKLists(lists)) == vector<int>{});

    lists = vector<ListNode *>{make_list(1, 2, 3)};
    REQUIRE(as_vector(sol.mergeKLists(lists)) == vector<int>{1, 2, 3});


    lists = vector<ListNode *>{make_list(1, 2, 3), make_list(2, 3, 4)};
    REQUIRE(as_vector(sol.mergeKLists(lists)) == vector<int>{1, 2, 2, 3, 3, 4});

    lists = vector<ListNode *>{make_list(1, 2, 3), make_list(2, 3, 4), make_list(0, 100)};
    REQUIRE(as_vector(sol.mergeKLists(lists)) == vector<int>{0, 1, 2, 2, 3, 3, 4, 100});


    return 0;
}
