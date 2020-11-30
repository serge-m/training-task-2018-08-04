#include <algorithm>
#include <vector>
#include <utility>
#include <exception>
#include <iostream>
#include <iterator>

using std::vector;

struct Range {
    size_t start{0};
    size_t end{0};

    Range with_start(size_t start) const {
        return Range{start, this->end};
    }

    Range with_end(size_t end) const {
        return Range{this->start, end};
    }
};

size_t mid(const Range &range) {
    return (range.start + range.end) / 2;
}

std::ostream& operator<<(std::ostream &os, const vector<int>& v) {
    std::copy(v.begin(), v.end(), std::ostream_iterator<int>(std::cout, " "));
    return os;
}

void print_mid(vector<int> r, int32_t mid_idx) {
    try {
        std::cout << r.at(mid_idx);
    } catch (const std::out_of_range&) {
        std::cout << "null";
    }
    std::cout << " at idx: " << mid_idx << "\n";
}


class Solution {
public:
    double findMedianSortedArrays(const vector<int> &nums1, const vector<int> &nums2) {
        double target_idx = double(nums1.size() + nums2.size() - 1) / 2.;
        return findMedian(nums1, nums2, Range{0, nums1.size() + 1}, target_idx);
    }

public:
    double findMedian(const vector<int>& a, const vector<int>& b, Range range_a, double target_idx) {
        int32_t mid_a_idx = mid(range_a);
        int32_t mid_b_idx = int32_t(target_idx) - mid_a_idx;

        if (mid_b_idx < 0) {
            return findMedian(a, b, range_a.with_end(mid_a_idx), target_idx);
        }
        if (mid_b_idx > b.size()) {
            return findMedian(a, b, range_a.with_start(mid_a_idx), target_idx);
        }
        if (mid_a_idx == 0 || mid_b_idx == b.size() || a[mid_a_idx-1] <= b[mid_b_idx]) {
            if (mid_b_idx == 0 || mid_a_idx == a.size() || b[mid_b_idx-1] <= a[mid_a_idx]) {
                vector<int> rest;
                copy_at_most_2(a, mid_a_idx, rest);
                copy_at_most_2(b, mid_b_idx, rest);
                std::partial_sort(rest.begin(), rest.begin() + 2, rest.end());
                if (target_idx - trunc(target_idx) > 0.2) {
                    return (rest[0] + rest[1] ) / 2.;
                }
                return rest[0];
            } else {
                return findMedian(a, b, range_a.with_start(mid_a_idx), target_idx);
            }
        } else {
            return findMedian(a, b, range_a.with_end(mid_a_idx), target_idx);
        }
    }

    void copy_at_most_2(const vector<int> &source, size_t start, vector<int> &dest) const {
        for(size_t i = 0; i < 2 && start + i < source.size(); ++i)
            dest.push_back(source[start + i]);
    }
};



/*
 * range for a: t - len(b) ... t
 *    10,     20, 30, |40, 50, 60
 * 5,    | 15,                     100
 *
 *  1  1  | 1          10
 *             2 | 2 3
 *
 *  1  1    1  |        10
 *             | 2  2 3
 *  1  1      |  2   3
 *                        4 | 4 4

 *
 *                      |  1   1    1          10
 *              0 0 0   |
 *                       1   1  |  1          10
 *              0 |0 0

 *
 */
