s = input("Enter string: ")

s_list = list(set(s.split(' ')))
s_sorted = sorted(s_list)

print(*s_sorted)
