from nltk.stem import PorterStemmer

# Create stemmer object
stemmer = PorterStemmer()

# Sample words
words = [
    "playing",
    "played",
    "plays",
    "studies",
    "studying",
    "studied"
]

print("Stemming Results:\n")

# Apply stemming
for word in words:
    stem = stemmer.stem(word)
    print(f"{word} -> {stem}")