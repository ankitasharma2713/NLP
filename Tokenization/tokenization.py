import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
# Download tokenizer data
nltk.download("punkt")
nltk.download("punkt_tab")
text = """Natural Language Processing is a field of Artificial Intelligence.
It helps computers understand human language."""
# Word Tokenization
word_tokens = word_tokenize(text)
# Sentence Tokenization
sentence_tokens = sent_tokenize(text)
print("Original Text:")
print(text)

print("\nWord Tokens:")
for i, token in enumerate(word_tokens, start=1):
    print(f"{i}. {token}")

print("\nSentence Tokens:")
for i, sentence in enumerate(sentence_tokens, start=1):
    print(f"{i}. {sentence}")