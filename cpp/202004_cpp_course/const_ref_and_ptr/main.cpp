#include <iostream>

using namespace std;

int main() {
    int x = 5;
    const int MAX = 12;
    int &ref_x1 = x;
    const int &ref_x2 = x;


    const int *ptr1 = &x;
    ptr1 += 1; // ok
//    (*ptr1) += 1; //error: assignment of read-only location ‘* ptr1’
    int *const ptr2 = &x;
//    ptr2 += 1; // error: assignment of read-only variable ‘ptr2’
    (*ptr2) += 1;


    //Find which declarations are valid. If invalid, correct the declaration
    const int *ptr3 = &MAX;
    ptr3 += 1;
    cout << *ptr3;
//    int *ptr4 = &MAX ; // error: invalid conversion from ‘const int*’ to ‘int*’

    const int &r1 = ref_x1;
//    int &r2 = ref_x2 ; // error: binding reference of type ‘int&’ to ‘const int’ discards qualifiers

//    int *&p_ref1 = ptr1 ; // error: invalid conversion from ‘const int*’ to ‘int*’
    const int *&p_ref1 = ptr1; // ok
//    const int*&p_ref2 = ptr2 ; // error
    const int *const &p_ref2 = ptr2;
    return 0;
}