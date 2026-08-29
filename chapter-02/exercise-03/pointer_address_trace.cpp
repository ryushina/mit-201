#include <cassert>
#include <iostream>

int main() {
    int years = 0;
    int m = 0;
    double amt = 0.0;
    int firstnum = 154;
    int slope = 0;
    int k = 0;

    int* ptNum = nullptr;
    double* amtAddr = nullptr;
    int* zAddr = &slope;
    int* numAddr = &firstnum;
    int* ptDay = nullptr;
    int* ptYr = &years;

    ptNum = &m;
    amtAddr = &amt;
    *zAddr = 25;
    k = *numAddr;
    ptDay = zAddr;
    *ptYr = 1987;
    *amtAddr = *numAddr;

    assert(ptNum == &m);
    assert(amtAddr == &amt);
    assert(slope == 25);
    assert(k == 154);
    assert(ptDay == &slope);
    assert(years == 1987);
    assert(amt == 154.0);

    std::cout << "Illustrated final data from the presentation:\n";
    std::cout << "ptNum = 8096\n";
    std::cout << "amtAddr = 16256\n";
    std::cout << "zAddr = 20492\n";
    std::cout << "numAddr = 18938\n";
    std::cout << "ptDay = 20492\n";
    std::cout << "ptYr = 694\n";
    std::cout << "years = " << years << '\n';
    std::cout << "amt = " << amt << '\n';
    std::cout << "firstnum = " << firstnum << '\n';
    std::cout << "slope = " << slope << '\n';
    std::cout << "k = " << k << '\n';
}
