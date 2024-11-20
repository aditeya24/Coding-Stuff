array = [1,2,3,4,5]

x = IO.gets("Enter the search term: \n")
x = String.to_integer(String.trim(x))

start = 0
last = length(array) - 1

defmodule BinarySearch do
  def binary_search(array, x, start, last) do
    if start <= last do 
        middle = div(start + last, 2)
        middle_ = Enum.at(array, middle)
        cond do
            x == middle_ ->
                middle
            x > middle_ ->
                binary_search(array, x, middle + 1, last)
            x < middle_ ->
                binary_search(array, x, start, middle - 1)
        end
    else
      -1
    end
  end
end




y = BinarySearch.binary_search(array, x, start, last)
if y != -1 do
    IO.puts("The search term was found at index #{y}")
else
    IO.puts("The search term was not found")
end
