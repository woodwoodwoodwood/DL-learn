#include <bits/stdc++.h>
using namespace std;

// 将大于 10 的数字转换为大写字母
string convertToChar(int num) {
    if (num < 10) {
        return to_string(num); 
    } else {
        char letter = 'A' + (num - 10);
        return string(1, letter);
    }
}

int main() {
    int n;
    cin >> n;

    // 遍历每一行
    for (int i = 1; i <= n; ++i) {
        // 打印前导空格
        for (int j = 0; j < n - i; ++j) {
            cout << "  "; // 这里是两个空格
        }

        // 打印每行的数字和字母，升序部分
        for (int j = 1; j <= i; ++j) {
            cout << convertToChar(j) << " ";
        }

        // 打印每行的数字和字母，降序部分
        for (int j = i - 1; j >= 1; --j) {
            cout << convertToChar(j) << " ";
        }

        // 换行
        cout << "\n";
    }

    return 0;
}
