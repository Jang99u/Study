# Sentence Segmentation

from konlpy.tag import Kkma

def tokenize_and_segment(sentence):
    kkma = Kkma()
    sentences = kkma.sentences(sentence)  # 문장 분리
    tokens_list = [kkma.morphs(sent) for sent in sentences]  # 문장 내 토큰화
    return tokens_list

if __name__ == "__main__":
    input_text = "안녕하세요. 한국어 문장 분리와 토큰화를 테스트해보는 예제입니다. 잘 동작하는지 확인해보세요!"
    result = tokenize_and_segment(input_text)
    for tokens in result:
        print(tokens)