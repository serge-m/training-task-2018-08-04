#include <iostream>

using std::cout;
struct Stuff {
    int i;
    Stuff(): i(0) {
        cout << "Stuff default init, i=0" << "\n";
    }
    Stuff(int i): i(i) {
        cout << "Stuff init with i=" << i << "\n";
    }

    ~Stuff() {
        cout << "Stuff deinit, i=" << i << "\n";
    }
};
class Class
{
private:
    Stuff stuff{ 1 };

public:

    Class(int i) : stuff{ i }
    {
        cout << "Class init i=" << i << "\n";
    }

    Class()
    {
        cout << "Class init default" << "\n";
    }

    void print()
    {
        std::cout << "stuff.i: " << stuff.i << '\n';
    }

};

int main()
{
    Class c1{ 2 };
    c1.print();

    Class c2{};
    c2.print();

    return 0;
}