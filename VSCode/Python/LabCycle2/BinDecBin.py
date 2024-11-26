num = input("Enter a decimal number: ")
i = int(num)
bin_s = ""
while i > 0:
    if i % 2 != 0:
        bin_s += '1'
    else:
        bin_s += '0'
    i = i // 2
bin_num = bin_s[::-1]
print(bin_num)
dec = 0
for i, j in enumerate(bin_num):
    dec += int(j) * (2 ** i) 
print(dec)
