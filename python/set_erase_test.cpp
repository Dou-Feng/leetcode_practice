#include <iostream>
#include <set>
using namespace std;


class A {
public:
    int a, b, c;
    A(int _a) : a(_a){}

    bool operator<(const A& elem) const {
        return a < elem.a;
    }

    ostream& operator<<(ostream& os) const {
        int p = (long long)(void*)this;
        os << p;
        return os;
    }
};

int main() {
    set<A> test_set;
    A a(1);
    A b(2);
    test_set.insert(a);
    test_set.insert(b);
    


    A c(3);
    test_set.erase(c);
    for (auto it : test_set) {
        cout << it.a << endl;
    }


    return 0;

}