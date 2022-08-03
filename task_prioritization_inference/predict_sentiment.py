import os 
import argparse
import pandas as pd
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, SpatialDropout1D
from tensorflow.keras.layers import Embedding
import pickle
import pathlib
import sys

scripts_dir = pathlib.Path(__file__).parent.resolve()
default_model_file = os.path.join(scripts_dir, 'sentiment_model.h5')
default_tokenizer_file = os.path.join(scripts_dir, 'tokenizer.pickle')


def predict(data):
    model = keras.models.load_model(default_model_file)
    with open(default_tokenizer_file, 'rb') as handle:
        tokenizer = pickle.load(handle)
    sentiment_label = ['negative', 'positive']
    # Tokenize text
    x_test = pad_sequences(tokenizer.texts_to_sequences([data['input_text']]), maxlen=300)
    # Predict
    score = model.predict([x_test])[0]
    # Decode sentiment
    label = sentiment_label[int(score.round().item())]
    return label, score.item()
