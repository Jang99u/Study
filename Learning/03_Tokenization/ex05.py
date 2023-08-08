from keras.preprocessing.text import Tokenizer

# 텍스트 데이터 준비
texts = ['I love programming', 'Python is great', 'Machine learning is fun']

# Tokenizer 객체 생성
tokenizer = Tokenizer()

# 텍스트 데이터를 기반으로 토큰화 및 정수 인코딩 수행
tokenizer.fit_on_texts(texts)

# 단어 사전 확인
word_index = tokenizer.word_index
print(word_index)

# 텍스트 데이터를 정수 시퀀스로 변환
sequences = tokenizer.texts_to_sequences(texts)
print(sequences)