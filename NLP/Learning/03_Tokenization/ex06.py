from keras.preprocessing.text import Tokenizer

# 텍스트 데이터
texts = ["Hello world", "Keras is great", "Text preprocessing with Keras"]

# Tokenizer 객체 생성
tokenizer = Tokenizer()

# 토큰화 및 정수 인코딩 수행
# 주어진 텍스트에 포함된 단어나 서브워드들을 토큰화하여 어휘 사전을 구축
tokenizer.fit_on_texts(texts)

# 텍스트를 정수 시퀀스로
sequences = tokenizer.texts_to_sequences(texts)
print(sequences)
