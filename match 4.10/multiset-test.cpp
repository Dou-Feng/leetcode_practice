#include <bits/stdc++.h>

using namespace std;

multiset<int> ms;

void print() {
    for (auto& e : ms) {
        cout << e << ", ";
    }
    cout << endl;
}

int main() {
    ms.insert(1);
    ms.insert(1);
    ms.insert(2);
    ms.insert(3);
    print();

    ms.erase(1);
    print();
    ms.insert(1);
    ms.insert(1);
    ms.erase(ms.find(1));
    print();
    return 0;
}
