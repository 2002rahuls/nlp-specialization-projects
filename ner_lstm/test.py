from sample_sentences import sentences, labels, tag_map
from utils import get_sentence_vectorizer, label_vectorizer, predict
from model import NER, masked_loss, masked_accuracy

# Vectorize
sentence_vectorizer, vocab = get_sentence_vectorizer(sentences)
y = label_vectorizer(labels, tag_map)

# Build model
model = NER(len_tags=len(tag_map), vocab_size=len(vocab))
model.compile(optimizer='adam', loss=masked_loss, metrics=[masked_accuracy])

# Train heavily on toy data (overfit)
model.fit(sentence_vectorizer(sentences), y, epochs=200, batch_size=2)

# Test prediction
sentence = "Apple is buying INDIA startup in London"
preds = predict(sentence, model, sentence_vectorizer, tag_map)
print(preds)
