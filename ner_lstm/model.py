# model.py
import tensorflow as tf

def NER(len_tags, vocab_size, embedding_dim=50):
    model = tf.keras.Sequential(name='NER_Model')
    model.add(tf.keras.layers.Embedding(input_dim=vocab_size+1,
                                        output_dim=embedding_dim,
                                        mask_zero=True))
    model.add(tf.keras.layers.LSTM(units=embedding_dim,
                                   return_sequences=True))
    model.add(tf.keras.layers.Dense(units=len_tags,
                                    activation=tf.nn.log_softmax))
    return model

def masked_loss(y_true, y_pred):
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True, ignore_class=-1)
    return tf.reduce_mean(loss_fn(y_true, y_pred))

def masked_accuracy(y_true, y_pred):
    mask = tf.not_equal(y_true, -1)
    y_pred_class = tf.argmax(y_pred, axis=-1)
    matches = tf.cast(tf.equal(y_true, tf.cast(y_pred_class, tf.float32)), tf.float32)
    return tf.reduce_sum(matches * tf.cast(mask, tf.float32)) / tf.reduce_sum(tf.cast(mask, tf.float32))
