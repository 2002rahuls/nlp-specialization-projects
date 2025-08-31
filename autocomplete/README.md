# Autocomplete using N-Gram Language Models

This project implements a simple **autocomplete system** using **n-gram language models** with add-k smoothing.

---

## 📚 Key Concepts

- Tokenization and vocabulary creation
- Counting n-grams and (n+1)-grams
- Add-k smoothing for probability estimation
- Suggesting next word predictions
- Getting top-k probable completions

---

## 🚀 Example Run

```python
from utils import count_n_grams, suggest_a_word, get_suggestions

data = [
    ["i", "love", "nlp"],
    ["i", "love", "machine", "learning"],
    ["i", "enjoy", "learning"],
    ["i", "love", "python"],
    ["python", "is", "fun"],
    ["nlp", "is", "fun"]
]

vocab = set([word for sentence in data for word in sentence])

n = 2
n_gram_counts = count_n_grams(data, n)
n_plus1_gram_counts = count_n_grams(data, n+1)

prefix = ["i", "love"]
print("Next word:", suggest_a_word(prefix, n_gram_counts, n_plus1_gram_counts, vocab))
print("Top 3:", get_suggestions(prefix, n_gram_counts, n_plus1_gram_counts, vocab, top_k=3))
```
