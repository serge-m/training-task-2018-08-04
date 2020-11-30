#include <string>

using std::string;
class Solution {
public:
    bool isMatch(string s, string p) {
        return match(s, s.size() - 1, p, p.size() - 1);
    }

    bool match(const string& s, int last_s, const string& p, int last_p ) {
        if (last_p == -1) {
            return last_s == -1;
        }
        auto pc = p[last_p];
        if (pc == '*') {
            --last_p ;
            pc = p[last_p];
            if (match(s, last_s, p, last_p - 1)) {
                return true;
            }
            while(last_s >= 0 && (pc == '.' || s[last_s] == pc)) {
                if (match(s, last_s-1, p, last_p-1)) {
                    return true;
                }
                --last_s;
            }
            return false;
        }
        if (pc == '.') {
            if (last_s == -1) {
                return false;
            }
            return match(s, last_s - 1, p, last_p - 1);
        }

        if (last_s < 0) {
            return false;
        }
        return (pc == s[last_s]) && match(s, last_s - 1, p, last_p - 1);

    }
};