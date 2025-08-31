# Autocomplete Demo

from utils import count_n_grams, estimate_probability, suggest_a_word, get_suggestions

# Example dataset
data = [
    ["i", "love", "nlp"],
    ["i", "love", "machine", "learning"],
    ["i", "enjoy", "learning"],
    ["i", "love", "python"],
    ["python", "is", "fun"],
    ["nlp", "is", "fun"]
]

# Build vocabulary
vocab = set([word for sentence in data for word in sentence])

# Train bigram and trigram counts
n = 2
n_gram_counts = count_n_grams(data, n)
n_plus1_gram_counts = count_n_grams(data, n+1)

print("Vocabulary:", vocab)
print("Bigram examples:", list(n_gram_counts.items())[:5])

# Try a prefix
prefix = ["i", "love"]

# Suggest one word
suggestion = suggest_a_word(prefix, n_gram_counts, n_plus1_gram_counts, vocab)
print("\nNext word suggestion:", suggestion)

# Get top-k suggestions
top_suggestions = get_suggestions(prefix, n_gram_counts, n_plus1_gram_counts, vocab, top_k=3)
print("\nTop suggestions:")
for word, prob in top_suggestions:
    print(f"{word}: {prob:.4f}")
