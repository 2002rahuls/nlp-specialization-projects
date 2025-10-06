import tensorflow as tf

def translate(model, text, max_length=50, temperature=0.7):
    """
    Generates a translation for a given input sentence using a trained Seq2Seq model.
    """
    text = tf.constant([text])
    context = model.source_vectorizer(text).to_tensor()
    context = model.encoder(context)

    sos_id = model.target_vectorizer('<SOS>')
    eos_id = model.target_vectorizer('<EOS>')
    next_token = tf.constant([[sos_id]], dtype=tf.int64)

    state = [tf.zeros((1, model.decoder.pre_attention_rnn.units)),
             tf.zeros((1, model.decoder.pre_attention_rnn.units))]

    tokens, logits_list = [], []
    done = False

    for _ in range(max_length):
        logits, state = model.decoder(context, next_token, state=state, return_state=True)
        logits = tf.squeeze(logits, axis=1)

        if temperature == 0.0:
            next_token = tf.argmax(logits, axis=-1, output_type=tf.int64)
        else:
            probs = tf.nn.softmax(logits / temperature)
            next_token = tf.random.categorical(tf.math.log(probs), num_samples=1)

        if next_token.numpy()[0, 0] == eos_id:
            break

        tokens.append(next_token)
        logits_list.append(logits)

    tokens = tf.concat(tokens, axis=-1)
    translation = model.tokens_to_text(tokens)
    return translation, logits_list[-1], tokens
