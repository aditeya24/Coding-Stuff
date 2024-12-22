n = int(input("Enter n: "))

print("Input 1st list: ")
list1 = [int(input()) for i in range(n)]
print("Input 2nd list: ")
list2 = [int(input()) for i in range(n)]

temp_list = list1 + list2
even_list = list(filter(lambda x: (x % 2 == 0), temp_list))
odd_list = list(filter(lambda x: (x % 2 != 0), temp_list)) 
final_list = even_list + odd_list

print(final_list)
