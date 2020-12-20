#include <bits/stdc++.h>
#include <set>
using namespace std;

/*
 * Complete the runningMedian function below.
 */
/*
123 45
123 456
1234 56
*/

template<typename T>
ostream& operator<<(ostream &os, const set<T>& a) {
    for (auto x: a) {
        os << x << " ";
    }
    return os;
}


template<typename T>
ostream& operator<<(ostream &os, const vector<T>& a) {
    for (auto x: a) {
        os << x << " ";
    }
    return os;
}

vector<double> runningMedian(vector<int> a) {
    vector<double> results;
    results.reserve(a.size());
    std::set<double> lower;
    std::set<double> higher;
    for(auto x : a) {
        // cout << x << ":\n" << std::flush;
        // cout << "0 lower " << lower << " higher " << higher << "\n" << std::flush;
        if (results.empty() || x <= *lower.rbegin()) {
            lower.insert(x);
        }
        else {
            higher.insert(x);
        }
        // cout << "1 lower " << lower << " higher " << higher << "\n" << std::flush;

        if (lower.size() > higher.size() + 1) {
            auto it_largest = std::prev(lower.end());
            higher.insert(*it_largest);
            lower.erase(it_largest);
        }
        else if (higher.size() > lower.size()) {
            auto it_smallest = higher.begin();
            lower.insert(*it_smallest);
            higher.erase(it_smallest);
        }
        // cout << "2 lower " << lower << " higher " << higher << "\n" << std::flush;

        if (lower.size() == higher.size()) {
            results.push_back((*lower.rbegin() + *higher.begin()) / 2.);
        }
        else if(lower.size() == higher.size() + 1) {
            results.push_back(*lower.rbegin());
        }
        else {
            // std::cout << "bad size res " << lower.size() << " " << higher.size() << "\n";
        }
    }
    return results;
}

int main() {

    vector<int> a{1,2,3,4,5,6,7};
    vector<double> result = runningMedian(a);

    cout << result << "\n";
}

int main_()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int a_count;
    cin >> a_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<int> a(a_count);

    for (int a_itr = 0; a_itr < a_count; a_itr++) {
        int a_item;
        cin >> a_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        a[a_itr] = a_item;
    }

    vector<double> result = runningMedian(a);

    fout << std::fixed << std::setprecision(1);
    for (int result_itr = 0; result_itr < result.size(); result_itr++) {
        fout << result[result_itr];

        if (result_itr != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}
