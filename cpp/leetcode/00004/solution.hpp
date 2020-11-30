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

    bool empty() const {
        return start >= end;
    }
};

size_t mid(const Range &range) {
    return (range.start + range.end) / 2;
}

struct VectRange {
    using elem_type = int;
    const vector<elem_type> &v;
    Range range;

    explicit VectRange(const std::vector<elem_type> &v) : v{v}, range{0, v.size()} {
    }

    explicit VectRange(const std::vector<elem_type> &v, size_t start, size_t end) : v{v}, range{start, end} {
    }

    size_t mid_idx() {
        return mid(range);
    }

    elem_type mid_val() {
        return v[mid_idx()];
    }

    VectRange with_start(size_t start) {
        return VectRange{v, start, range.end};
    }

    VectRange with_end(size_t end) {
        return VectRange{v, range.start, end};
    }
};


std::ostream& operator<<(std::ostream &os, const vector<int>& v) {
    std::copy(v.begin(), v.end(), std::ostream_iterator<int>(std::cout, " "));
    return os;
}

std::ostream& operator<<(std::ostream &os, const VectRange& r) {
    std::cout << "[" << r.range.start << "," << r.range.end << "] ";
    std::copy(r.v.begin(), r.v.end(),
              std::ostream_iterator<int>(std::cout, " "));
    return os;
}

void print_mid(const VectRange &r, int32_t mid_idx) {
    try {
        std::cout << r.v.at(mid_idx);
    } catch (const std::out_of_range&) {
        std::cout << "null";
    }
    std::cout << " at idx: " << mid_idx << "\n";
}


class Solution {
public:
    double findMedianSortedArrays(const vector<int> &nums1, const vector<int> &nums2) {
        double target_idx = double(nums1.size() + nums2.size() - 1) / 2.;
        return findMedian(VectRange{nums1, 0, nums1.size() + 1}, VectRange{nums2}, target_idx);
    }

public:
    double findMedian(VectRange a, VectRange b, double target_idx) {
        int32_t mid_a_idx = a.mid_idx();
        int32_t mid_b_idx = int32_t(target_idx) - mid_a_idx;
        std::cout << "a: " << a << "\n";
        std::cout << "b: " << b << "\n";

        std::cout << "a: ";
        print_mid(a, mid_a_idx);
        std::cout << "b: ";
        print_mid(b, mid_b_idx);

        if (mid_b_idx < 0) {
            return findMedian(a.with_end(mid_a_idx), b, target_idx);
        }
        if (mid_b_idx > b.v.size()) {
            return findMedian(a.with_start(mid_a_idx), b, target_idx);
        }
        if (mid_a_idx == 0 || mid_b_idx == b.v.size() || a.v[mid_a_idx-1] <= b.v[mid_b_idx]) {
            if (mid_b_idx == 0 || mid_a_idx == a.v.size() || b.v[mid_b_idx-1] <= a.v[mid_a_idx]) {
                vector<int> rest;
                for( size_t i = 0; i < 2 && mid_a_idx + i < a.v.size(); ++i)
                    rest.push_back(a.v[mid_a_idx + i]);
                for( size_t i = 0; i < 2 && mid_b_idx + i < b.v.size(); ++i)
                    rest.push_back(b.v[mid_b_idx + i]);
                std::partial_sort(rest.begin(), rest.begin() + 2, rest.end());
                if (target_idx - size_t(target_idx) > 0.1) {
                    return (rest[0] + rest[1] ) / 2.;
                }
                return rest[0];
            } else {
                return findMedian(a.with_start(mid_a_idx), b, target_idx);
            }
        } else {
            return findMedian(a.with_end(mid_a_idx), b, target_idx);
        }
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

/*
 * case a_0 < a_mid < b_mid < ... < b_end
 * a_0 ... a_mid ... a_end
 * b_0 ... b_mid ... b_end
 *
 * 5 + 5 - 1 / 2 = 4.5
 * 10,20,30,40,50
 * 35,35,35,35,35
 *
 * 10,20,30!40,50
 *
 *   case target_idx < a_mid_idx + b_mid_idx
 *   action: remove b_mid .. b_end they are too big
 *   else
 *   action: remove a_0 ... a..mid
 *
 *   case target_idx > a_mid_idx:
 *   action remove a_0..a_mid
 *   else
 *   remove a_mid..a_end
 * case b0 < ... < b_mid < a_min < ... < a_end
 *   case target_idx < a_mid_idx + b_mididx
 *   action: reomve a_mid ... a_end
 *
 *   otherwise: remove b_0 ... b_mid
 *
 *
 *
 * ------------------------
 *  0  1 2  3  4
 * 10,20,30,40,50
 *       |
 * 15,25,35,45,55
 *       |
 *
 * target = 4.5
 *
 */



