#include <iostream>
#include <vector>
#include <algorithm>

bool isSorted(const std::vector<int>& arr) {
    for (size_t i = 1; i < arr.size(); ++i) {
        if (arr[i] < arr[i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    std::cin >> n;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            std::vector<int> temp = arr;  
            std::reverse(temp.begin() + i, temp.begin() + j + 1);

            if (isSorted(temp)) {
                std::cout << "Yes\n";
                return 0;
            }
        }
    }

    std::cout << "No\n";

    return 0;
}
