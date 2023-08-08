import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import layers
import numpy as np
import pandas as pd
import os
import json
import pickle
from tqdm import tqdm
from konlpy.tag import Okt
from keras.preprocessing.text import Tokenizer
from keras.models import save_model
from keras.utils import to_categorical
import re

okt = Okt()
tokenizer = Tokenizer()

class EmotionAnalyzer:
    def __init__(self):
        DATA_PATH = './NLP/Model_/data/CLEAN_DATA/'
        DATA_OUT = './NLP/Model_/data/DATA_OUT/'
        INPUT_TRAIN_DATA = 'nsmc_train_input.npy'
        LABEL_TRAIN_DATA = 'nsmc_train_label.npy'
        DATA_CONFIGS = 'data_configs.json'

        self.train_input = np.load(open(DATA_PATH + INPUT_TRAIN_DATA, 'rb'), allow_pickle=True)
        self.train_input = pad_sequences(self.train_input, maxlen=self.train_input.shape[1])
        self.train_label = np.load(open(DATA_PATH + LABEL_TRAIN_DATA, 'rb'), allow_pickle=True)
        self.prepro_configs = json.load(open(DATA_PATH + DATA_CONFIGS, 'r'))
        self.word_vocab = self.prepro_configs['vocab']

        self.tokenizer = Tokenizer()
        self.tokenizer.fit_on_texts(self.word_vocab)

        MAX_LENGTH = 8  # 문장 최대 길이

        model_name = 'cnn_classifier_kr'
        BATCH_SIZE = 512
        NUM_EPOCHS = 10
        VALID_SPLIT = 0.1
        MAX_LEN = self.train_input.shape[1]

        kargs = {'model_name': model_name, 'vocab_size': self.prepro_configs['vocab_size'], 'embbeding_size': 128,
                 'num_filters': 100, 'dropout_rate': 0.5, 'hidden_dimension': 250, 'output_dimension': 1}

        @tf.keras.utils.register_keras_serializable()
        class CNNClassifier(tf.keras.Model):

            def __init__(self, **kargs):
                super(CNNClassifier, self).__init__(name=kargs['model_name'])
                self.embedding = layers.Embedding(input_dim=kargs['vocab_size'], output_dim=kargs['embbeding_size'])
                self.conv_list = [layers.Conv1D(filters=kargs['num_filters'], kernel_size=kernel_size, padding='valid',activation = tf.keras.activations.relu,
                                                kernel_constraint = tf.keras.constraints.MaxNorm(max_value=3)) for kernel_size in [3,4,5]]
                self.pooling = layers.GlobalMaxPooling1D()
                self.dropout = layers.Dropout(kargs['dropout_rate'])
                self.fc1 = layers.Dense(units=kargs['hidden_dimension'],
                                        activation = tf.keras.activations.relu,
                                        kernel_constraint=tf.keras.constraints.MaxNorm(max_value=3.))
                self.fc2 = layers.Dense(units=3,  # 수정할 부분 : 출력 차원 변경
                                        activation=tf.keras.activations.softmax,  # 활성화 함수 변경
                                        kernel_constraint= tf.keras.constraints.MaxNorm(max_value=3.))

            def call(self,x):
                x = self.embedding(x)
                x = self.dropout(x)
                x = tf.concat([self.pooling(conv(x)) for conv in self.conv_list], axis = 1)
                x = self.fc1(x)
                x = self.fc2(x)
                return x

        self.model = CNNClassifier(**kargs)
        self.model.compile(optimizer=tf.keras.optimizers.Adam(),
                           loss=tf.keras.losses.CategoricalCrossentropy(),
                           metrics=[tf.keras.metrics.CategoricalAccuracy(name='accuracy')])

        self.train_label = to_categorical(self.train_label, num_classes=3)

        earlystop_callback = EarlyStopping(monitor='val_accuracy', min_delta=0.0001, patience=2)
        checkpoint_path = DATA_OUT + model_name + '\weights.h5'
        checkpoint_dir = os.path.dirname(checkpoint_path)

        if os.path.exists(checkpoint_dir):
            print("{} -- Folder already exists \n".format(checkpoint_dir))
        else:
            os.makedirs(checkpoint_dir, exist_ok=True)
            print("{} -- Folder create complete \n".format(checkpoint_dir))

        cp_callback = ModelCheckpoint(
            checkpoint_path, monitor='val_accuracy', verbose=1, save_best_only=True,
            save_weights_only=True
        )

        history = self.model.fit(self.train_input, self.train_label, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS,
                                 validation_split=VALID_SPLIT, callbacks=[earlystop_callback, cp_callback])

        save_model(self.model, './NLP/Model_/')

    def analyze_emotion(self, input_text):
        sentence = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣\\s ]', '', input_text)
        stopwords = ['은', '는', '이', '가', '하', '아', '것', '들', '의', '있', '되', '수', '보', '주', '등', '한']
        sentence = okt.morphs(sentence, stem=True)
        sentence = [word for word in sentence if not word in stopwords]
        vector = self.tokenizer.texts_to_sequences([sentence])
        pad_new = pad_sequences(vector, maxlen=8)

        model_path = './data/DATA_OUT/cnn_classifier_kr/weights.h5'
        self.model.load_weights(model_path)
        predictions = self.model.predict(pad_new)

        emotions = np.array(predictions)
        emotion_labels = ['불안', '분노', '기쁨']

        def summarize_emotion(emotions, threshold=0.35):
            summary = []
            for e in emotions:
                dominant_emotion = np.argmax(e)
                if e[dominant_emotion] > threshold:
                    summary.append(emotion_labels[dominant_emotion])
            return summary

        overall_summary = summarize_emotion(emotions)
        return overall_summary
    