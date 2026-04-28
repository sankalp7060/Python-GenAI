import unicodedata

def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c))

print(remove_accents("Crème brûlée à la carte"))