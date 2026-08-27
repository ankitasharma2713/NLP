import nltk
from nltk.stem import WordNetLemmatizer

# Download required WordNet data
nltk.download("wordnet")
nltk.download("omw-1.4")

# Create lemmatizer object
lemmatizer = WordNetLemmatizer()

# Sample words with their parts of speech
words = [
    ("playing", "v"),
    ("played", "v"),
    ("studies", "v"),
    ("studying", "v"),
    ("better", "a"),
    ("cars", "n")
]

print("Lemmatization Results:\n")

# Apply lemmatization
for word, pos in words:
    lemma = lemmatizer.lemmatize(word, pos=pos)
    print(f"{word} -> {lemma}")