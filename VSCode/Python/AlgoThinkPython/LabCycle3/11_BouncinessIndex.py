h = int(input("Enter initial height in feet: "))
bi = float(input("Enter bounciness index: "))
n = int(input("Enter number of bounces: "))
total = h
current_height = h
for i in range(0,n):
    current_height *= bi
    total += 2 * current_height
total -= current_height
print(f"Total distance travelled: {total:.2f} feet")