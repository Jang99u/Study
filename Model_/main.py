import pickle
from emotion_analysis_module import EmotionAnalyzer

# 모델 객체 생성
analyzer = EmotionAnalyzer()

# 학습된 모델 불러오기
analyzer.load_model('trained_model.h5')

# 피클 파일로 저장
with open('emotion_analyzer.pkl', 'wb') as f:
    pickle.dump(analyzer, f)

# 피클 파일 로드
with open('emotion_analyzer.pkl', 'rb') as f:
    loaded_analyzer = pickle.load(f)

# 감정 분석 수행 및 결과 출력
input_text = input('감성 분석할 문장을 입력해주세요: ')
result = loaded_analyzer.analyze_emotion(input_text)
print("입력 문장:", input_text)
print("감정 분석 결과:", result)