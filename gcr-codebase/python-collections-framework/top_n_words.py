from collections import Counter

def top_n_words(text, n):
    words = text.split()
    return Counter(words).most_common(n)

print(top_n_words("great service great product", 2))