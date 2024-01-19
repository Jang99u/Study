from keras.preprocessing.sequence import pad_sequences

# 시퀀스 데이터 준비
sequences = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]

# 패딩 추가
padded_sequences = pad_sequences(sequences, maxlen=4, padding='post')
print(padded_sequences)
