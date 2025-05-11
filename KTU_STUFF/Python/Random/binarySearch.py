array = [1,2,3,4,5]

x = input("Enter the search term: ")
x = int(x)


def binarySearch():
    start = 0
    end = len(array) - 1

    while start <= end:
        middle = (start + end) // 2
        if x == array[middle] :
            return "found at index "+str(middle)
            exit()
        elif x > array[middle]:
            start = middle + 1
        elif x < array[middle]:
            end = middle - 1
    return "not found"

y= binarySearch()
print("The search term was "+y)