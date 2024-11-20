#include <iostream>
using namespace std;

int binarySearch(int x);

int main() {
    int x;
    cout << "Enter the search term: ";
    cin >> x;
    int y = binarySearch(x);
    if(y == -1)
        cout << "\nThe search term was not found";
    else {
        cout << "\nThe search term was found at index " << y;
    }
    return 0;
}

int binarySearch(int x) {
    int array[] = {1,2,3,4,5};
    int start = 0, end = sizeof(array) - 1;
    while (start <= end) {
        int middle = (start + end) / 2;
        int a = array[middle];
        if (x == a)
            return middle;
        else if (x > a)
            start = middle + 1;
        else if (x < a)
            end = middle - 1;
    }
    return -1;
}
