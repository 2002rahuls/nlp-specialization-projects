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

### 3. [RNN/GRU Text Generation](./rnn_language_model/)

- Implemented using **GRU-based recurrent neural networks**
- Generates text character-by-character given a seed sequence
- Covers:
  - Character-level tokenization
  - Embedding layers and GRU implementation using `tf.keras`
  - Loss calculation using `SparseCategoricalCrossentropy` with `from_logits=True`
  - Temperature-based sampling for creative text generation
- Includes a notebook with full **training, evaluation, and generation pipeline**

### 4. [NER with LSTM](./ner_lstm/)

- Implements **Named Entity Recognition** using an LSTM neural network
- Trains on sample sentences with entity tags (PER, ORG, LOC, TIM)
- Demonstrates sequence labeling, masking, and custom loss/accuracy for padded tokens
- Includes notebook and script for training and prediction

### 5. [Siamese Network](./siamese_network/)

- Implements a **Siamese neural network** for sentence similarity
- Uses twin subnetworks with shared weights to compare input pairs
- Demonstrates contrastive loss and distance-based similarity scoring
- Includes a notebook for training and evaluating on sample sentence pairs

### 6. [Seq2Seq Translation](./seq2seq_translation/)

- Implements a **sequence-to-sequence (Seq2Seq) neural network** for English-to-Portuguese translation
- Uses LSTM-based encoder-decoder architecture with custom tokenization
- Supports temperature-based sampling for diverse translations
- Includes ROUGE-1 and overlap-based evaluation metrics
- Jupyter notebook demonstrates data prep, model training, translation, and evaluation

---

## 📚 Concepts Covered So Far

- Text preprocessing (tokenization, handling OOV words)
- N-gram language models and add-k smoothing
- Autocomplete based on conditional probabilities
- Autocorrect using edit distance and frequency models
- Character-level RNNs and GRU networks for generative modeling
- Loss functions, optimizers, and log-perplexity evaluation
- Temperature-based sampling for controlled randomness in text generation
- Sequence labeling for NER with LSTM
- Masking and handling padded tokens in sequence models
- Custom loss and accuracy functions for sequence tasks
- Sentence similarity modeling using Siamese networks and contrastive loss
- Sequence-to-sequence translation with encoder-decoder LSTM architecture
- ROUGE and overlap-based evaluation for translation quality
