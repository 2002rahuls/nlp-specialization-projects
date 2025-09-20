# RNN/GRU Language Model

This project implements a character-level language model using Recurrent Neural Networks (RNNs) and Gated Recurrent Units (GRUs) in TensorFlow. The model is trained on the complete works of William Shakespeare to generate text and evaluate language modeling performance.

## Features

- Character-level language modeling
- GRU-based neural network architecture
- Temperature-controlled text generation
- Log perplexity evaluation
- Model saving in TensorFlow SavedModel format

## Project Structure

- `rnn_lm.ipynb`: Main Jupyter notebook for model training, evaluation, and text generation
- `data/input_text.txt`: Training corpus (Shakespeare's works)
- `saved_model/grulm_model/`: Directory containing the trained model

## Getting Started

### Prerequisites

- Python 3.8+
- TensorFlow 2.x
- NumPy

Install dependencies:

```bash
pip install tensorflow numpy
```

### Training the Model

1. Open `rnn_lm.ipynb` in Jupyter Notebook or VS Code.
2. Run all cells to:
   - Load and preprocess the dataset
   - Build and compile the GRU language model
   - Train the model on the dataset
   - Evaluate log perplexity
   - Generate sample text
   - Save the trained model

### Generating Text

After training, use the `GenerativeModel` class in the notebook to generate text samples:

```python
# Example usage
print(gen_model.generate_n_chars(200, prefix="I have a great"))
```

You can adjust the `temperature` parameter for more or less randomness in generation.

### Evaluating Log Perplexity

The notebook includes code to compute log perplexity on a batch of data:

```python
lp = log_perplexity(preds, target_batch)
print("Log Perplexity:", lp.numpy())
```

### Saving and Loading the Model

The trained model is saved in `saved_model/grulm_model/` using TensorFlow's SavedModel format:

```python
model.save("saved_model/grulm_model")
```

You can load the model later for inference or further training.

## Dataset

The model is trained on Shakespeare's complete works (`data/input_text.txt`). You can replace this file with any other large text corpus for different results.

## References

- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Character-level Language Modeling](https://karpathy.github.io/2015/05/21/rnn-effectiveness/)
