# defaultdict

word_count = {}
for word in document:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

word_counts = {}

for word in document:
    try:
        word_counts[word] += 1
    except  KeyError:
        word_counts[word] = 1



from collections import defaultdict

word_count = defaultdict(int)
for word in document:
    word_counts[word] += 1


from collections import Counter

c = Counter([0, 1, 2, 0])

print(c)