N = int(input("Enter N: "))
print("Input words: ")
words = [input() for i in range(N)]
#words_dict = {i: len(words[i]) for i in range(N)}
words_sorted = sorted(words)
words_length = [len(words_sorted[i]) for i in range(N)]
for i in range(N):
    print(f"{words_sorted[i]}  {words_length[i]}")
