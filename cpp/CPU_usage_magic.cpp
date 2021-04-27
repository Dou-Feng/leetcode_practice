#include <windows.h>
#include <iostream>

using namespace std;

const double SPLIT = 0.01;
const int COUNT = 200;
const double PI = 3.14159265;
const int INTERVAL = 300;

int main() {
    for (int i = 0 ;i < 100; ++i) {
        cout <<  "i = " << i << ", CPU tick count = " << getCPUTickCount() << endl;
    }
    return 0;
}