#include <bits/stdc++.h>

using namespace std;




void printbit(uint32_t n) {
    stack<int> bits;
    for (int i = 0; i < 32; ++i) {
        bits.push(n % 2);
        n >>= 1;
    }
    while (!bits.empty()) {
        cout << bits.top();
        bits.pop();
    }
    cout <<endl;
}
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t high_mask = 1 << 31, low_mask = 1;
        uint32_t h, l;
        for (int i = 0; i < 16; ++i) {
            printbit(n);
            l = (n & low_mask);
            h = (n & high_mask);
            n = n ^ l ^ h | (l << (31 - 2*i)) | (h >> (31 - 2*i));
            // cout <<"i = " << i << ", l = " << l << ", h = " << h << ", n = " << n << endl;
            low_mask <<= 1;
            high_mask >>= 1;   
        }
        return n;
    }
};

int main() {
    Solution sol;

    bool s = sol.reverseBits(4294967293u);
    cout << s << endl;
    return 0;
}