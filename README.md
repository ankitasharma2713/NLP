# Natural Language Processing (NLP)

This repository contains Python implementations and practical demonstrations of fundamental **Natural Language Processing (NLP)** techniques using the **Natural Language Toolkit (NLTK)**.

The purpose of this repository is to understand basic NLP text preprocessing techniques through simple Python programs, code demonstrations, outputs, and explanations.

---

## 📚 Topics Covered

### 1. Tokenization

Tokenization is the process of breaking text into smaller units called **tokens**, such as words or sentences.

**Includes:**
- Word Tokenization
- Sentence Tokenization
- Python implementation using NLTK
- CodeSnap image
- Output
- Explanation

📁 [View Tokenization](./Tokenization)

---

### 2. Normalization

Text normalization converts raw text into a cleaner and more consistent form before further NLP processing.

**Includes:**
- Lowercase conversion
- Tokenization
- Punctuation removal
- Stopword removal
- Python implementation using NLTK
- CodeSnap image
- Output
- Explanation

📁 [View Normalization](./Normalization)

---

### 3. Stemming

Stemming reduces words to their common root or stem by removing prefixes or suffixes.

**Includes:**
- Porter Stemmer
- Word stemming examples
- Python implementation using NLTK
- CodeSnap image
- Output
- Explanation

📁 [View Stemming](./Stemming)

---

### 4. Lemmatization

Lemmatization converts words into their meaningful base or dictionary form using linguistic information such as the part of speech.

**Includes:**
- WordNet Lemmatizer
- Noun, verb, and adjective examples
- Python implementation using NLTK
- CodeSnap image
- Output
- Explanation

📁 [View Lemmatization](./Lemmatization)

---

## 🔄 NLP Preprocessing Flow

The techniques demonstrated in this repository can be understood as a basic text preprocessing workflow:

```text
Raw Text
   ↓
Tokenization
   ↓
Normalization
   ↓
Stemming / Lemmatization
   ↓
Processed Text
````

---

## 🛠️ Technologies Used

* **Python**
* **NLTK (Natural Language Toolkit)**
* **Visual Studio Code**
* **CodeSnap**

---

## 📂 Repository Structure

```text
NLP/
│
├── Tokenization/
│   ├── tokenization.py
│   ├── Tokenization_CodeSnap.jpeg
│   ├── Tokenization_Output.png
│   └── README.md
│
├── Normalization/
│   ├── normalization.py
│   ├── Normalization_CodeSnap.jpeg
│   ├── Normalization_Output.png
│   └── README.md
│
├── Stemming/
│   ├── stemming.py
│   ├── Stemming_CodeSnap.jpeg
│   ├── Stemming_Output.png
│   └── README.md
│
└── Lemmatization/
    ├── lemmatization.py
    ├── Lemmatization_CodeSnap.jpeg
    ├── Lemmatization_Output.png
    └── README.md
```

---

## ⚙️ Installation

Install Python and NLTK before running the programs.

```bash
pip install nltk
```

Run any Python file using:

```bash
python filename.py
```

For example:

```bash
python Tokenization/tokenization.py
```

---

## 🎯 Objective

The objective of this repository is to demonstrate fundamental NLP preprocessing concepts through practical Python implementations and make the concepts easy to understand through code, output, and explanations.

---

## 👩‍🏫 Academic Work

This repository contains practical work related to the **Natural Language Processing (NLP)** course.

**Instructor:** Ankita Sharma

---

## 📌 Conclusion

These fundamental preprocessing techniques form the foundation of many NLP applications, including text classification, sentiment analysis, information retrieval, search systems, and other language-processing tasks.

````

### What the main GitHub page will look like

```text
NLP
│
├── 📁 Tokenization
├── 📁 Normalization
├── 📁 Stemming
└── 📁 Lemmatization
````

And when someone opens the repository, the README immediately explains **what the repository contains, what each folder does, the workflow, technologies, and how to run the code**.

One small recommendation: keep the instructor line as **“Instructor: Ankita Sharma”** only if that is how Ma'am wants her name represented publicly on the repository.
