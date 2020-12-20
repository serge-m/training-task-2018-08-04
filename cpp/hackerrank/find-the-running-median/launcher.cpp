#include <bits/stdc++.h>
#include <set>
#include <random>

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
    std::multiset<double> lower;
    std::multiset<double> higher;
    for(auto x : a) {
        if (results.empty() || x <= *lower.rbegin()) {
            lower.insert(x);
        }
        else {
            higher.insert(x);
        }

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

        if (lower.size() == higher.size()) {
            results.push_back((*lower.rbegin() + *higher.begin()) / 2.);
        }
        else if(lower.size() == higher.size() + 1) {
            results.push_back(*lower.rbegin());
        }
    }
    return results;
}

vector<double> runningMedianBySort(vector<int> a) {
    vector<double> results;
    results.reserve(a.size());
    for(size_t i = 0; i < a.size(); ++i) {
        sort(a.begin(), a.begin() + i + 1);

        size_t m = (i+1) / 2;
        if ((i + 1) %2 == 1 ) {
            results.push_back(a[m]);
        }
        else {
            results.push_back((a[m] + a[m-1]) / 2.);
        }
    }
    return results;
}

template<typename T>
vector<T> random_vector(int seed, size_t size, T min, T max) {
    std::seed_seq seed_{seed};
    default_random_engine engine{seed_};
    uniform_int_distribution<T> distribution{min, max};
    vector<T> v;
    v.reserve(size);
    generate_n(std::back_inserter(v), size, [&distribution, &engine]() {return distribution(engine);});
    return v;
}

int main__() {

    for (int size = 7; size < 20; ++ size) {
        auto v = random_vector(0, size, 0, size*10);

        cout << size << "\n";
        cout << v << "\n";
        const vector<double> &ans1 = runningMedian(v);
        const vector<double> &ans2 = runningMedianBySort(v);

        if (ans1 != ans2) {
            cout << ans2 << "\n";
            cout << ans1 << "\n";
            cout << "bad ! \n";
        }
        cout << "\n";
    }
    return 0;
}

int main()
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
