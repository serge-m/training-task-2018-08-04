#include <iostream>

int main() {
    using namespace std;
    int a1;

    std::cout << "uninitialized " << a1 << std::endl;

    char d1[10];
    cout << "d1\n";
    for (auto c: d1) {
        cout << int(c) << " ";
    }
    cout << "\n";

    char d2[1000] = {'a'};
    cout << "d2\n";
    for (auto c: d2) {
        cout << int(c) << " ";
    }
    cout << "\n";

    char d3[1000] = {"asdasdaa"};
    cout << "d3\n";
    for (auto c: d3) {
        cout << int(c) << " ";
    }
    cout << "\n";

    char d4[1000]{"asdasdaa"};
    cout << "d4\n";
    for (auto c: d4) {
        cout << int(c) << " ";
    }
    cout << "\n";

    int *p = new int;
    cout << "*p: " << *p << "\n"; // UB?


    return 0;
}
