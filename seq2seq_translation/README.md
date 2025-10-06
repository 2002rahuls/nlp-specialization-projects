# Seq2Seq Translation

This project implements a sequence-to-sequence (Seq2Seq) neural network for English-to-Portuguese sentence translation using TensorFlow and Keras. It demonstrates the core concepts of encoder-decoder architectures, attention, and evaluation metrics for translation quality.

## Features

- **Encoder-Decoder Model:** LSTM-based encoder and decoder for sequence modeling
- **Custom Tokenization:** TextVectorization layers for both source and target languages
- **Translation Function:** Generates translations with temperature-based sampling for diversity
- **Evaluation Metrics:** Includes ROUGE-1 similarity and average overlap functions for translation quality
- **Jupyter Notebook:** Full pipeline for data preparation, model training, translation, and evaluation

## File Overview

- `Seq2Seq_Translation.ipynb`: Main notebook with code for data prep, model, training, translation, and evaluation
- `translator.py`: Contains the core translation function for generating output sentences
- `evaluation.py`: Implements ROUGE-1 and overlap-based evaluation functions

## Model Architecture

- **Encoder:** Embedding + LSTM to encode input sentences
- **Decoder:** Embedding + LSTM + Dense layer to generate output tokens
- **Training:** Teacher forcing with input and target batches
- **Inference:** Greedy or temperature-based sampling for translation

## Example Usage

```python
from translator import translate
translation, logits, tokens = translate(model, "i like apples", max_length=50, temperature=0.7)
print("Translation:", translation)
```

## Evaluation

- Use `evaluation.py` to compute ROUGE-1 similarity and average overlap between candidate and reference translations.

## Concepts Covered

- Sequence-to-sequence modeling
- Encoder-decoder architecture
- Tokenization and vectorization
- LSTM networks
- Teacher forcing
- Temperature-based sampling
- ROUGE metric for translation quality
