import sentencepiece as spm
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# 텍스트 데이터 예시
texts = [
    "Hello, how are you?",
    "I'm doing fine, thank you.",
    "This is a simple example of text preprocessing."
]

# SentencePiece 모델 학습
MODEL_PATH = "./Learning/07_Detokenization/model/"
spm.SentencePieceTrainer.Train('--input=./Learning/07_Detokenization/model/data.txt --model_prefix=./Learning/07_Detokenization/model/m --vocab_size=41')

# SentencePiece 모델 로드
sp = spm.SentencePieceProcessor()
sp.Load("./Learning/07_Detokenization/model/m.model")

# 텍스트 데이터를 서브워드로 분절
subword_sequences = [sp.EncodeAsPieces(text) for text in texts]

# Tokenizer 객체 생성
tokenizer = Tokenizer(num_words=41)  # 어휘 사이즈에 맞게 설정

# 서브워드를 문자열로 변환하여 어휘 사전 구축
subword_texts = [' '.join(subwords) for subwords in subword_sequences]
tokenizer.fit_on_texts(subword_texts)

# 텍스트를 숫자 시퀀스로 변환
sequences = tokenizer.texts_to_sequences(subword_texts)

# 패딩을 추가하여 시퀀스 길이를 맞춤
max_sequence_length = max([len(seq) for seq in sequences])
padded_sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='post')

# 어휘 사전 확인
word_index = tokenizer.word_index
print("Word Index:", word_index)

# 서브워드로 분절된 시퀀스 확인
print("Subword Sequences:", subword_sequences)

# 토큰화된 시퀀스 확인
print("Tokenized Sequences:", sequences)

# 패딩된 시퀀스 확인
print("Padded Sequences:", padded_sequences)
