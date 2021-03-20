/*
5. Longest Palindromic Substring
Medium

O(n^2)
space O(n)

*/




template<typename T>
ostream& operator<<(ostream&os, vector<T> v) {
    for (auto x: v) {
        os << x << ",";
    }
    return os;
}

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) {
            return "";
        }
        vector<int> pl_prev(s.size(), 0);
        vector<int> pl(s.size(), 0);
        pl_prev[0] = 1;

        int best_start=0, best_end=0;
        size_t best = 1;

        for(auto i = 1; i < s.size(); ++i ) {
            pl[i] = 1;
            if (s[i] == s[i-1]) {
                pl[i-1] = 2;
            }
            else {
                pl[i-1] = 0;
            }
            for (auto j = 0; j < i-1; ++j) {
                if (s[i] == s[j] && pl_prev[j+1] != 0) {
                    pl[j] = pl_prev[j+1] + 2;
                } else {
                    pl[j] = 0;
                }

            }
            auto max_el_idx = std::max_element(pl.begin(), pl.begin()+i+1) - pl.begin();
            if (pl[max_el_idx] > best) {
                best = pl[max_el_idx];
                best_start = max_el_idx;
                best_end = i;
            }

            //cout << "prev " << pl_prev << "\n";
            //cout << "pl   " << pl << "\n";
            std::swap(pl_prev, pl);
        }

        return s.substr(best_start, best_end - best_start + 1);
    }
};


/*
pl[i][j] = len of palindrome s[j:i+1] or 0 if it is not
cbbcbb
112411

*/