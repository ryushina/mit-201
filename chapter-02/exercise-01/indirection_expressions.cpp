#include <cassert>
#include <iostream>

int main() {
    int x = 10;
    int y = 20;
    long yield = 30;
    double miles = 40.5;
    int m = 50;
    int date = 2026;
    double distance = 60.25;
    char tab = '\t';
    int hours = 8;

    int* xAddr = &x;
    int* yAddr = &y;
    long* ptYld = &yield;
    double* ptMiles = &miles;
    int* mptr = &m;
    int* pdate = &date;
    double* distPtr = &distance;
    char* tabPt = &tab;
    int* hoursPt = &hours;

    assert(*xAddr == x);
    assert(*yAddr == y);
    assert(*ptYld == yield);
    assert(*ptMiles == miles);
    assert(*mptr == m);
    assert(*pdate == date);
    assert(*distPtr == distance);
    assert(*tabPt == tab);
    assert(*hoursPt == hours);

    std::cout << "a. *xAddr   = " << *xAddr << '\n';
    std::cout << "b. *yAddr   = " << *yAddr << '\n';
    std::cout << "c. *ptYld   = " << *ptYld << '\n';
    std::cout << "d. *ptMiles = " << *ptMiles << '\n';
    std::cout << "e. *mptr    = " << *mptr << '\n';
    std::cout << "f. *pdate   = " << *pdate << '\n';
    std::cout << "g. *distPtr = " << *distPtr << '\n';
    std::cout << "h. *tabPt   = tab character\n";
    std::cout << "i. *hoursPt = " << *hoursPt << '\n';
}
