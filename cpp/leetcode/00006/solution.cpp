/*
6. ZigZag Conversion
Medium
*/


class Solution {
public:
    string convert(string s, int numRows) {
        if (s.size() < 2 || numRows < 2) {
            return s;
        }
        stringstream ss;
        int period = get_period(numRows);

        for (int row = 0; row < numRows; ++ row) {
            int idx_from_diag = (numRows - row - 1) * 2;
            for (int i = row; i < s.size(); i += period) {
                ss << s[i];
                if (row != 0 and row != numRows-1 && i + idx_from_diag < s.size()) {
                    ss << s[i + idx_from_diag];
                }
            }

        }
        return ss.str();
    }

    int get_period(int numRows) {
        return numRows * 2 - 2;
    }
};