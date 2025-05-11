package main
import ("fmt")

func main() {
    var x, y int
    fmt.Println("Enter the search term: ")
    fmt.Scanln(&x)
    y = binarySearch(x)
    if y != -1 {
            fmt.Printf("The search was found at index %d \n", y)
    } else {
    fmt.Println("The search term was not found")
    }
}

func binarySearch(x int) int {
    array := []int{1,2,3,4,5}
    var  a, b, middle int = 0, len(array) - 1, 0
    for a <= b {
        middle = (a + b) / 2
        if x == array[middle] {
            return middle
        } else if x > array[middle] {
            a = middle + 1
        } else if x < array[middle] {
            b = middle - 1
        }
    }
    return -1
}
