from konlpy.tag import Okt

okt = Okt()
sentence = "그녀는 공원에서 산책하며 꽃을 구경했습니다."

morphs_stem = okt.morphs(sentence, stem=True)
morphs_no_stem = okt.morphs(sentence, stem=False)

print("With Stemming:", morphs_stem)
print("Without Stemming:", morphs_no_stem)