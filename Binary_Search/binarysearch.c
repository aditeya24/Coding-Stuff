#include <stdio.h>

int binarySearch(int x);

int main() {
    int x;
    printf("Enter the search term: \n");
    scanf("%d", &x);
    int y = binarySearch(x);
    if(y == -1)
        printf("The search term was not found\n");
    else
        printf("The search term was found at index %d \n", y);
    return 0;
} 

int binarySearch(int x) {
    int array[] = {1,2,3,4,5};
    int start = 0, end = sizeof(array) - 1;
    while (start <= end) {
        int middle = (start + end) / 2;
        if(x == array[middle])
            return middle;
        else if(x > array[middle])
            start = middle + 1;
        else if(x < array[middle])
            end = middle - 1;
    }
    return -1;
}
