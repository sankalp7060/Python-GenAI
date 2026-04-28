def extract_context(paragraph, keyword):
    words = paragraph.split()
    for i, word in enumerate(words):
        if word.lower() == keyword.lower():
            start = max(0, i-5)
            end = min(len(words), i+6)
            print("Context:", " ".join(words[start:end]))

paragraph = "Python is powerful and widely used in data engineering and automation."
extract_context(paragraph, "data")