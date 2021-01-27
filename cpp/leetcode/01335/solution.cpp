/*
1335. Minimum Difficulty of a Job Schedule
Hard

second time
t = 35
*/

#include <utility>
#include <functional>
#include <vector>
#include <unordered_map>
#include <cassert>

using std::pair;
using std::hash;
using std::vector;
using std::unordered_map;
using std::make_pair;

struct hash_pair {
    template <class T1, class T2>
    size_t operator()(const pair<T1, T2>& p) const
    {
        auto hash1 = hash<T1>{}(p.first);
        auto hash2 = hash<T2>{}(p.second);
        return hash1 ^ hash2;
    }
};


class Solution {
    static const int no_sol{-1};
    using arr = vector<int>;
    unordered_map<pair<int,int>, int, hash_pair> cache{};
public:

    int minDifficulty(vector<int>& jobDifficulty, int d) {
        if (d==0) {
            return no_sol;
        }
        return search(jobDifficulty, 0, d);
    }

private:
    int search(arr& a, int start, int num_days) {
        if (start + num_days > a.size()) {
            return no_sol;
        }
        auto c = cache.find(std::make_pair(start, num_days));
        if (c != cache.end()) {
            return c->second;
        }
        if (num_days == 1) {
            return *std::max_element(a.begin() + start, a.end());
        }

        int best = no_sol;
        auto max_in_day = a[start];
        for(int i = start; i < a.size(); ++ i) {
            max_in_day = std::max(max_in_day, a[i]);
            auto r = search(a, i+1, num_days-1);
            if (r != no_sol) {
                if (best==no_sol || best > r + max_in_day) {
                    best = r + max_in_day;
                }
            }

        }
        cache[make_pair(start, num_days)] = best;
        return best;
    }
};

int main() {
    auto sol = Solution();
    vector<int> input = {6,5,4,3,2,1};
    auto result = sol.minDifficulty(input, 2);
    assert(result == 7);
}