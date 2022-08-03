import torch
from transformers import DistilBertModel
import json
import os
import pathlib
import sys

scripts_dir = pathlib.Path(__file__).parent.resolve()
# model_path = os.path.join(scripts_dir, 'model.h5')
sys.path.append(str(scripts_dir))

# prerun to fetch model files
from prerun import download_model_files
download_model_files()

from bert_model import BERT_Arch
import predict_intent
import predict_sentiment

default_intents_file = os.path.join(scripts_dir, 'intents.json')
default_model_file = os.path.join(scripts_dir, 'intents_model.pt')
intents_file = os.environ.get('INTENTS_FILE', default_intents_file)
model_file = os.environ.get('MODEL_FILE', default_model_file)

if os.path.exists('/input/train'):
    model_file = '/input/train/extended_model_file.pt'
    intents_file = '/input/train/extended_intents.json'

f = open(intents_file)
intents = json.load(f)
number_of_labels = len(intents)
model = BERT_Arch(DistilBertModel.from_pretrained('distilbert-base-uncased'), number_of_labels)
model.load_state_dict(torch.load(model_file))

    
def predict(data):
    sentiment, score = predict_sentiment.predict(data)
    topic = predict_intent.predict(data, intents, model)
    return {"topic": topic, "sentiment": sentiment, "score": score}
