import os
from subword_nmt.learn_bpe import learn_bpe
from subword_nmt.apply_bpe import BPE

# ������ �ε� (�н� �����ͷ� ��ü)
data = ["apple", "banana", "cherry", "date"]

# BPE �н�
bpe_codes_path = "bpe_codes.txt"
num_operations = 1000  # BPE �˰��� �۾� ��
with open("data.txt", "w") as f:
    f.write("\n".join(data))
learn_bpe(input="data.txt", output=bpe_codes_path, num_operations=num_operations)

# BPE ����
bpe = BPE(open(bpe_codes_path))
subword_data = [bpe.process_line(line) for line in data]

# ���
for original, subword in zip(data, subword_data):
    print(f"Original: {original} | Subword: {subword}")
