#include <utility>
#include <iostream>

void print(int &x) {
    std::cout << "print(int&)" << std::endl;
}

void print(const int &x) {
    std::cout << "print(const int&)" << std::endl;
}

#define rv_ref
#ifdef rv_ref

void print(int &&x) {
    std::cout << "print(int &&)" << std::endl;
}

#endif

int main() {
    int x = 10;


    int &ref = x;  //l-value reference
    print(x);

    print(static_cast<int&&>(x));

    print(x+4);
    print(std::move(x));
    print(ref+4);

    print(3); //binds to void print(int &&x) if available
    return 0;
}
