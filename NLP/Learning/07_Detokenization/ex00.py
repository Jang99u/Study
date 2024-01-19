from keras.preprocessing.text import Tokenizer

texts = ["Hello world", "Keras is great", "Text preprocessing with Keras"]
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)

sequences = tokenizer.texts_to_sequences(texts)

# 숫자 시퀀스를 텍스트로 변환
reconstructed_texts = []
for sequence in sequences:
    reconstructed_text = " ".join([tokenizer.index_word[idx] for idx in sequence])
    reconstructed_texts.append(reconstructed_text)

print(reconstructed_texts)
