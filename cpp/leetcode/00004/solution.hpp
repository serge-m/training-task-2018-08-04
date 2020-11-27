#include <algorithm>
#include <vector>
#include <utility>

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

    size_t len() const {
        return range.end - range.start;
    }
};


class Solution {
public:
    double findMedianSortedArrays(const vector<int> &nums1, const vector<int> &nums2) {
        double target_idx = double(nums1.size() + nums2.size() - 1) / 2.;
        return findMedian(VectRange{nums1}, VectRange{nums2}, target_idx);
    }

public:
    double findMedian(VectRange a, VectRange b, double target_idx) {
        if (a.range.empty()) {
            return ith_elem(b, target_idx - a.range.start);
        }
        if (b.range.empty()) {
            return ith_elem(a, target_idx - b.range.start);
        }
        if (a.len() + b.len() < 5) {
            vector<int> sum;
            for( int i = a.range.start; i < a.range.end; ++ i) {
                sum.push_back(a.v[i]);
            }
            for( int i = b.range.start; i < b.range.end; ++ i) {
                sum.push_back(b.v[i]);
            }
            std::sort(sum.begin(), sum.end());
            return findMedian(VectRange(sum), VectRange(vector<int>{}), target_idx-a.range.start-b.range.start);

        }
        if (a.mid_val() < b.mid_val()) {
            return findMedianInSorted(a, b, target_idx);
        }
        else {
            return findMedianInSorted(b, a, target_idx);
        }


    }

    double ith_elem(const VectRange &b, double target_in_b) const {
        size_t target_start = target_in_b;
        size_t target_end = target_start;
        if (target_in_b - target_start > 0.1) {
            target_end = target_start + 1;
        }
        return (b.v[target_start] + b.v[target_end]) / 2.;
    }

    double findMedianInSorted(VectRange a, VectRange b, double target_idx) {
        size_t a_mid_idx = a.mid_idx();
        size_t b_mid_idx = b.mid_idx();
        if (target_idx <= a_mid_idx + b_mid_idx) {
            return findMedian(a, b.with_end(b_mid_idx), target_idx);
        } else {
            return findMedian(a.with_start(a_mid_idx), b, target_idx);
        }
    }

};


/*
 * case a_0 < a_mid < b_mid < ... < b_end
 * a_0 ... a_mid ... a_end
 * b_0 ... b_mid ... b_end
 *   case target_idx < a_mid_idx + b_mid_idx
 *   action: remove b_mid .. b_end they are too big
 *
 *   case target_id > a_min_idx + b_mid_idx
 *   action: remove a_0 ... a..mid
 *
 * case b0 < ... < b_mid < a_min < ... < a_end
 *   case target_idx < a_mid_idx + b_mididx
 *   action: reomve a_mid ... a_end
 *
 *   otherwise: remove b_0 ... b_mid
 *
 *
 */



