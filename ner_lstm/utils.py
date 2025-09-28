# utils.py
import tensorflow as tf
import numpy as np

def get_sentence_vectorizer(sentences):
    vectorizer = tf.keras.layers.TextVectorization(standardize=None)
    vectorizer.adapt(sentences)
    vocab = vectorizer.get_vocabulary()
    return vectorizer, vocab

def label_vectorizer(labels, tag_map):
    label_ids = []
    for element in labels:
        tokens = element.split(' ')
        element_ids = [tag_map[token] for token in tokens]
        label_ids.append(element_ids)
    # Manually pad sequences
    max_len = max(len(x) for x in label_ids)
    for i in range(len(label_ids)):
        pad_len = max_len - len(label_ids[i])
        label_ids[i] += [-1]*pad_len
    return tf.constant(label_ids, dtype=tf.int32)

def predict(sentence, model, sentence_vectorizer, tag_map):
    sentence_vectorized = sentence_vectorizer([sentence])
    output = model(sentence_vectorized)
    outputs = np.argmax(output, axis=-1)[0]
    labels = list(tag_map.keys())
    return [labels[idx] for idx in outputs]
