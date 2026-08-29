import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")

# Sample sentence
text = "Natural Language Processing is very interesting"

# Tokenize the sentence
tokens = word_tokenize(text)

# Generate Unigrams
unigrams = list(ngrams(tokens, 1))

# Generate Bigrams
bigrams = list(ngrams(tokens, 2))

# Generate Trigrams
trigrams = list(ngrams(tokens, 3))

# Display tokens
print("Tokens:")
print(tokens)

# Display Unigrams
print("\nUnigrams:")
for i, gram in enumerate(unigrams, start=1):
    print(f"{i}. {' '.join(gram)}")

# Display Bigrams
print("\nBigrams:")
for i, gram in enumerate(bigrams, start=1):
    print(f"{i}. {' '.join(gram)}")

# Display Trigrams
print("\nTrigrams:")
for i, gram in enumerate(trigrams, start=1):
    print(f"{i}. {' '.join(gram)}")