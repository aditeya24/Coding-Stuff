set1 = set(map(int, input("Enter set1 elements with spaces: ").split()))
set2 = set(map(int, input("Enter set2 elements with spaces: ").split()))

union = set1 | set2
intersection = set1&set2
diff_a = set1 - set2
diff_b = set2 - set1
sym_diff = set1 ^ set2

print(f"Union: {union}\nIntersection: {intersection}\nDifference A-B: {diff_a}\nDifference B-A: {diff_b}\nSymmetric Difference: {sym_diff}")
