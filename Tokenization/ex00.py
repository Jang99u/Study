from konlpy.tag import Okt

def tokenize_korean_sentence(sentence):
    okt = Okt()
    tokens = okt.morphs(sentence)  # 문장을 형태소로 분리하여 토큰화
    return tokens

if __name__ == "__main__":
    input_sentence = "한국어 토큰화를 해보는 예제입니다."
    tokens = tokenize_korean_sentence(input_sentence)
    print(tokens)