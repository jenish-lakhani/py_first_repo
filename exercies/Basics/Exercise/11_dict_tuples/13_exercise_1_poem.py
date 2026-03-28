word_stats = {}

with open("poem.txt", "r") as f:
    for line in f:
        word = line.split(" ")
        for word in word:
            if word in word_stats:
                word_stats[word] += 1
            else:
                word_stats[word] = 1

print(word_stats)


word_occurance = list(word_stats.values())
max_count = max(word_occurance)
print("max occurance of any word is:", max_count)

print("word with max occurances are: ")
for word, count in word_stats.items():
    if count == max_count:
        print(word)
