def reverse_words(sentence):
    return " ".join(word[::-1] for word in sentence.split())

print(reverse_words("Hello Python Developer"))