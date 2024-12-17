N = int(input("Enter N: "))
print("Input each word: ")
words = [input() for i in range(N)]

words_sorted = sorted(words, key=len)
words_dict = {i: len(i) for i in words_sorted}

print(words_dict)
