$array = Array[1,2,3,4,5]

puts "Enter the search term: "
x = gets.to_i

def binarySearch(x)
    a, b = 0, $array.length - 1
    while a <= b do
        middle = (a + b) / 2
        if x == $array[middle]
            return middle
        elsif x > $array[middle]
            a = middle + 1
        elsif x < $array[middle]
            b = middle - 1
        end
    end
    return -1
end

y = binarySearch(x)
if y != -1
    puts "The search term was found at index "+ y.to_s
else
    puts "The search term was not found"
end
