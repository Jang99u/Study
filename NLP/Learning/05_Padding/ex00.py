from keras.preprocessing.sequence import pad_sequences

# ������ ������ �غ�
sequences = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

# �е� �߰�
padded_sequences = pad_sequences(sequences, maxlen=4, padding='post')
print(padded_sequences)
