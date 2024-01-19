from keras.preprocessing.sequence import pad_sequences

sequences = [
    [1, 2, 3, 4, 5],
    [6, 7, 8],
    [9, 10, 11, 12, 13, 14, 15]
]

padded_sequences = pad_sequences(sequences, maxlen=4, padding='post')
print(padded_sequences)
