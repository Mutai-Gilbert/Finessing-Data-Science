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

stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list

stopwords_set = set(stopwords_list)
"zip" in stopwords_set

from matplotlib import pyplot as pyplot

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title("Nominal GDP")
plt.ylabel("Billions of $")
plt.show()