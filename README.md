# NLP Specialization Projects

This repository contains my implementations of key projects from the **Natural Language Processing Specialization** on Coursera.  
So far, I have completed **Autocomplete**, **Autocorrect**, and **RNN-based Text Generation**, with more projects to come as I progress.

---

## 🔹 Completed Projects

### 1. [Autocomplete](./autocomplete/)
- Built using **n-gram language models** with add-k smoothing
- Suggests the most probable next words given a prefix
- Covers vocabulary creation, n-gram counting, and probability estimation

### 2. [Autocorrect](./autocorrect/)
- Suggests corrections for misspelled words
- Combines **minimum edit distance (dynamic programming)** with word frequency
- Demonstrates string similarity and language modeling concepts

### 3. [RNN/GRU Text Generation](./rnn_gru_text_generation/)
- Implemented using **GRU-based recurrent neural networks**
- Generates text character-by-character given a seed sequence
- Covers:  
  - Character-level tokenization  
  - Embedding layers and GRU implementation using `tf.keras`  
  - Loss calculation using `SparseCategoricalCrossentropy` with `from_logits=True`  
  - Temperature-based sampling for creative text generation  
- Includes a notebook with full **training, evaluation, and generation pipeline**  

---

## 📚 Concepts Covered So Far
- Text preprocessing (tokenization, handling OOV words)  
- N-gram language models and add-k smoothing  
- Autocomplete based on conditional probabilities  
- Autocorrect using edit distance and frequency models  
- Character-level RNNs and GRU networks for generative modeling  
- Loss functions, optimizers, and log-perplexity evaluation  
- Temperature-based sampling for controlled randomness in text generation  
