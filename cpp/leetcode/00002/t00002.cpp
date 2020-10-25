#include <algorithm>
#include <iostream>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};



class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return add(0, l1, l2);
    }

private:
    ListNode* add(int current, ListNode *l1, ListNode* l2) {
        if (!l1) {
            std::swap(l1, l2);
        }

        if (!l1) {
            if (current==0) {
                return nullptr;
            }
            return new ListNode{current};
        }

        // l1 is not empty
        auto sum = current + l1->val;
        ListNode* l2_next = nullptr;
        if (l2) {
            sum += l2->val;
            l2_next = l2->next;
        }
        return new ListNode{
                sum % 10,
                add(sum / 10, l1->next, l2_next)
        };
    }
};



int main() {
    auto l1 = new ListNode(6,new ListNode(5));
    auto l2 = new ListNode(4,new ListNode(9));
    auto res = Solution().addTwoNumbers(l1, l2);

    while(res) {
        std::cout << res->val;
        res = res->next;
    }

}