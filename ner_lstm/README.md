# Named Entity Recognition (NER) with LSTM

This project implements a simple Named Entity Recognition (NER) system using an LSTM neural network in TensorFlow/Keras. The model is trained on a small set of sample sentences and entity labels, and demonstrates core concepts of sequence labeling for NER tasks.

## Features

- LSTM-based sequence labeling for NER
- Custom masking for padded tokens
- Support for multiple entity types (PER, ORG, LOC, TIM)
- Easy-to-understand code for educational purposes

## Project Structure

- `train.ipynb`: Main notebook for training and testing the NER model
- `model.py`: Defines the LSTM model and custom loss/accuracy functions
- `sample_sentences.py`: Contains sample sentences and entity labels
- `utils.py`: Utility functions for vectorization and prediction
- `test.py`: Script for training and testing the model

## Getting Started

### Prerequisites

- Python 3.8+
- TensorFlow 2.x

Install dependencies:

```bash
pip install tensorflow
```

### Training the Model

1. Open `train.ipynb` in Jupyter Notebook or VS Code.
2. Run all cells to:
   - Load and vectorize sample sentences and labels
   - Build and compile the LSTM NER model
   - Train the model on the toy dataset
   - Test predictions on new sentences

Alternatively, run `test.py` to train and test the model in a script.

### Example Usage

```python
from sample_sentences import sentences, labels, tag_map
from utils import get_sentence_vectorizer, label_vectorizer, predict
from model import NER, masked_loss, masked_accuracy

# Vectorize
sentence_vectorizer, vocab = get_sentence_vectorizer(sentences)
y = label_vectorizer(labels, tag_map)

# Build model
model = NER(len_tags=len(tag_map), vocab_size=len(vocab))
model.compile(optimizer='adam', loss=masked_loss, metrics=[masked_accuracy])

# Train
model.fit(sentence_vectorizer(sentences), y, epochs=200, batch_size=2)

# Predict
sentence = "Apple is buying startup in London"
preds = predict(sentence, model, sentence_vectorizer, tag_map)
print(preds)
```

## Data Format

- Sentences: Plain text strings
- Labels: Space-separated entity tags (e.g., `B-PER`, `I-ORG`, `O`)
- Tag mapping: See `sample_sentences.py` for supported tags

## Model Details

- Embedding layer for word representations
- LSTM layer for sequence modeling
- Dense output layer with log-softmax activation
- Custom loss and accuracy functions to handle padding

## References

- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Sequence Labeling and NER](https://nlp.stanford.edu/software/CRF-NER.html)
