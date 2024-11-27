h = int(input("Enter initial height in feet: "))
bi = float(input("Enter bounciness index: "))
n = int(input("Enter number of bounces: "))
total = h
current_height = h * bi
for i in range(0,n):
    total += 2 * current_height
    current_height *= bi
print(f"Total distance travelled: {total:.2f} feet")