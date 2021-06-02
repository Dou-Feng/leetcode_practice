#include <bits/stdc++.h>
#include <iostream>

using namespace std;
#define ll long long

int gcd(ll a, ll b) {
  while(b^=a^=b^=a%=b);
  return a;
}

int main() {
  ll a, b;
  cin >> a >> b;
  cout << gcd(a, b) << endl;
  return 0;
}

