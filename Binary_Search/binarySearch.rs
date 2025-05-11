use std::io;

fn main() {
    let mut input = String::new();
    println!("Enter the search term: ");
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let x: i32 = input.trim().parse().expect("Invalid input");
    let y = binary_search(x);
    if y == -1{
        println!("The search term was not found");
    } else {
        println!("The search term was found at index {}", y);
    }
}

fn binary_search(x: i32) -> i32 {
    let array: [i32; 5] = [1,2,3,4,5];
    let mut start: i32 = 0;
    let mut end: i32 = array.len() as i32 - 1;
    let mut middle: i32;
    while start <= end {
        middle = (start + end) / 2;
        if x == array[middle as usize]{
            return middle;
        } else if x > array[middle as usize] {
            start = middle + 1;
        } else if x < array[middle as usize] {
            end = middle - 1;
        }
    }
    return -1;
}
