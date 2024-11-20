const array = [1,2,3,4,5];

var x = parseInt(prompt("Enter the search term: "), 10);

function binarySearch(array, x) {
    let start = 0;
    let end = array.length - 1;
    
    while (start <= end) {
        let middle = Math.floor((start + end) / 2)
        if (x === array[middle])
            return middle;
        else if (x > array[middle])
            start = middle + 1;
        else if (x < array[middle])
            end = middle - 1;
    }
    return -1;
}

let y = binarySearch(array, x);
if (y !== -1)
    console.log("The search term was found at index: ", y);
else
  console.log("The search term was not found");
