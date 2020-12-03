#include "list_node.h"
#include <vector>

using std::vector;

class Solution {
public:
    void move_from_head_to_tail(ListNode *&dst_tail, ListNode *&src_head) {
        dst_tail->next = src_head;
        src_head = src_head->next;
        dst_tail = dst_tail->next;
    }

    ListNode *merge(ListNode *a, ListNode *b) {
        ListNode to_head{};
        ListNode *cur = &to_head;
        while (a != nullptr && b != nullptr) {
            if (a->val < b->val)
                move_from_head_to_tail(cur, a);
            else
                move_from_head_to_tail(cur, b);
        }

        while (a != nullptr) {
            move_from_head_to_tail(cur, a);
        }
        while (b != nullptr) {
            move_from_head_to_tail(cur, b);
        }

        return to_head.next;
    }

    // The function reuses the nodes from the input lists in the output.
    // Input lists are modified to save time and memory.
    ListNode *mergeKLists(vector<ListNode *> &lists) {

        if (lists.empty()) {
            return nullptr;
        }
        vector<ListNode *> dst{lists};
        while (dst.size() > 1) {
            vector<ListNode *> src{dst};
            dst.clear();
            for (int i = 1; i < src.size(); i += 2) {
                dst.push_back(merge(src[i - 1], src[i]));
            }
            if (src.size() % 2 == 1) {
                dst.push_back(src.back());
            }
        }
        return dst[0];
    }
};