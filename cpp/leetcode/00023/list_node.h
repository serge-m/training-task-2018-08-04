#ifndef LEETCODE_SOL_LIST_NODE_H
#define LEETCODE_SOL_LIST_NODE_H
#include <vector>


struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


template<typename ... ArgTypes>
ListNode* make_list(ArgTypes ...args);

template<typename T, typename ... ArgTypes>
ListNode* make_list(T t, ArgTypes... args) {
    return new ListNode(t, make_list(args...));
}

template<>
ListNode* make_list() {
    return nullptr;
}

std::vector<int> as_vector(ListNode* list) {
    std::vector<int> result;
    while(list != nullptr) {
        result.push_back(list->val);
        list = list->next;
    }
    return result;
}

#endif //LEETCODE_SOL_LIST_NODE_H
