from keras.preprocessing.text import Tokenizer

# �ؽ�Ʈ ������ �غ�
texts = ['I love programming', 'Python is great', 'Machine learning is fun']

# Tokenizer ��ü ����
tokenizer = Tokenizer()

# �ؽ�Ʈ �����͸� ������� ��ūȭ �� ���� ���ڵ� ����
tokenizer.fit_on_texts(texts)

# �ܾ� ���� Ȯ��
word_index = tokenizer.word_index
print(word_index)

# �ؽ�Ʈ �����͸� ���� �������� ��ȯ
sequences = tokenizer.texts_to_sequences(texts)
print(sequences)