# Siamese Network for Sentence Similarity

This project demonstrates a simple Siamese neural network using LSTM layers to determine the similarity between pairs of sentences. The main use case is identifying duplicate questions, such as in FAQ or Q&A systems.

## Features

- Uses TensorFlow and Keras for model building
- Shared LSTM encoder for both input sentences
- Cosine similarity as the output metric
- Toy dataset for demonstration
- Training, evaluation, and prediction helper functions
- Jupyter notebook for step-by-step experimentation

## File Structure

- `siamese_notebook.ipynb`: Main notebook with code for data loading, preprocessing, model building, training, and evaluation
- `README.md`: Project documentation

## How It Works

1. **Data Preparation**: Pairs of sentences are tokenized and padded to a fixed length.
2. **Model Architecture**: Both sentences are passed through a shared embedding and LSTM encoder. Their outputs are compared using cosine similarity.
3. **Training**: The model is trained to predict whether sentence pairs are duplicates.
4. **Evaluation**: Accuracy is measured on a test set.
5. **Prediction**: A helper function allows quick similarity checks between new sentence pairs.

## Example Usage

See the notebook for code examples. Typical usage:

```python
predict("What is AI?", "Define artificial intelligence")
predict("How old are you?", "What’s your age?")
predict("What is AI?", "What is your name?")
```
