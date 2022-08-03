import numpy as np
import re
import torch
import random
import transformers
from sklearn.preprocessing import LabelEncoder
from transformers import DistilBertTokenizer, DistilBertModel
from bert_model import BERT_Arch
import json
from transformers import logging
import os


# logging.set_verbosity_warning()
logging.set_verbosity_error()

# specify GPU
device = torch.device('cpu')


def predict(data, intents, model):
    message = data['input_text']
    # Converting the labels into encodings
    le = LabelEncoder()
    lst = []
    for i in intents:
        lst = lst + [i]
    lst = le.fit_transform(lst)
    message = re.sub(r'[^a-zA-Z ]+', '', message)
    test_text = [message]
    model.eval()
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    tokens_test_data = tokenizer(test_text, max_length=8, padding='max_length',
                                 truncation=True, return_token_type_ids=False)
    test_seq = torch.tensor(tokens_test_data['input_ids'])
    test_mask = torch.tensor(tokens_test_data['attention_mask'])
    preds = None
    with torch.no_grad():
        preds = model(test_seq.to(device), test_mask.to(device))
    sm = torch.nn.Softmax(dim=1)
    probabilities = sm(preds)
    preds = preds.detach().cpu().numpy()
    preds = np.argmax(preds, axis=1)
    return le.inverse_transform(preds)[0]
