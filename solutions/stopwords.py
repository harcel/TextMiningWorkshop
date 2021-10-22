# stopwords is a set, so if you add stopwords yourself, they won't be duplicated.
length = [len(w) for w in stopwords]
longestword = list(stopwords)[length.index(max(length))]
print(f"The longest stopword is {longestword}")

orig_length = len(stopwords)
new_list = ["and", "market", "people"]
for nw in new_list: stopwords.add(nw)
print(f"The number of new words is {len(stopwords)-orig_length}")
