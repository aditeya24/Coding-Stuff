num = input("Enter a 3 digit number: ")

ar_num = 0
i = 0
while i < len(num):
	ar_num += int(num[i]) ** 3
	i += 1
if int(num) == ar_num:
	print(f"{num} is an Armstrong number.")
else:
	print(f"{num} is not an Armstrong number.")
