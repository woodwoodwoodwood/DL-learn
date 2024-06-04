#include<bits/stdc++.h>
using namespace std;

int main() {
    long long n, a;
    cin >> n;
    a = n;
    int s = 0;
    for(int i = n; i >= 1; i--) {
        for(int j = 0; j <= i; j++) {
            cout << " ";
        }
        for(int j = 0; j <= n - i; j++) {
            cout << j + 1 << " ";
        }
        for(int j = a - i; j >= 1; j--) {
            cout << j << " ";
        }
        cout << "\n";
    }
}