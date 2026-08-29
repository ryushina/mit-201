#include <iostream>
#include <type_traits>

int main() {
    int y = 1;
    char ch = 'A';
    long int year = 2026;
    double amount = 125.50;
    int zValue = 25;
    float quantity = 3.5F;
    int date = 29;
    double yield = 8.75;

    int* yAddr = &y;
    char* chAddr = &ch;
    long int* ptYr = &year;
    double* amt = &amount;
    int* z = &zValue;
    float* qp = &quantity;
    int* datePt = &date;
    double* yldAddr = &yield;

    static_assert(std::is_same_v<decltype(yAddr), int*>);
    static_assert(std::is_same_v<decltype(chAddr), char*>);
    static_assert(std::is_same_v<decltype(ptYr), long int*>);
    static_assert(std::is_same_v<decltype(amt), double*>);
    static_assert(std::is_same_v<decltype(z), int*>);
    static_assert(std::is_same_v<decltype(qp), float*>);
    static_assert(std::is_same_v<decltype(datePt), int*>);
    static_assert(std::is_same_v<decltype(yldAddr), double*>);

    std::cout << "yAddr -> " << *yAddr << '\n';
    std::cout << "chAddr -> " << *chAddr << '\n';
    std::cout << "ptYr -> " << *ptYr << '\n';
    std::cout << "amt -> " << *amt << '\n';
    std::cout << "z -> " << *z << '\n';
    std::cout << "qp -> " << *qp << '\n';
    std::cout << "datePt -> " << *datePt << '\n';
    std::cout << "yldAddr -> " << *yldAddr << '\n';
}
