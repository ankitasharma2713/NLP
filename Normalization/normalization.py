import re

# Sample text
text = "  Hello!!! This is an NLP COURSE.   NLP is AMAZING!!!  "

# Convert text to lowercase
text = text.lower()

# Remove punctuation
text = re.sub(r"[^\w\s]", "", text)

# Remove extra spaces
text = " ".join(text.split())

# Display normalized text
print("Normalized Text:")
print(text)