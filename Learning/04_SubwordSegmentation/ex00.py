import os
from subword_nmt.learn_bpe import learn_bpe
from subword_nmt.apply_bpe import BPE

# 데이터 로딩 (학습 데이터로 대체)
data = ["apple", "banana", "cherry", "date"]

# BPE 학습
bpe_codes_path = "bpe_codes.txt"
num_operations = 1000  # BPE 알고리즘 작업 수
with open("data.txt", "w") as f:
    f.write("\n".join(data))
learn_bpe(input="data.txt", output=bpe_codes_path, num_operations=num_operations)

# BPE 적용
bpe = BPE(open(bpe_codes_path))
subword_data = [bpe.process_line(line) for line in data]

# 출력
for original, subword in zip(data, subword_data):
    print(f"Original: {original} | Subword: {subword}")
