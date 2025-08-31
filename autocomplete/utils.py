import random

def count_n_grams(data, n, start_token='<s>', end_token='<e>'):
    """
    Count all n-grams in the dataset
    """
    n_grams = {}
    for sentence in data:
        sentence = [start_token] * n + sentence + [end_token]
        sentence = tuple(sentence)
        for i in range(len(sentence) - n + 1):
            n_gram = sentence[i:i+n]
            n_grams[n_gram] = n_grams.get(n_gram, 0) + 1
    return n_grams


def estimate_probability(word, previous_n_gram, n_gram_counts, n_plus1_gram_counts, vocab_size, k=1.0):
    """
    Estimate probability of a word given previous n-gram, with add-k smoothing
    """
    previous_n_gram = tuple(previous_n_gram)
    n_gram_count = n_gram_counts.get(previous_n_gram, 0)
    n_plus1_gram = previous_n_gram + (word,)
    n_plus1_count = n_plus1_gram_counts.get(n_plus1_gram, 0)

    probability = (n_plus1_count + k) / (n_gram_count + k * vocab_size)
    return probability


def suggest_a_word(previous_tokens, n_gram_counts, n_plus1_gram_counts, vocab, k=1.0):
    """
    Suggest the most probable next word given a list of previous tokens
    """
    n = len(list(n_gram_counts.keys())[0])
    previous_n_gram = previous_tokens[-n:]

    max_prob = -1
    suggestion = None
    for word in vocab:
        prob = estimate_probability(word, previous_n_gram, n_gram_counts, n_plus1_gram_counts, len(vocab), k)
        if prob > max_prob:
            max_prob = prob
            suggestion = word
    return suggestion


def get_suggestions(previous_tokens, n_gram_counts, n_plus1_gram_counts, vocab, k=1.0, top_k=5):
    """
    Return top_k suggestions sorted by probability
    """
    n = len(list(n_gram_counts.keys())[0])
    previous_n_gram = previous_tokens[-n:]

    probs = {}
    for word in vocab:
        prob = estimate_probability(word, previous_n_gram, n_gram_counts, n_plus1_gram_counts, len(vocab), k)
        probs[word] = prob
    
    sorted_words = sorted(probs.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_k]
