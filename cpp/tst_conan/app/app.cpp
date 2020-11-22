#include <iostream>
#include <func_lib.h>

using namespace std;
int main() {
    for (auto x : {1, 2, 10}) {
        cout << "Square of " << x << " is " << func_square(x) << "\n";
    }
}

