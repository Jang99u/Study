import numpy as np
import tensorflow as tf

# 데이터 준비
data = (np.array([1, 2, 3, 4]), np.array(['A', 'B', 'C', 'D']))

# 데이터셋 생성
dataset = tf.data.Dataset.from_tensor_slices(data)

# 데이터셋 사용
for item in dataset:
    print(list(item))