# One-hot encoding

from keras.utils import to_categorical

labels = [0, 1, 2]
one_hot_labels = to_categorical(labels, num_classes=3)
print(one_hot_labels)
